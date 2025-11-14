from config import PATH_PREFIX

def display_menu():

    # 延迟导入以避免循环引用
    from functions import function_info

    # 1. 读取与显示标题
    with open(f"{PATH_PREFIX}data/title.txt", "r", encoding="utf-8") as f:
        title = f.read()
    print(title)

    # 2. 动态生成功能菜单
    for key, value in function_info.items():
        print(f"{key}. {value['description']}")
    
    # 3. 显示退出选项
    print("q. 退出")

def show_instructions(function_key="0"):
    
    # 延迟导入以避免循环引用
    from functions import function_info
    
    # 读取对应功能的说明文件
    instruction_file = function_info[function_key]["instruction_file"]

    with open(f"{PATH_PREFIX}{instruction_file}", "r", encoding="utf-8") as f:
        instructions = f.read()
    
    # 显示说明内容    
    print(instructions)

    # 提示按任意键继续
    input("输入任意内容返回上级菜单：")


if __name__ == "__main__":
    # display_menu()
    show_instructions("0")
    show_instructions("1")
    show_instructions("2")
    show_instructions("3")