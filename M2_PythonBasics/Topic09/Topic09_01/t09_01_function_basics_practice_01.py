# 定义函数
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

# 调用函数
weight = 70
height = 1.75
bmi_value = calculate_bmi(weight, height)
print(f"一个体重为 {weight} 公斤，身高为 {height} 米的人，BMI 指数是: {round(bmi_value, 2)}")