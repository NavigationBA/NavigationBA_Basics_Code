print("函数参数的默认值示例")

def show_welcome_message(name="某某"):
    print(f"欢迎，{name}！")

# 调用函数，传入参数
show_welcome_message("张三")
# 调用函数，不传入参数，使用默认值
show_welcome_message()