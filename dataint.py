
#read the input file

print("Calculating transistor counts...")

f=open('input.txt','r')
input=str(f.read())

#load the cell information from celldefs.lib

f=open('celldefs.txt','r')
celldefs=str(f.read())
celldefs=celldefs.replace('\n','')
celldefs=celldefs.split(',')

#array of the different cells in the library
cells = []

#corresponding array of transistor counts for each cell
transcounts = []

#number of each cell counted in the input file
cellcounts = []

#cell categorization
cellcats = []


i=1
while i<=len(celldefs)-3:
	cells.append(celldefs[i])
	transcounts.append(int(celldefs[i+1]))
	cellcats.append(celldefs[i+2])
	i=i+3

i=0
totalcells = 0
totaltrans = 0
while i<=len(cells)-1:
	cellcounts.append(input.count(cells[i]))
	totalcells = totalcells + cellcounts[i]
	totaltrans = totaltrans + cellcounts[i]*transcounts[i]
	i=i+1

#generate nice table elements with uniform width
i=0
display_cells = []
while i<=len(cells)-1:
	display_cells.append(cells[i])
	while len(display_cells[i])<=15:
		display_cells[i] = display_cells[i]+" "
	i=i+1

i=0
display_cellcats = []
while i<=len(cellcats)-1:
	display_cellcats.append(cellcats[i])
	while len(display_cellcats[i])<=20:
		display_cellcats[i] = display_cellcats[i]+" "
	i=i+1

i=0
display_transcounts = []
while i<=len(transcounts)-1:
	display_transcounts.append(str(transcounts[i]))
	while len(display_transcounts[i])<=12:
		display_transcounts[i] = display_transcounts[i]+" "
	i=i+1

i=0
display_cellcounts = []
while i<=len(cellcounts)-1:
	display_cellcounts.append(str(cellcounts[i]))
	while len(display_cellcounts[i])<=12:
		display_cellcounts[i] = display_cellcounts[i]+" "
	i=i+1

#print the results

print('RESULT TABLE A:')
print('====================================================================')
print('|Cell            | Cell category       | Trans/cell  | # In Design |')
i=0
while i<=len(cells)-1:
	if cellcounts[i] > 0:
		print('|'+display_cells[i]+'|'+display_cellcats[i]+'|'+display_transcounts[i]+'|'+display_cellcounts[i]+'|')
	i=i+1
print('====================================================================')
print(' TOTAL DESIGN CELL COUNT: '+str(totalcells))
print('====================================================================')
print(' TOTAL DESIGN TRANSISTOR COUNT: '+str(totaltrans))
print('====================================================================')

# make a second table, this time by category

# cell categorizations without duplicates
cellcatdefs = []

# cellcounts for cellcatdefs
cellcatcounts = []

# transistor counts for cellcatdefs
celltranscounts = []

i=0
while i<=len(cells)-1:
	j=0
	newcat = 1 #if this stays one, you have a new category of cell
	while j<=len(cellcatdefs)-1:
		if cellcats[i]==cellcatdefs[j]:
			celltranscounts[j]=celltranscounts[j]+cellcounts[i]*transcounts[i]
			cellcatcounts[j] = cellcatcounts[j]+cellcounts[i]
			newcat=0
		j=j+1
	if newcat == 1:
			cellcatdefs.append(cellcats[i])
			celltranscounts.append(cellcounts[i]*transcounts[i])
			cellcatcounts.append(cellcounts[i])
	i=i+1


#make nice uniform-width elements for table B

i=0
display_cellcatdefs = []
while i<=len(cellcatdefs)-1:
	display_cellcatdefs.append(cellcatdefs[i])
	while len(display_cellcatdefs[i])<=20:
		display_cellcatdefs[i] = display_cellcatdefs[i]+" "
	i=i+1

i=0
display_celltranscounts = []
while i<=len(cellcatdefs)-1:
	display_celltranscounts.append(str(celltranscounts[i]))
	while len(display_celltranscounts[i])<=18:
		display_celltranscounts[i] = display_celltranscounts[i]+" "
	i=i+1

i=0
display_cellcatcounts = []
while i<=len(cellcatdefs)-1:
	display_cellcatcounts.append(str(cellcatcounts[i]))
	while len(display_cellcatcounts[i])<=12:
		display_cellcatcounts[i] = display_cellcatcounts[i]+" "
	i=i+1


#print the second table

print(' ')
print(' ')
print(' ')
print(' ')

print('RESULT TABLE B:')
print('=========================================================')
print('| Cell category       | Cell number | Total transistors |')
i=0
while i<=len(cellcatdefs)-1:
	if celltranscounts[i] > 0:
		print('|'+display_cellcatdefs[i]+'|'+display_cellcatcounts[i]+'|'+display_celltranscounts[i]+'|')
	i=i+1
print('=========================================================')
print(' TOTAL DESIGN CELL COUNT: '+str(totalcells))
print('=========================================================')
print(' TOTAL DESIGN TRANSISTOR COUNT: '+str(totaltrans))
print('=========================================================')
