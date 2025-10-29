is_has_ticket = input("请问您有票吗？(是/否)：")
is_has_danger_item = input("请问您有违禁品吗？(是/否)：")
gender = input("请输入您的性别：(男/女)：")

if is_has_ticket == "是":
    if is_has_danger_item == "是":
        print("违禁品不能带上飞机，请处理后再来")
    else:
        if gender == "男":
            print("先生您好，祝您旅途愉快～")
        else:
            print("女士您好，祝您旅途愉快～")
else:
    print("请先去买票～")