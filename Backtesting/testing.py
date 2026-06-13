import pandas as pd
import pandas_ta as ta
import numpy as np

# 1. 将原始数据转换为 pandas Series，这是量化分析的基石
close_series = pd.Series([10.0, 11.0, 12.0, 15.0, 14.0, 13.0, 16.0, 17.0, 19.0, 17.0])

# 2. 使用 pandas-ta 计算简单移动平均线 (SMA)
# pandas-ta 的好处是它的结果直接是一个 Series，方便后续回测或绘图
ma_ta = close_series.ta.sma(length=5)

# 3. 对比你原来的手动实现
def my_MA(arr, period): 
    out = [] 
    for i in range(0,len(arr)): 
        tmp = arr[max(0,i+1-period):i+1] 
        if len(tmp)<period: 
            out.append(None) 
        else: 
            value = sum(tmp)/period 
            out.append(value) 
    return out 

ma1 = my_MA(close_series.tolist(), 5)

print("手动实现的 MA:", ma1)
print("pandas-ta 实现的 SMA:\n", ma_ta.to_list())