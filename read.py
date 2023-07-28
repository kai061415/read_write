#讀取檔案
#檢查檔案是否存在
#讓使用者輸入
#印出所有紀錄
#寫入檔案
#strip() 除掉換行符號
#split(',') 使用,做分割

import os #operating system

products = []

#讀取檔案
def read_file(filename):
	with open(filename, 'r', encoding='utf-8') as f:  
		for line in f:
			if '體重, 體脂' in line:
				continue
			products.append(line.strip().split(','))	
	return products
	
#讓使用者輸入
def user_input(products):	
	while True:   
		name = input('請輸入體重: ')
		if name == 'q':
			break
		body = input('請輸入體脂: ')
		s = []
		s.append(name)
		s.append(body)
		products.append(s)
	return products

#印出所有紀錄
def print_products(new_products):
	for line in products:
		print('您的體重為:', line[0], '您的體脂為:', line[1])

#寫入檔案
def write_file(filename, new_products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('體重, 體脂\n')  #新增欄位
		for line in new_products:
			f.write(line[0] + ',' + line[1] + '\n')	

#程式進入點
def main():
	products = []
	filename = 'test.txt'
	if os.path.isfile(filename):   #檢查檔案是否存在
		print('找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案!')

	new_products = user_input(products)
	print_products(new_products)
	write_file('test.txt', new_products)	

main()	 # refactor 重構		