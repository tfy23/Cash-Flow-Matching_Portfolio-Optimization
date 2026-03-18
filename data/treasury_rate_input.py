import csv

# 准备数据 - 期限和对应的收益率
#数据更新日期：202603017
#数据来源：https://yield.chinabond.com.cn/cbweb-czb-web/czb/moreInfo?locale=cn_ZH&nameType=1
data = [
    ['Year', 'Rate'],  # 表头
    [0.25, 1.23],      # 3个月 = 0.25年
    [0.5, 1.24],       # 6个月 = 0.5年
    [1, 1.27],         # 1年
    [2, 1.34],         # 2年
    [3, 1.36],         # 3年
    [5, 1.58],         # 5年
    [7, 1.71],         # 7年
    [10, 1.83],        # 10年
    [30, 2.38]         # 30年
]

# 写入CSV文件
filename = 'treasury_rates.csv'
with open(filename, 'w', newline='', encoding='utf-8-sig') as file:  # 使用utf-8-sig编码，方便Excel打开
    writer = csv.writer(file)
    writer.writerows(data)

print(f"✅ CSV文件 '{filename}' 已生成成功！")
print(f"📊 共生成 {len(data)-1} 条国债收益率数据记录\n")

# 显示数据预览
print("数据预览：")
print("-" * 30)
print(f"{'Year':<6} {'Rate (%)':<10}")
print("-" * 30)
for row in data[1:]:
    year_str = f"{row[0]}年" if row[0] >= 1 else f"{int(row[0]*12)}个月"
    print(f"{row[0]:<6} {row[1]:<10} ({year_str})")