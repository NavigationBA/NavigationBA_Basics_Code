def test_func_v3(a, b, c=1, d=2):
    return a + b + c + d

# 按顺序传入参数
result1 = test_func_v3(3, 4)       # a=3, b=4, c 使用默认值, d 使用默认值
result2 = test_func_v3(3, 4, 5)    # a=3, b=4, c=5, d 使用默认值
result3 = test_func_v3(3, 4, 5, 6) # a=3, b=4, c=5, d=6

# 传入参数，使用参数名
result4 = test_func_v3(b=4, a=3)
result5 = test_func_v3(d=6, a=3, b=4)

# 如果带参数名和不带参数名混用，规则就会比较混乱，以下代码都不会报错，只是可读性很差：
result6 = test_func_v3(3, b=4, d=6)
result7 = test_func_v3(3, 4, d=6)
result8 = test_func_v3(3, 4, c=5)
result9 = test_func_v3(3, 4, c=5, d=6)
result10 = test_func_v3(c=5, d=6, b=4, a=3) 
