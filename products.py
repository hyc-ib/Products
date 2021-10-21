# 載入作業系統(operating system)模組
import os

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 進入下一個迴圈
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 執行碼
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'Q' and 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

# 購買紀錄
def print_products(products):
    for product in products:
        print(product[0], '的價格是', product[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for product in products:
            f.write(product[0] + ',' + str(product[1]) + '\n')

# main function
def main():
    products = [] # 如果沒有找到檔案也有製造清單
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案在不在
        print('繼續輸入')
        products = read_file(filename)
    else:
        print('還沒有歷史紀錄')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)


main()