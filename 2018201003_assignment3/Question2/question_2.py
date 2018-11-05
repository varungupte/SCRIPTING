import os
import re
import pathlib
import sys
from pathlib import Path
import linecache
import difflib
import string,fileinput

# ls command :- for listing the contents of the directory
# Formats of ls that will work in this shell:-
# ls , ls ~ , ls . , ls directoryname(complete path)

def ls(directory_name=""):
	if directory_name=="":
		directory_name="."
	elif directory_name=="~":
		directory_name=str(Path.home())
	# currentDirectory=pathlib.Path(directory_name)
	# for currentFile in currentDirectory.iterdir():
    # currentnewFile=currentFile.replace("home","/")  
	# 	print(currentFile)
	for i in os.listdir(directory_name):
		print(i)

def pwd():
	print(os.getcwd())

def cd(x):
	os.chdir(x)

# touch command format :- touch filename , touch filename1 filename2 filename3........

def touch(names):
	for name in names :
		f=open(name,"w+")
		f.close()

def grep(x,y):
	x1=0
	for line in open(y, 'r'):
    		if re.search(x,line):
    			x1=1
    			print(line)
	if x1==0:
	    print("pattern not found")

def tail(fname,nlines):
	nlines = int(nlines)

	# count the total number of lines
	if os.path.exists(fname):
		tot_lines = len(open(fname).readlines())

		# use line cache module to read the lines
		for i in range(tot_lines - nlines + 1, tot_lines+1):
		    print(linecache.getline(fname,i))

def head(fname,nlines):
	nlines = int(nlines)
	if os.path.exists(fname):
		with open(fname) as f:
			for l in (f.readlines()[0:nlines]):
				print(l)
def diff(fname,sname):
	with open(fname, 'r') as hosts0:
		with open(sname, 'r') as hosts1:
			dif=difflib.unified_diff(hosts0.readlines(),hosts1.readlines(),fromfile='hosts0',tofile='hosts1',n=0)
			for line in dif:
				f=["---","+++","@@"]
				for prefix in f:
					if line.startswith(prefix):
						break
					else:
						print(line[1:])

def tr(teststring,pattern1,pattern2):
	teststring=teststring.translate(str.maketrans(pattern1,pattern2))
	print(teststring)

while(1):	
	text=input("enter command to execute:")
	command=text.split()
	if command[0]=="exit":
		break
	elif command[0]=="ls":
		if len(command)==1 :
			ls()
		else:
			ls(command[1])
	elif command[0]=="pwd":
		pwd()	
	elif command[0]=="cd":
		cd(command[1])
	elif command[0]=="touch":
		touch(command[1:])
	elif command[0]=="grep":
		grep(command[1],command[2])
	elif command[0]=="diff":
		diff(command[1],command[2])
	elif command[0]=="tail":
		if len(command)==2:
			tail(command[1],10)
		elif len(command)!=3:
			print('Usage:tail <file> <nlines>')
		else:
			tail(command[1],command[2])	
	elif command[0]=="head":
		if len(command)==2:
			head(command[1],10)
		elif len(command)!=3:
			print('Usage:head <file> <nlines>')
		else:
			head(command[1],command[2])	
	elif command[0]=="tr":
		if len(command)==4:
			tr(command[3],command[1],command[2])
		elif len(command)<=3:
			print('Usage:tr <character_set_to_be replaced> <character_set_to_be_replaced_into> text')
	elif command[0]=="sed": 
		for line in fileinput.input(command[3]):
			print(line.replace(command[1],command[2]))
			print("")




