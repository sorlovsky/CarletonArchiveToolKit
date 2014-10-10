#Simon Orlovsky
#10/9/14
#Carleton Archives

#content data set
import csv
file = open("content.csv")

contentFields = []
for line in file:
    fields = line.split(',')
    print fields
    contentFields.append(fields[1])

#print contentFields[0][1]

#digital records data set
file = open("digitalContent.csv")       

digitalFields = []
for line in file:
    fields = line.split(',')
    digitalFields.append(fields[3]);
file.close()

# print len(digitalFields)
# print len(contentFields)

print contentFields[0][0]


correctList = []
for i in range(len(digitalFields)):
    for j in range(len(contentFields)):
        if digitalFields[i]== contentFields[j]:
            correctList.append(digitalFields[i])

# #print correctList

# incorrectList = []
# for i in range(len(digitalFields)):
#     if digitalFields[i] not in correctList:
#         incorrectList.append(digitalFields[i])

# #print incorrectList

