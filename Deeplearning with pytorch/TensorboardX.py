import torch
import numpy as np
from tensorboardX import SummaryWriter


writer = SummaryWriter()
for epoch in range(100):
    writer.add_scalar('scalar/test',np.random.rand(),epoch)
    writer.add_scalars('scalar/scalars_test',{'xsinx':epoch*np.sin(epoch),'xcosx':epoch*np.cos(epoch)},epoch)

writer.close()

'''运行代码之后生成文件之后，我们在runs同级目录下使用命令行：
tensorboard --logdir runs. 
当SummaryWriter(log_dir='scalar')的log_dir的参数值 存在时，
将tensorboard --logdir runs 改为 tensorboard --logdir 参数值
'''