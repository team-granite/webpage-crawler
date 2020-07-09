from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from django.core.files import File
from bs4 import BeautifulSoup
import requests
import datetime

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

homepage = 'https://opentreasury.gov.ng'
querystring_2018 = '/index.php/component/content/article/11-dpr/29-daily-payment-report-2?Itemid=101'
querystring_2019 = '/index.php/component/content/article/11-dpr/2759-daily-payment-report-fgn-2019?Itemid=101'
querystring_2020 = '/index.php/component/content/article/11-dpr/3015-2020-daily-payment?Itemid=101'
querystring_2018_monthly = "/index.php/component/content/article/15-sample/221-monthly-budget-performance-fgn-total?Itemid=101"
querystring_2019_monthly ="/index.php/component/content/article/54-2019/fgn-monthly/1212-fgn-monthly?Itemid=101"
querystring_2020_monthly = "/index.php/component/content/article/92-2020/3847-fgn-monthly?Itemid=101"

CRON_URL = "http://localhost:8000"
CRON_DEV_URL = 'https://fgn-web-crawler.herokuapp.com'
CRON_TIME = "09:00"

treasury2018 = "/index.php/component/content/article/10-daily-treasury-statement-fgn/26-daily-treasury-statement-fgn-9?Itemid=101"
treasury2019 = "/index.php/component/content/article/10-daily-treasury-statement-fgn/26-daily-treasury-statement-fgn-9?Itemid=101"
treasury2020 = "/index.php/component/content/article/10-daily-treasury-statement-fgn/26-daily-treasury-statement-fgn-9?Itemid=101"


# Download files for their performance reports 
@api_view(['GET'])
def year_download_2018(request):
	"""
	Download the excel files (.xlsx) of 2018
	:param request:
	:return: filename, download url
	"""
	# return JsonResponse([1],safe = False)
	response = HttpResponse(content_type = 'application/ms-excel')
	result = []
	url = f'{homepage + querystring_2018}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		soup = BeautifulSoup(r, 'lxml')
		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								file_name = table_data[0].text
								file_link = homepage + table_data[1].find('a')['href']
								result.append({file_name: file_link})

								# rename the file, save it's extension and download
								excel_file_name = file_name.replace('/', '_')
								excel_file_type = file_link.split('.')[-1]
								excel_file = excel_file_name + '.' + excel_file_type

								# print("Downloading...")
								with open('static/expense/2018/{}'.format(excel_file), 'wb+') as file:
									response = requests.get(file_link, verify=False)
									myfile = File(file)
									myfile.write(response.content)
									myfile.closed
									file.closed
							except:
								result.append({table_data[0].text: ""})
		print("The end")
		return JsonResponse([excel_file], safe =False)

@api_view(['GET'])
def year_download_2019(request):
	"""
	Download the excel files (.xlsx) of 2018
	:param request:
	:return: filename, download url
	"""
	# return JsonResponse([1],safe = False)
	response = HttpResponse(content_type = 'application/ms-excel')
	result = []
	url = f'{homepage + querystring_2019}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		soup = BeautifulSoup(r, 'lxml')
		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								file_name = table_data[0].text
								file_link = homepage + table_data[1].find('a')['href']
								result.append({file_name: file_link})

								# rename the file, save it's extension and download
								excel_file_name = file_name.replace('/', '_')
								excel_file_type = file_link.split('.')[-1]
								excel_file = excel_file_name + '.' + excel_file_type

								# print("Downloading...")
								with open('static/expense/2019/{}'.format(excel_file), 'wb+') as file:
									response = requests.get(file_link, verify=False)
									myfile = File(file)
									myfile.write(response.content)
									myfile.closed
									file.closed
							except:
								result.append({table_data[0].text: ""})
		print("The end")
		return JsonResponse([excel_file], safe =False)


@api_view(['GET'])
def year_download_2020(request):
	"""
	Download the excel files (.xlsx) of 2020
	:param request:
	:return: filename, download url
	"""
	# return JsonResponse([1],safe = False)
	response = HttpResponse(content_type = 'application/ms-excel')
	result = []
	url = f'{homepage + querystring_2020}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		soup = BeautifulSoup(r, 'lxml')
		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								file_name = table_data[0].text
								file_link = homepage + table_data[1].find('a')['href']
								result.append({file_name: file_link})

								# rename the file, save it's extension and download
								excel_file_name = file_name.replace('/', '_')
								excel_file_type = file_link.split('.')[-1]
								excel_file = excel_file_name + '.' + excel_file_type

								# print("Downloading...")
								with open('static/expense/2020/{}'.format(excel_file), 'wb+') as file:
									response = requests.get(file_link, verify=False)
									myfile = File(file)
									myfile.write(response.content)
									myfile.closed
									file.closed
							except:
								result.append({table_data[0].text: ""})
		print("The end")
		return JsonResponse([excel_file], safe =False)



# DOWNLOAD BUDGET

def year_2018_monthly_download(request):
	url = f'{homepage + querystring_2018_monthly}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		monthlyreport = {}

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								monthlyreport.update({table_data[0].text: homepage + table_data[2].find('a')['href']})
								file_name = table_data[0].text
								file_link = homepage + table_data[2].find('a')['href']
								monthlyreport.append({file_name: file_link})

								# rename the file, save it's extension and download
								excel_file_name = file_name.replace('/', '_')
								excel_file_type = file_link.split('.')[-1]
								excel_file = excel_file_name + '.' + excel_file_type

								# print("Downloading...")
								with open('static/budget/2018/{}'.format(excel_file), 'wb+') as file:
									response = requests.get(file_link, verify=False)
									myfile = File(file)
									myfile.write(response.content)
									myfile.closed
									file.closed
							except:
								monthlyreport.update({table_data[0].text: ""})
						
		return JsonResponse([monthlyreport], safe =False)



def year_2019_monthly_download(request):
	url = f'{homepage + querystring_2019_monthly}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		monthlyreport = {}

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								file_name = table_data[0].text
								file_link = homepage + table_data[2].find('a')['href']
								monthlyreport.update({file_name: file_link})

								# rename the file, save it's extension and download
								excel_file_name = file_name.replace('/', '_')
								excel_file_type = file_link.split('.')[-1]
								excel_file = excel_file_name + '.' + excel_file_type

								# print("Downloading...")
								with open('static/budget/2019/{}'.format(excel_file), 'wb+') as file:
									response = requests.get(file_link, verify=False)
									myfile = File(file)
									myfile.write(response.content)
									myfile.closed
									file.closed
							except:
								monthlyreport.update({table_data[0].text: ""})
						
		return JsonResponse([monthlyreport], safe =False)


def year_2020_monthly_download(request):
	url = f'{homepage + querystring_2020_monthly}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		monthlyreport = {}

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								file_name = table_data[0].text
								file_link = homepage + table_data[2].find('a')['href']
								monthlyreport.update({file_name: file_link})

								# rename the file, save it's extension and download
								excel_file_name = file_name.replace(' Monthly Budget Performance', '_2020').lower()
								excel_file_type = file_link.split('.')[-1]
								excel_file = excel_file_name + '.' + excel_file_type

								# print("Downloading...")
								with open('static/budget/2020/{}'.format(excel_file), 'wb+') as file:
									response = requests.get(file_link, verify=False)
									myfile = File(file)
									myfile.write(response.content)
									myfile.closed
									file.closed
							except:
								monthlyreport.update({table_data[0].text: ""})
						
		return JsonResponse([monthlyreport], safe =False)


@api_view(['GET'])
def year_2018(request):
	url = f'{homepage + querystring_2018}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result = {table_data[0].text: homepage + table_data[1].find('a')['href']}
							except:
								result = {table_data[0].text: ""}
		return Response([result])
	

@api_view(['GET'])
def year_2019(request):
	url = f'{homepage + querystring_2019}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result = {table_data[0].text: homepage + table_data[1].find('a')['href']}
							except:
								result = {table_data[0].text: ""}
		return Response([result])


@api_view(['GET'])
def year_2020(request):
	url = f'{homepage + querystring_2020}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result = {table_data[0].text: homepage + table_data[1].find('a')['href']}
							except:
								result = {table_data[0].text: ""}
		return Response([result])


@api_view(['GET'])
def year_2018_momthly(request):
	url = f'{homepage + querystring_2018_monthly}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		monthlyreport = {}

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								monthlyreport.update({table_data[0].text: homepage + table_data[2].find('a')['href']})
							except:
								result = {table_data[0].text: ""}
		return Response([monthlyreport])


@api_view(['GET'])
def year_2019_momthly(request):
	url = f'{homepage + querystring_2019_monthly}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		monthlyreport = {}

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								monthlyreport.update({table_data[0].text: homepage + table_data[2].find('a')['href']})
							except:
								result = {table_data[0].text: ""}
		return Response([monthlyreport])


@api_view(['GET'])
def year_2020_momthly(request):
	url = f'{homepage + querystring_2020_monthly}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		monthlyreport = {}

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								monthlyreport.update({table_data[0].text: homepage + table_data[2].find('a')['href']})
							except:
								result = {table_data[0].text: ""}
		return Response([monthlyreport])

@api_view(['GET'])
def daily_report(request, year, month, date):
	
	"""
	Daily report view
	:param request: Year, Month, Date
	:return: the download link for the particular day
	"""

	try:
		if int(year) == 2018:
			url = f'{homepage + querystring_2018}'
		if int(year) == 2019:
			url = f'{homepage + querystring_2019}'
		if int(year) == 2020:
			url = f'{homepage + querystring_2020}'
		
		if request.method == 'GET':
			r = requests.get(url, verify=False).text
			soup = BeautifulSoup(r, 'lxml')
			for section in soup.find('section', attrs={'class': 'sppb-section'}):
				for div in section.find_all('div', attrs={'class': 'sppb-panel'})[int(month) - 1]:
					table = div.find_all('table')
					
					for table_rows in table:
						for tr in table_rows.find_all("tr")[int(date) : int(date)+1]:
							table_data = tr.find_all('td')
							for i in table_data:
								if i != None:
									try:
										result = {table_data[0].text: homepage + table_data[1].find('a')['href']}
									except:
										result = {table_data[0].text: ""}
			return Response([result])
		
	except:
		return Response("Invalid date")


# Run Cron Jobs
def cronjob(request):
	import schedule
	import time 
	import json 

	x = datetime.datetime.now()

	year =  str(x.year)
	month  = str(x.month)
	if len(month) == 1:
		month = "0"+ str(x.month)
	day = x.day
	if len(year) == 1:
		day = "0" + str(x.day)


	schedule.every().day.at(CRON_TIME).do(job)
	# schedule.every(10).seconds.do(job)
	while True:
		schedule.run_pending()
		time.sleep(1)
		link = requests.get(CRON_DEV_URL+'/v1/dailyreportjson/{}/{}/{}/'.format(year,month, day)).json()
		return JsonResponse([link], safe = False)



def job():
	import json 
	x = datetime.datetime.now()

	year =  str(x.year)
	month  = str(x.month)
	if len(month) == 1:
		month = "0"+ str(x.month)
	day = x.day
	if len(year) == 1:
		day = "0" + str(x.day)

	link = requests.get(CRON_URL+'/v1/dailyreportjson/{}/{}/{}/'.format(year,month, day)).json()
	return JsonResponse([link], safe=False)


def daily_report_json(request, year, month, date):
	
	"""
	Daily report Json
	:param request: Year, Month, Date
	:return: the download link for the particular day
	"""

	try:
		if int(year) == 2018:
			url = f'{homepage + querystring_2018}'
		if int(year) == 2019:
			url = f'{homepage + querystring_2019}'
		if int(year) == 2020:
			url = f'{homepage + querystring_2020}'
		
		if request.method == 'GET':
			r = requests.get(url, verify=False).text
			soup = BeautifulSoup(r, 'lxml')
			for section in soup.find('section', attrs={'class': 'sppb-section'}):
				for div in section.find_all('div', attrs={'class': 'sppb-panel'})[int(month) - 1]:
					table = div.find_all('table')
					
					for table_rows in table:
						for tr in table_rows.find_all("tr")[int(date) : int(date)+1]:
							table_data = tr.find_all('td')
							for i in table_data:
								if i != None:
									try:
										result = {table_data[0].text: homepage + table_data[1].find('a')['href']}
									except:
										result = {table_data[0].text: ""}
			return JsonResponse([result], safe=False)
		
	except:
		return JsonResponse("Invalid date", safe=False)



@api_view(['GET'])
def get_months(request, year, category):

		"""
		Monthlyly Report View
		:param request: Year, Category(1-Administrative, 2-Budget, 3-Function)
		:return: the download link for the month based on the selected category 
		"""

		if int(year) == 2018:
			url = f'{homepage + querystring_2018_monthly}'
		elif int(year) == 2019:
			url = f'{homepage + querystring_2019_monthly}'
		elif int(year) == 2020:
			url = f'{homepage + querystring_2020_monthly}'
		else:
			return("Invalid Request")

		r = requests.get(url, verify=False).text
		month_dict = {"Admin":{}, "Eco":{}, "Func":{}}

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')

		table_rows = table[0].find_all('tr')
		for td in table_rows:
			table_data = td.find_all('td')
			for i in table_data:
							if i != None:
								try:
									month_dict["Admin"].update({(table_data[0].text).split(" ")[0]: homepage + table_data[2].find('a')['href']})
								except:
									continue


		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')

		table_rows = table[1].find_all('tr')
		for td in table_rows:
			table_data = td.find_all('td')
			for i in table_data:
							if i != None:
								try:
									month_dict["Eco"].update({(table_data[0].text).split(" ")[0]: homepage + table_data[2].find('a')['href']})
								except:
									continue


		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')

		table_rows = table[2].find_all('tr')
		for td in table_rows:
			table_data = td.find_all('td')
			for i in table_data:
							if i != None:
								try:
									month_dict["Func"].update({(table_data[0].text).split(" ")[0]: homepage + table_data[2].find('a')['href']})
								except:
									continue

		if int(category) == 1:
			return JsonResponse(month_dict["Admin"])
		elif int(category) == 2:
			return JsonResponse(month_dict["Eco"])
		elif int(category) == 3:
			return JsonResponse(month_dict["Func"])
								

@api_view(['GET'])
def treasury_2018(request):
	
	"""
	Yearly Report View
	:param request: Year, Month, Date
	:return: the download link for the particular day
	"""

	result = {}
	url = f'{homepage + treasury2018}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs = {'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result.update({table_data[0].text : homepage + table_data[1].find('a')['href']})
							except:
								result.update({table_data[0].text : " "})
	return Response([result])

		
@api_view(['GET'])
def treasury_2019(request):
	
	result = {}
	url = f'{homepage + treasury2019}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs = {'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result.update({table_data[0].text : homepage + table_data[1].find('a')['href']})
							except:
								result.update({table_data[0].text : " "})
	return Response([result])

		
@api_view(['GET'])
def treasury_2020(request):
	
	"""
	Yearly Report View
	:param request: Year, Month, Date
	:return: the download link for the particular day
	"""

	result = {}
	url = f'{homepage + treasury2020}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text
		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs = {'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result.update({table_data[0].text : homepage + table_data[1].find('a')['href']})
							except:
								result.update({table_data[0].text : " "})
	return Response([result])

@api_view(['GET'])
def daily_treasury_report(request, year, month, date):
	
	"""
	Daily Treasury view
	:param request: Year, Month, Date
	:return: the download link for the particular day
	"""

	try:
		if int(year) == 2018:
			url = f'{homepage + treasury2018}'
		if int(year) == 2019:
			url = f'{homepage + treasury2020}'
		if int(year) == 2020:
			url = f'{homepage + treasury2020}'
		
		if request.method == 'GET':
			r = requests.get(url, verify=False).text
			soup = BeautifulSoup(r, 'lxml')
			for section in soup.find('section', attrs={'class': 'sppb-section'}):
				for div in section.find_all('div', attrs={'class': 'sppb-panel'})[int(month) - 1]:
					table = div.find_all('table')
					
					for table_rows in table:
						for tr in table_rows.find_all("tr")[int(date) : int(date)+1]:
							table_data = tr.find_all('td')
							for i in table_data:
								if i != None:
									try:
										result = {table_data[0].text: homepage + table_data[1].find('a')['href']}
									except:
										result = {table_data[0].text: ""}
			return Response([result])
		
	except:
		return Response("Invalid date")


@api_view(['GET'])
def get_months(request, year):

		if int(year) == 2018:
			url = f'{homepage + querystring_2018_monthly}'
		elif int(year) == 2019:
			url = f'{homepage + querystring_2019_monthly}'
		elif int(year) == 2020:
			url = f'{homepage + querystring_2020_monthly}'


		r = requests.get(url, verify=False).text
		month_dict = {"Admin":{}, "Eco":{}, "Func":{}}

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')

		table_rows = table[0].find_all('tr')
		for td in table_rows:
			table_data = td.find_all('td')
			for i in table_data:
							if i != None:
								try:
									# month_dict["Admin"].update({(table_data[0].text).split(" ")[0]: homepage + table_data[1].find('a')['href']})
									file_name = (table_data[0].text).split(" ")[0]
									file_link = homepage + table_data[2].find('a')['href']
									month_dict["Admin"].update({file_name: file_link})

									# rename the file, save it's extension and download
									excel_file_name = file_name.replace(' Monthly Budget Performance', '_2020').lower()
									excel_file_type = file_link.split('.')[-1]
									excel_file = excel_file_name + '.' + excel_file_type

									# print("Downloading...")
									with open('static/budget/{}/administrative/{}'.format(year,excel_file), 'wb+') as file:
										response = requests.get(file_link, verify=False)
										myfile = File(file)
										myfile.write(response.content)
										myfile.closed
										file.closed
										
								except:
									continue


		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')

		table_rows = table[1].find_all('tr')
		for td in table_rows:
			table_data = td.find_all('td')
			for i in table_data:
							if i != None:
								try:
									# month_dict["Eco"].update({(table_data[0].text).split(" ")[0]: homepage + table_data[2].find('a')['href']})
									file_name = (table_data[0].text).split(" ")[0]
									file_link = homepage + table_data[2].find('a')['href']
									month_dict["Eco"].update({file_name: file_link})

									# rename the file, save it's extension and download
									excel_file_name = file_name.replace(' Monthly Budget Performance', '_2020').lower()
									excel_file_type = file_link.split('.')[-1]
									excel_file = excel_file_name + '.' + excel_file_type

									# print("Downloading...")
									with open('static/budget/{}/economic/{}'.format(year,excel_file), 'wb+') as file:
										response = requests.get(file_link, verify=False)
										myfile = File(file)
										myfile.write(response.content)
										myfile.closed
										file.closed
								except:
									continue


		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')

		table_rows = table[2].find_all('tr')
		for td in table_rows:
			table_data = td.find_all('td')
			for i in table_data:
							if i != None:
								try:
									# month_dict["Func"].update({(table_data[0].text).split(" ")[0]: homepage + table_data[1].find('a')['href']})
									file_name = (table_data[0].text).split(" ")[0]
									file_link = homepage + table_data[2].find('a')['href'] 
									month_dict["Func"].update({file_name: file_link})

									# rename the file, save it's extension and download
									excel_file_name = file_name.replace(' Monthly Budget Performance', '_2020').lower()
									excel_file_type = file_link.split('.')[-1]
									excel_file = excel_file_name + '.' + excel_file_type

									# print("Downloading...")
									with open('static/budget/{}/govt_functions/{}'.format(year,excel_file), 'wb+') as file:
										response = requests.get(file_link, verify=False)
										myfile = File(file)
										myfile.write(response.content)
										myfile.closed
										file.closed
								except:
									continue
		print(month_dict['Admin'])
		return JsonResponse(month_dict) 