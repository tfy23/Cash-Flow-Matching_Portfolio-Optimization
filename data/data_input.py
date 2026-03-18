import csv

# 准备数据
data = [
    ['Bond_ID', 'Maturity', 'Coupon', 'Price'],
    ['Bond_1', 1, 5.0, 102],
    ['Bond_2', 2, 3.5, 99],
    ['Bond_3', 2, 5.0, 101],
    ['Bond_4', 3, 3.5, 98],
    ['Bond_5', 4, 4.0, 98],
    ['Bond_6', 5, 9.0, 104],
    ['Bond_7', 5, 6.0, 100],
    ['Bond_8', 6, 8.0, 101],
    ['Bond_9', 7, 9.0, 102],
    ['Bond_10', 8, 7.0, 94]
]

# 写入CSV文件
filename = 'bonds.csv'
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV文件 '{filename}' 已生成成功！")

# 验证：读取并显示文件内容
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
    print("\n文件内容预览：")
    print(content)

# 可选：以表格形式显示数据
print("\n数据表格形式：")
print("-" * 50)
print(f"{'Bond_ID':<10} {'Maturity':<10} {'Coupon':<10} {'Price':<10}")
print("-" * 50)
for row in data[1:]:  # 跳过表头
    print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10}")