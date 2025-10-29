cash_flows = [-2000, 1000, 1500, 2000, 2500, 3000]
r = 0.05

npv_list = []

for t in range(len(cash_flows)):
    cf_t = cash_flows[t]
    npv_t = cf_t / ((1 + r) ** t)
    npv_list.append(npv_t)

npv = sum(npv_list)
print(f"现金流的现值（NPV）为：{npv}")