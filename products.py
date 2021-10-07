# 載入作業系統(operating system)模組
import os

# 讀取檔案
products = []
if os.path.isfile('products.csv'): # 檢查檔案在不在
	print('繼續輸入')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 進入下一個迴圈
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('還沒有歷史紀錄')

# 執行碼
while True:
	name = input('請輸入商品名稱: ')
	if name == 'Q' or 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

# 購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n')