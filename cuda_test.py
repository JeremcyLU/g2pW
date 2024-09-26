import torch

# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# print(device)
print(torch.cuda.is_available()) # 查看pytorch是否支持CUDA
print(torch.cuda.device_count()) # 查看可用的CUDA数量
# torch.version.cuda # 查看对应CUDA的版本号
