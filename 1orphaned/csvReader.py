import csv
digitalContent = []

#reading digital content
with open('digitalContent.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        #print row[3]
        digitalContent.append(row)
content = []

#reading content
with open('content.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	if (len(row)!=1):
    		#print row[1]
    		content.append(row)

#getting correct answers
wrong = digitalContent[:];
for i in range(len(digitalContent)):
	for j in range(len(content)):
		if (digitalContent[i][4]== content[j][0]):
			correct= digitalContent[i]
			wrong.remove(correct)
			break
			

print "Number of digital records", len(digitalContent)

#figuring out orphaned
# wrong = []
# for i in range(len(digitalContent)):
# 	isSame = False
# 	for j in range(len(correct)):
# 		if (digitalContent[i][3]== correct[j][3]):
# 			isSame = True
# 	if isSame == False:
# 		wrong.append(digitalContent[i])

print "Number of orphaned records", len(wrong)

# wrongCollectionIDonly = []
# for i in range(len(wrong)):
# 	for j in range(len(content)):
# 		if (wrong[i][3]== content[j][1]):
# 			wrongCollectionIDonly.append(wrong[i])
# 			break

# print "Number of matching collection IDs but incorrect collection content id to ID", len(wrongCollectionIDonly)



orphaned = []

for i in range(len(wrong)):
	print wrong[i][3], wrong[i][4]
	if wrong[i][3]!= '0':
		orphaned.append(wrong[i])
print "Number of orphaned is ",len(orphaned)


with open('orphaned.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(orphaned)