age = 20
gender = "男"
is_vip = True

if age >= 18:
    if gender == "男":
        if is_vip:
            print("尊贵的VIP先生您好，欢迎光临本网吧～")
        else:
            print("先生您好，欢迎光临本网吧～")
    else:
        if is_vip:
            print("尊贵的VIP女士您好，欢迎光临本网吧～")
        else:
            print("女士您好，欢迎光临本网吧～")
else:
    print("小朋友，你还不能进网吧哦～")