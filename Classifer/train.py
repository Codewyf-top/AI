import torch
from torch import optim
from torch import nn
import argparse
from model.RESNET import resnet18,resnet34,resnet50,resnet101,resnet152
import os
import numpy as np
import random
from torchvision.datasets import ImageFolder
from torch.optim.lr_scheduler import _LRScheduler
from torch.utils.tensorboard import SummaryWriter                         #import tensorboard
#from tensorboardX import SummaryWriter                                   #导入可视化工具TensorboardX
from torch.autograd import Variable
from utils.utils import WarmUpLR,get_acc,load_config,train_tf,test_tf

#writer = SummaryWriter() #tensorboard可视化工具初始化
def main(mode=None):
    
    config = load_config(mode)
    
    torch.manual_seed(config.SEED)                  #为CPU设计种子用于生成随机数，以使得结果是确定的
    torch.cuda.manual_seed(config.SEED)             #为GPU设置随机种子，可以保证每次初始化相同
    np.random.seed(config.SEED)
    random.seed(config.SEED)
    
    train_set = ImageFolder(config.TRAIN_PATH, transform=train_tf)                                  #设置训练路径
    length_train = len(train_set)               #return the number of items in a container
    train_data=torch.utils.data.DataLoader(train_set,batch_size=config.BATCH_SIZE,shuffle=True)     #
    iter_per_epoch = len(train_data)            #return the number of per epoch

    test_set = ImageFolder(config.TEST_PATH, transform=test_tf)
    length_test = len(test_set)
    test_data=torch.utils.data.DataLoader(test_set, batch_size=config.BATCH_SIZE, shuffle=True)
    
    # INIT GPU初始化GPU
    os.environ['CUDA_VISIBLE_DEVICES'] = ','.join(str(e) for e in config.GPU)
    if torch.cuda.is_available():
        config.DEVICE = torch.device("cuda")
        print('\nGPU IS AVAILABLE')
        torch.backends.cudnn.benchmark = True
    else:
        config.DEVICE = torch.device("cpu")

     # choose network选择一个网络
    net = resnet18().to(config.DEVICE)          #使用resnet18
    print('The Model is ResNet18\n')

    # optimizer and loss function       优化和损失函数
    optimizer = optim.SGD(net.parameters(),lr=config.LR,momentum=0.9,weight_decay=5e-4)     #Stochastic Gradient Descent随机梯度下降
    loss_function = nn.CrossEntropyLoss()                                                   #交叉熵损失函数

    # warmup
    train_scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=config.MILESTONES,gamma=0.5)#调整学习率learning rate
    # milestons是数组，gamma是倍数,LR初始值为0.01，当milestones达到所设置的3，6，9时，lr的数值乘以gamma，即倍数
    warmup_scheduler = WarmUpLR(optimizer, iter_per_epoch * config.WARM)
                 
    # create checkpoint folder to save model
    model_path = os.path.join(config.PATH,'model')
    if not os.path.exists(model_path):
        os.mkdir(model_path)
    checkpoint_path = os.path.join(model_path,'{epoch}-{type}.pth')
                 
    best_acc = 0.0
    a = config.EPOCH

    for epoch in range(1, config.EPOCH):

        if epoch > config.WARM:
            train_scheduler.step(epoch)
    
        ### train ###
        net.train()   
        train_loss = 0.0 # cost function error
        train_correct = 0.0

        for i, data in enumerate(train_data):

            if epoch <= config.WARM:
                warmup_scheduler.step()

            length = len(train_data)
            image, label = data
            image, label = image.to(config.DEVICE),label.to(config.DEVICE)

            output = net(image)
            train_correct += get_acc(output, label)
            loss = loss_function(output, label)
            train_loss +=loss.item()

            # backward
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            print('Training Epoch: {epoch} [{trained_samples}/{total_samples}]\tLoss: {:0.4f}\tAcc: {:0.4f}\tLR: {:0.6f}'.format(
                train_loss/(i+1),
                train_correct/(i+1),
                optimizer.param_groups[0]['lr'],
                epoch=epoch,
                trained_samples=i * config.BATCH_SIZE + len(image),
                total_samples=length_train
            ))
        
        ### eval ### 
        net.eval()
        test_loss = 0.0     # cost function error
        test_correct = 0.0

        for i, data in enumerate(test_data):
            images, labels = data
            images, labels = images.to(config.DEVICE),labels.to(config.DEVICE)

            outputs = net(images)
            loss = loss_function(outputs, labels)
            test_loss += loss.item()
            test_correct += get_acc(outputs, labels)
            
            print('Testing: [{test_samples}/{total_samples}]\tAverage loss: {:.4f}, Accuracy: {:.4f}'.format(
            test_loss /(i+1),
            test_correct / (i+1),
            test_samples=i * config.BATCH_SIZE + len(images),
            total_samples=length_test
        ))
        print()

        #start to save best performance model 保存当前训练的最佳的模型
        acc = test_correct/(i+1)  
        if epoch > config.MILESTONES[1] and best_acc < acc:
            torch.save(net.state_dict(), checkpoint_path.format(epoch=epoch, type='best'))
            best_acc = acc
            continue

        if not epoch % config.SAVE_EPOCH:
            torch.save(net.state_dict(), checkpoint_path.format(epoch=epoch, type='regular'))
                 
if __name__ == "__main__":
    main()
