from functions import function_info

def get_user_input():
    while True:
        user_input = input("请输入你的选择: ")
        if user_input in function_info.keys() or user_input == 'q':
            break
        else:
            print("输入有误，请重新输入")
    return user_input

if __name__ == "__main__":
    get_user_input()