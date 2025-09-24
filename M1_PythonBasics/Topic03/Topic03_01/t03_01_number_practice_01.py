price_per_500g = float(input("请输入西瓜每斤单价（元）："))
weight = float(input("请输入西瓜重量（斤）："))

total_price = price_per_500g * weight

print("西瓜总价为：", total_price, "元")