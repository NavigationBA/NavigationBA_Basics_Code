print("isinstance基本用法函数示例")

a = 100
b = 3.14
c = "Hello"
d = True
e = [1, 2, 3]
f = (4, 5, 6)
g = {7, 8, 9}
h = {"name": "Alice", "age": 30}

print(isinstance(a, int))        
print(isinstance(b, float))      
print(isinstance(c, str))        
print(isinstance(d, bool))       
print(isinstance(e, list))       
print(isinstance(f, tuple))      
print(isinstance(g, set))       
print(isinstance(h, dict))


print("判断None类型")
x = None
print(isinstance(x, type(None)))