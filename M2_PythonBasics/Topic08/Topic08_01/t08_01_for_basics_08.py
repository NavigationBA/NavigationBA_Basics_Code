print("for循环嵌套")

for i in range(3):  
    print(f"外圈第{i+1}圈开始")
    for j in range(2): 
        print(f"  内圈第{j+1}圈")
    print(f"外圈第{i+1}圈结束")