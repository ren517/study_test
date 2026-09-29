import torch

x = torch.rand(2, 3, 4, dtype=torch.float32)

print("shape:", x.shape)
print("dtype:", x.dtype)
print("device:", x.device)

y = torch.rand(3, 4)

col = y[:, 1]
print(col)
print(col.shape)
print(col.dtype)

z = torch.rand(2, 3, 4)
z = z.reshape(2, 12)
print("\n3.")
print("reshape后:", z.shape)

z = z.unsqueeze(0)
print("unsqueeze后:", z.shape)

x1 = torch.rand(2, 3)
x2 = torch.rand(2, 3)
x = torch.cat([x1, x2], dim=0)
print(x.shape)
x = torch.stack([x1, x2], dim=0)
print(x.shape)

result = x1 * x2
print(result.shape)

a = torch.rand(2, 3)
b = torch.rand(3, 2)
matrix_result = a @ b
print(matrix_result)
