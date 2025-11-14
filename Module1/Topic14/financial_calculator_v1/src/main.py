from input_handler import get_user_input
from ui import display_menu
from functions import function_info

def main():

    while True:
        
        # 显示菜单
        display_menu()
        print("-" * 40)
        # 获取用户输入
        user_input = get_user_input()

        # 处理用户输入
        if user_input == 'q':
            print("-" * 40)
            print("感谢使用，程序已退出！")
            break
        else:
            print("-" * 40)
            function = function_info[user_input]["function"]
            function()

if __name__ == "__main__":
    main()