print("拆分合并型的方法")

print("a b c".split())
print("a,b,c".split(","))
print("a,b,c".split(",", 1))

print("a b c".rsplit())
print("a,b,c".rsplit(","))
print("a,b,c".rsplit(",", 1))

s = """
line1
line2
line3
"""
print(s.splitlines())

print("a-b-c".partition("-"))
print("a-b-c".rpartition("-"))

print("".join(["a", "b", "c"]))
print("-".join(["a", "b", "c"]))