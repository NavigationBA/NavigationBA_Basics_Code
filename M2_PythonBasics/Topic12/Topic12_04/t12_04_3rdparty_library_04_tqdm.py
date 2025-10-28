# tqdm与joblib结合使用，显示并行计算进度条

from joblib import Parallel, delayed
from tqdm import tqdm
import time

data = range(1, 101)

def compute_square(x):
    time.sleep(1)  # 模拟耗时操作
    return x * x

data_squared = Parallel(n_jobs=-1)(delayed(compute_square)(num) for num in tqdm(data))
total = sum(data_squared)
print("平方和：", total)