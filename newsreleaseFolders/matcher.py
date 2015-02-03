'''
matcher.py

Simon Orlovsky
February 2015
Carleton College Archives

This is a python script that will a directory filled with folders of pictures that are organized with a particular structure.
Our goal is to reproduce the file structure of this directory and replace the .jpgs with .tiffs that we have stored on our machine.

'''

import os, sys, shutil

# Open a file
path = "/Users/simonorlovsky/code/carleton_archive/newsreleaseFolders/directories"
dirs = os.listdir( path )


#adding all directories to list
directories = {}

for dir in dirs:
	if dir[0]!=".":
		directories[dir] = '' #the key is the directory name for now it is blank because we haven't put anything into it
	

for i, v in enumerate(directories):
	newpath = "/Users/simonorlovsky/code/carleton_archive/newsreleaseFolders/directories/"+v
	files = os.listdir( newpath )

	#Check to make sure this directory isn't empy
	if files == []:
		print v, "is empty"
	directories[v] = files
	print "Folder:", v
	print "Files:", directories[v]
	filesToCopyOver = directories[v]
	for i in range(len(filesToCopyOver)):
		filesToCopyOver[i]= filesToCopyOver[i][:-3]+"tiff"
	print "Files to move over", filesToCopyOver
	src = "/Users/simonorlovsky/code/carleton_archive/newsreleaseFolders/tiffs/"
	print "Source:", src
	dst = "/Users/simonorlovsky/code/carleton_archive/newsreleaseFolders/"+v
	print "Destination", dst
	print ""

	
	# os.mkdir(v)

	
	# shutil.move(src, dst)
	# print ""



