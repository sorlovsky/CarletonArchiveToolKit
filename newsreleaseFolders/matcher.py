import os, sys

# Open a file
path = "/Users/simonorlovsky/code/carleton_archive/newsreleaseFolders/directories"
dirs = os.listdir( path )


#adding all directories to list
directories = {}

for dir in dirs:
	if dir[0]!=".":
		directories[dir] = ''


# for i in range(len(directories)):
# 	newpath = "/Users/simonorlovsky/code/carleton_archive/newsreleaseFolders/directories/"+directories[i]
# 	files = os.listdir( path )
# 	print files

for i, v in enumerate(directories):
	newpath = "/Users/simonorlovsky/code/carleton_archive/newsreleaseFolders/directories/"+v
	files = os.listdir( newpath )

	#Check to make sure this directory isn't empy
	if files == []:
		print v, "is empty"
	directories[v] = files
	print i, v
	print "Files:", directories[v]
	print ""

for i, v in enumerate(directories):
    os.mkdir(v)
    src = "/Users/simonorlovsky/code/carleton_archive/newsreleaseFolders/directories/"
    dst = "/Users/simonorlovsky/code/carleton_archive/newsreleaseFolders/directories/"+v
    shutil.move(src, dst)



