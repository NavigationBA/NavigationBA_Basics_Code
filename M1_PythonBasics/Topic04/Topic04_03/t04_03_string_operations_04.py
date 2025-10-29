print("判断型的方法：")

print("(1) 判断是否为字符串和数字：")
print("abc123".isalnum())
print("abc".isalnum())
print("123".isalnum())

print("(2) 判断是否为数字：")
print("123".isdecimal())
print("②".isdecimal())
print("一百".isdecimal())
print("123".isdigit())
print("②".isdigit())
print("一百".isdigit())
print("123".isnumeric())
print("②".isnumeric())
print("一百".isnumeric())

print("(3) 是否只包含空白字符：")
print("  \n \t".isspace())

print("(4) 是否只包含 ASCII：")
print("abc123,.?! \n\t".isascii())

print("(5) 判断格式：")
print("abc".islower())
print("abc123".islower())
print("Abc123".islower())

print("ABC".isupper())
print("ABC123".isupper())
print("Abc123".isupper())

print("Hello Python".istitle())
print("Hello Python!@#".istitle())
print("Hello python".istitle())

print("(6) 判断开头结尾")

print("Hello Python".startswith("H"))
print("Hello Python".startswith("He"))
print("Hello Python".startswith("Hello"))

print("Hello Python".endswith("on"))
print("Hello Python".endswith("hon"))
print("Hello Python".endswith("Python"))

print("Hello Python".startswith("he"))

print("Hello Python".startswith(("He", "Hel", "Ha")))
print("Hello Python".startswith(("Ha", "Hb", "Hc")))