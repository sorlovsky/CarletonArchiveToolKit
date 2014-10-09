#Simon Orlovsky
#10/9/14
#Carleton Archives

#content data set
file = open("tblCollections_Content.txt")

count=0
contentFields = []
for line in file:
    fields = line.split(',')
    contentFields.append(fields)
    count+=1

print "There were", count, "files in content"
print contentFields[0][0]

#digital records data set
file = open("tblDigitalLibrary_DigitalContent.txt")       

digitalFields = []
count=0
for line in file:
    fields = line.split(',')
    digitalFields.append(fields);
    count+=1
file.close()

print "There were", count, "files in digital content"

