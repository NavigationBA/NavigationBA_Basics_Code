# 使用tqdm库显示进度条

from tqdm import tqdm
import time

for i in tqdm(range(100)):
    # 模拟一些耗时操作
    time.sleep(0.1)