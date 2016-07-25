#!/usr/bin/python 

import os, sys, time

cwd = os.getcwd()
os.system("clear")
print "Your current working directory is: "+cwd
print "Projects will configured in this directory"	

def configure_project():
	name = raw_input("What is the name of your project?: ")
	if os.path.exists(name):
		print "Project already exists: " +name
		print ""
		print "Returning to Menu"
		
	else:
		print "Creating new project named: " +name
		os.makedirs(name)
		directories = ['nmap' , 'eyewitness' , "nessus" , 'screenshots' , 'logs' , 'reports']
		root_path = name
		for directory in directories:
			os.makedirs(os.path.join(root_path, directory))


if __name__ == "__main__":
    try:
        configure_project()
        
    except KeyboardInterrupt: 
        print "\n Keyboard has been stopped :("
        time.sleep(2)
        pass