# 使用joblib库进行并行计算平方和

from joblib import Parallel, delayed

data = [1, 2, 3, 4, 5]

def compute_square(x):
    return x * x

data_squared = Parallel(n_jobs=-1)(delayed(compute_square)(num) for num in data)

total = sum(data_squared)
print("平方和：", total)