import csv
import locale
from datetime import datetime

def readCsv(filename):
	container = []
	with open(filename) as file:
		reader = csv.reader(file)
		for row in reader:
			container.append(row)
	return container

def stringToDate(csvList, index):
	for row in csvList:
		if len(row) > index:
			row[index] = datetime.strptime(row[index], "%Y-%m-%d")

def dateToString(date):
	locale.setlocale(locale.LC_TIME, "es_PE.utf8")
	return date.strftime(", %B %Y")

# 105 Control_R
