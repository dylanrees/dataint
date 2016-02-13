
#read the input file

print("It's numerical calculus time!!!!!!")

print(" ")

print("Reading input file...")

f=open('input.txt','r')
rawdata=str(f.read())

print ("Data loaded.")

print(" ")

print ("Determining data channels...")

#load the data channels

rawdata=rawdata.split('\n')

dchannels=rawdata[0].split('	')
print(str(len(dchannels))+" channels detected:")

i=0

while i<=len(dchannels)-1:
	print("     "+dchannels[i])
	i=i+1

#sort the data
#data will be sorted into a 2d grid. 
#convention:
#first indexing number is channel
#second indexing number is data point
print(" ")
print("Sorting and converting data...")

#initialize the data array
i=0
data = []
while i<=len(dchannels)-1:
	data.append(0)
	data[i]=[]
	j=0
	while j<=len(rawdata)-1:
		data[i].append(0)
		j=j+1
	i=i+1

#populate the data array

i=1
j=0

while i<=len(rawdata)-2:
	stage=rawdata[i].split('	')
	j=0
	while j<=len(dchannels)-1:
		data[j][i-1]=stage[j]
		j=j+1

	i=i+1

#convert data strings to numbers


j=0

while j<=len(dchannels)-1:
	i=0
	while i<=len(data[0])-3:
		broken = data[j][i].split('e')
		broken = float(broken[0])*pow(10,int(broken[1]))
		data[j][i]=broken
		i=i+1
	j=j+1

print("Data ready.")

#do the calculation

i=1
j=1
while j<=len(dchannels)-1:
	area = 0
	i=1
	while i<len(data[0])-2:
		area = area + (data[0][i]-data[0][i-1])*(data[j][i]+data[j][i-1])/2
		i=i+1
	print("Total area under channel "+dchannels[j]+": ")
	print(str(area)+" second-volts")
	j=j+1

