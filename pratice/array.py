m = int(input("Nhập giá trị m: "))
n = int(input("Nhập giá trị n: "))
# a= []

# for i in range(n):
#     x = int(input(f"Nhập giá trị a[{i}]: "))
#     a.append(x)

# for i in range(n):
#     print(a[i], end = " ")

a = []

for i in range(m):
    row = []
    for j in range(n):
        x = int(input(f"Nhập giá trị a[{i}][{j}]: "))
        row.append(x)
    a.append(row)

print(a)

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end = " ")
#     print()