#Simon Orlovsky
#10/9/14
#Carleton Archives

#content data set
file = open("tblCollections_Content.txt")

contentFields = []
for line in file:
    fields = line.split(',')
    contentFields.append(fields)

#digital records data set
file = open("tblDigitalLibrary_DigitalContent.txt")       

digitalFields = []
for line in file:
    fields = line.split(',')
    digitalFields.append(fields);
file.close()

correctList = []
for i in range(len(digitalFields)):
    for j in range(len(contentFields)):
        if digitalFields[i][0] == contentFields[j][0]:
            correctList.append(digitalFields[i])
            break

print correctList

# for i in range(len(digitalFields)):
#     for j in range(len(correctList)):

