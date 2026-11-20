# list = [x for x in range(5)]

# pets = ["dog", "cat", "rabbit", "fish"]
# pets.append("chick")  # 向列表的最后追加元素
# pets.append("cat")  # 向列表的最后追加元素
# print(pets)  # ['dog', 'cat', 'rabbit', 'fish', 'chick']
# pets.insert(0, "snake")  # 在索引 0 位置处插入 'snake'，其他元素后移
# print(pets)  # ['snake', 'dog', 'cat', 'rabbit', 'fish', 'chick']
# pets.pop()  # 移出列表末尾的元素
# print(pets)  # ['snake', 'dog', 'cat', 'rabbit', 'fish']
# pets.remove("rabbit")  # 移除值为 'rabbit' 的元素，所要移除的值必须在列表中
# print(pets)  # ['snake', 'dog', 'cat', 'fish']
# del pets[0]  # 删除列表中索引为 0 的元素
# print(pets)  # ['dog', 'cat', 'fish']
# del pets  # 删除整个列表，pets 变量将不复存在

scores = [78.5, 79.0, 67.0, 89.0]
a = [1, 2, 3]
b = scores + a
scores.sort(reverse=True)
sorted(scores)
