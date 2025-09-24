s = "Hello Python!"

print("不填步长的切片：")
print(s[:])
print(s[1:])
print(s[:5])
print(s[1:5])

print("填入步长后的切片：")
print(s[::])
print(s[::1])
print(s[::2])
print(s[3::2])
print(s[:8:2])
print(s[3:8:2])
print(s[3:-2:2])
print(s[::-1])