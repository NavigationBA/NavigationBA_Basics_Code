item = input("请输入商品名称：")
price = input("请输入商品价格：")
number = input("请输入商品数量：")

s = (item + number + "件 x " + price + "元" + " = " + str(float(number) * float(price)) + "元")

s_output = s.center(30, "-")

print(s_output)

