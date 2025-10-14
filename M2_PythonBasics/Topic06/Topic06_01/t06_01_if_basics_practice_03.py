import random

cpu = random.choice(["石头", "剪刀", "布"])
usr = input("请输入您的出拳（石头/剪刀/布）：")

if usr == cpu:
    print("平局！")
elif (usr == "石头" and cpu == "剪刀") or (usr == "剪刀" and cpu == "布") or (usr == "布" and cpu == "石头"):
    print("恭喜你，你获胜了")
else:
    print("很遗憾，你失败了")
