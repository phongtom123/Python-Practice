a = []
n = int(input("Nhập giá trị n: "))

for i in range(n):
    x = int(input(f"Nhập giá trị a[{i}]: "))
    a.append(x)

for i in range(n):
    print(a[i], end = " ")

def find_max(a):
    max_val=0
    for i in range(n):
        if a[i] > max_val:
            max_val=a[i]
    return max_val
def find_min(a):
    min_val=99999
    for i in range(n):
        if a[i] < min_val:
            min_val = a[i]
    return min_val

def find_max2(a):
    max2_val=None
    for i in range(n):
        if (a[i] < find_max(a)) and (a[i] > find_min(a)):
            max2_val = a[i]
    return max2_val

print()
print("Max:", find_max(a))
print("Min:", find_min(a))
print("Max2:", find_max2(a))