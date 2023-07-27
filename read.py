#讀取檔案
#檢查檔案是否存在
#讓使用者輸入
#印出所有紀錄
#寫入檔案
#strip() 除掉換行符號
#split(',') 使用,做分割

import os #operating system

products = []
if os.path.isfile('test.txt'):
	print('找到檔案了!')
	with open('test.txt', 'r', encoding='utf-8') as f:  #讀取檔案
		for line in f:
			if '體重, 體脂' in line:
				continue
			s = line.strip().split(',')
			products.append(s)
else:
	print('找不到檔案!')	

#讓使用者輸入
while True:   
	name = input('請輸入體重: ')
	if name == 'q':
		break
	body = input('請輸入體脂: ')
	s = []
	s.append(name)
	s.append(body)
	products.append(s)
print(products)

#印出所有紀錄
for line in products:
	print('您的體重為:', line[0], '您的體脂為:', line[1])


#寫入檔案
with open('test.txt', 'w', encoding='utf-8') as f:
	f.write('體重, 體脂\n')  #新增欄位
	for line in products:
		f.write(line[0] + ',' + line[1] + '\n')	