from __future__ import print_function
import torch
#Tensors 张量
#张量类似于numpy的ndarrays，但是张量可以使用GPU来加速计算

"""x = torch.Tensor(5,3)
print(x)

y = torch.zeros(5,3,dtype=torch.long)
print(y)

z = torch.tensor([5.5,3])
print(z)

z = z.new_ones(5,3,dtype=torch.double)
print(z)

z = torch.rand_like(z,dtype=torch.float)#覆盖类型
print(z)                                #result的size相同
print(z.size())"""

x = torch.zeros(5,3,dtype=torch.double)
print(x)

y = torch.rand(5,3)
"""print(x + y)

print(torch.add(x,y))

result = torch.empty(5,3)
torch.add(x,y,out=result)
print(result)"""

y.add_(x)
print(y)

