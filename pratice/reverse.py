s = str(input("Nhập vào 1 chuỗi: "))
rev = s[::-1]
print(rev)

def palindrome(s):
    s = s.lower()

    return s == s[::-1]

print(palindrome(s))