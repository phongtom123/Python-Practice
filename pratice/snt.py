import math

n = int(input("nhập n:"))
# x = int(input("Nhập vào số x: "))

# def Boolean(x):
#     if x > 0:
#         for i in range(2,int(math.sqrt(x)) + 1):
#             if (x % i==0):
#                 print("ok")
#                 return False
#         return True

# if Boolean(x):
#     print("la snt")
# else:
#     print("khong la snt")

# def Boolean(x):
#     if x > 0:
#         for i in range(2,x):
#             if (x % i==0):
#                 return False
#         return True

def Boolean(x):
    if x > 0:
        for i in range(2,int(math.sqrt(x)) + 1):
            if (x % i==0):
                return False
        return True
    
for i in range(2, n):
    if Boolean(i):
        print(i, end=" ")