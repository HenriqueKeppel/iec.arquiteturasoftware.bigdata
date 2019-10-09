import mincemeat
import glob
import csv

text_files = glob.glob('C:\\Users\\416459\\exerc\\textos\\*')

def file_contents(file_name):
	f = open(file_name)
	try:
		return f.read()
	finally:
		f.close()
		
source = dict((file_name, file_contents(file_name))for file_name in text_files)

def mapfn(k, v):
	print 'map ' + k
	from stopwords import allStopWords
	for line in v.splitlines():
		for word in line.split():
			if (word in allStopWords):
				yield word, 1
				
def reducefn(k, v):
	print 'reduce ' + k
	return sum(v)
	
s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open("C:\\Users\\416459\\exerc\\RESULT.csv", "w"))
for k, v in results.items():
	w.writerow([k, v])