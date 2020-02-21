import csv
import numpy as np
import matplotlib.pyplot as plt

arr=[]
with open("GC_DATA.csv") as csvfile:
	reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) 
	# change contents to floats
	try:
		for row in reader:
			continue
	except:
		nothing=1 #placeholder, just for t/e 
	
	for row in reader:
		if(row[2]<50.0):
			arr.append(row)
l=[];r=[]
for i in arr:
	l.append(i[0])
	r.append(i[2])
#print(arr)
fig=plt.figure()
ax=fig.add_subplot(111,projection='polar')
c=ax.scatter(l,r)
#plt.polar(arr[0],arr[2])
plt.show()

plt.hist(l)
plt.show()
