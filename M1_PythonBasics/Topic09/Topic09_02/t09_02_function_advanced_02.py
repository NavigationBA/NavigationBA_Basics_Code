# 正确的定义方式
def test_func_v1(a, b, c=1, d=2): 
    return a + b + c + d

# 错误的定义方式
# def test_func_v2(a, b=1, c): 
#     return a + b + c