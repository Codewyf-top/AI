import torch
import numpy as np
"""
np_data = np.arange(6).reshape((2,3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()

print(
    '\nnumpy',np_data,
    '\ntorch',torch_data,
    '\ntensor2numpy',tensor2array
)
"""

#abs
"""
data = [-1,-2,1,2]
tensor = torch.FloatTensor(data)#转换为32位

print(
    '\nabs',
    '\nnumpy:',np.abs(data),
    '\ntorch:',torch.abs(tensor) #.sin   .mean平均值
)"""

data = [[1,2],[3,4]]
tensor = torch.FloatTensor(data)

print(
     '\nnumpy:',np.matmul(data,data),
     '\ntorch:',torch.mm(tensor,tensor)
 )