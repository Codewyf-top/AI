import numpy
import torch
x = torch.rand(4,4)
print(x[:,1])

y = x.view(16)

z = x.view(-1,8) #-1->没有指定维度

print(x.size(),y.size(),z.size())

x = torch.randn(1)
print(x)
print(x.item())