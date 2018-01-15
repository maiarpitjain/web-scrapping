#This will not run on online IDE
import requests
from bs4 import BeautifulSoup
station = str(input("Enter station"))
URL = "https://www.cleartrip.com/trains/stations/"+station

r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')

g_data=soup.find_all("td")
train = []
train_name = []
train_no = []
arrival = []
departure = []

for i in range(2,len(g_data),11):
	train.append(g_data[i-2].text)
	arrival.append(g_data[i-1].text)
	departure.append(g_data[i].text)

for item in train:
	name, no= item.split(" (")	
	train_name.append(name)
	train_no.append(no[0:len(no)-1])
print("Train_No","Train Name","\t\t","Arrival Time","\t","Departure Time")	
for i in range(len(train)):
	print(train_no[i],"\t",train_name[i],"\t",arrival[i],"\t\t",departure[i])
