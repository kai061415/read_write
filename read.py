#讀取檔案
#檢查檔案是否存在
#讓使用者輸入
#印出所有紀錄
#寫入檔案
#strip() 除掉換行符號
#split(',') 使用,做分割

products = []

#讀取檔案
with open('test.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '體重,體脂' in line:
			continue
		s = line.strip().split(',')
		products.append(s)

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
with open('test.csv', 'w', encoding='utf-8') as f:
	f.write('體重, 體脂\n')  #新增欄位
	for line in products:
		f.write(line[0] + ',' + line[1] + '\n')	