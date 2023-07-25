#讀取檔案
#檢查檔案是否存在
#讓使用者輸入
#印出所有紀錄
#寫入檔案
#strip() 除掉換行符號
#split(',') 使用,做分割

products = []

while True:   #讓使用者輸入
	name = input('請輸入體重: ')
	if name == 'q':
		break
	body = input('請輸入體脂: ')
	s = []
	s.append(name)
	s.append(body)
	products.append(s)
print(products)	


