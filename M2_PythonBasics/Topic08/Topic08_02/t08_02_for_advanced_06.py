print("嵌套推导式")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [num for row in matrix for num in row]
print(flattened)

print("嵌套推导式等价的循环写法")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
print(flattened)