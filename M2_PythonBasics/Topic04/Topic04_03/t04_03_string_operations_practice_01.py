phone_number = input("请输入你的手机号：")
phone_number_masked = phone_number[:3] + "****" + phone_number[-4:]
print("保护后的手机号：", phone_number_masked)