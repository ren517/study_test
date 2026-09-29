import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# ===============================
# 1. Tensor 基础操作
# ===============================

x = torch.arange(24, dtype=torch.float32).reshape(2, 3, 4)

print("shape:", x.shape)
print("dtype:", x.dtype)
print("device:", x.device)


# 取第2个维度
print("取第2列shape:", x[:, 1, :].shape)

# reshape + 增加维度
print("reshape:", x.reshape(2, 12).unsqueeze(1).shape)


# cat拼接
print("cat:", torch.cat((x, x)).shape)


# 矩阵乘法
a = torch.ones(2, 3)
b = torch.ones(3, 2)

print("矩阵乘法:")
print(a @ b)


# ===============================
# 2. FashionMNIST数据集
# ===============================

data = datasets.FashionMNIST(
    "data", train=True, download=True, transform=transforms.ToTensor()
)


loader = DataLoader(data, batch_size=64, shuffle=True)


images, labels = next(iter(loader))


print("\nFashionMNIST:")
print("images.shape:", images.shape)
print("labels.shape:", labels.shape)
print("dtype:", images.dtype)
print("device:", images.device)


# ===============================
# 3. 逐元素运算
# ===============================

# images形状:
# [64, 1, 28, 28]

result = images * 2

print("\n逐元素乘法:")
print(result.shape)


# ===============================
# 4. 广播
# ===============================

bias = torch.tensor([0.5])

broadcast_result = images + bias

print("\n广播:")
print(broadcast_result.shape)


# ===============================
# 5. 一次矩阵乘法
# ===============================

m1 = torch.ones(2, 3)
m2 = torch.ones(3, 4)

matrix_result = m1 @ m2

print("\n矩阵乘法结果:")
print(matrix_result.shape)


# ===============================
# 6. 可视化16张图片
# ===============================

plt.figure(figsize=(8, 8))


for i in range(16):

    plt.subplot(4, 4, i + 1)

    # 灰度图
    plt.imshow(images[i].squeeze(), cmap="gray")

    plt.title(str(labels[i].item()))

    plt.axis("off")


plt.tight_layout()
plt.show()
