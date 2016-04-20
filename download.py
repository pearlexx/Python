from urllib import request

apple = 'http://real-chart.finance.yahoo.com/table.csv?s=AAPL&d=3&e=18&f=2016&g=d&a=11&b=12&c=1980&ignore=.csv'

def download(csv_url):
	response = request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split('\\n')
	dest_url = r'apple.csv'
	fx = open(dest_url, 'w')
	for line in lines:
		fx.write(line + '\n')
	fx.close()
	
download(apple)
