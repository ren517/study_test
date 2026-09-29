import torch

print(1.0)
x1 = torch.zeros(2, 2)
print(x1.shape)
print(x1.ndim)
print(x1.dtype)

x1 = torch.zeros(2, 2, 2)
print(x1.shape)
print(x1.ndim)
print(x1.dtype)

x1 = torch.zeros(2, 2, 2, 2)
print(x1.shape)
print(x1.ndim)
print(x1.dtype)

print(2.0)
x2 = torch.ones(2, 2)
print(x2.shape)
print(x2.ndim)
print(x2.dtype)

x2 = torch.ones(2, 2)
print(x2.shape)
print(x2.ndim)
print(x2.dtype)

x2 = torch.ones(2, 2, 2)
print(x2.shape)
print(x2.ndim)
print(x2.dtype)

x2 = torch.ones(2, 2, 2, 2)
print(x2.shape)
print(x2.ndim)
print(x2.dtype)

print(3.0)
x3 = torch.rand(2, 2)
print(x3.shape)
print(x3.ndim)
print(x3.dtype)

x3 = torch.rand(2, 2, 2)
print(x3.shape)
print(x3.ndim)
print(x3.dtype)

x3 = torch.rand(2, 2, 2, 2)
print(x3.shape)
print(x3.ndim)
print(x3.dtype)

print(4.0)
x4 = torch.arange(4).reshape(2, 2)
print(x4.shape)
print(x4.ndim)
print(x4.dtype)

x4 = torch.arange(8).reshape(2, 2, 2)
print(x4.shape)
print(x4.ndim)
print(x4.dtype)


x4 = torch.arange(16).reshape(2, 2, 2, 2)
print(x4.shape)
print(x4.ndim)
print(x4.dtype)
