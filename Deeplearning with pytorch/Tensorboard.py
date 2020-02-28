from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")
x = range(100)
for i in x:
    writer.add_scalar('y=2x', i * 2, i)
writer.close()
#tensorboard --logdir logs
