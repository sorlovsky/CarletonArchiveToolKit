""" 
	carletonianMkDirs.py
	Using date, create new directories for each Carletonian issue.

	TO USE: update filepath with the correct directory containing the images

	1. create directories from file names
	2. move all matching files into their correct directories

"""

import os
import sys
import shutil

def main():
	filepath = "/Users/simonorlovsky/code/carleton_archive/directory_maker/newsreleasesorting"
	extensions = [".jpg",".jp2",".tif"]

	fList = []
	# creates a list of all files in the filepath directory
	for file in os.listdir(filepath):
		print file
		for ext in extensions:
			# file extensions are case-sensitive!
			if file.lower().endswith(ext):
				fList.append(file)
	for f in fList:
		# makes a directory given the file's name
		if not os.path.exists(os.path.join(filepath + str(f)[:14])):
			os.mkdir(filepath + f[:14])
		else:
			# print 'Cannot make directory: already exists "' + f + '"'
			pass

	# moves each file into the correct folder
	for f in fList:
		source = filepath + f
		destination = filepath + f[:14]	
		shutil.move(source,destination)

main()