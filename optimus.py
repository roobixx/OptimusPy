#!/usr/bin/python 

import os, sys, time

def banner ():
	print ""
	print "### Optimus Framework ###"
	print ""

def optimus ():

	banner()
	print "Project Options"
	print "[1] Configure Project"
	print "[2] Check Project Status"
	print "[3] Run NMAP"
	print "[4] Run EyeWitness"
	print "[5] Run Nessus Scan"
	print "[6] Start Metasploit Listener"
	print "[7] Generate Reports"
	print "[8] Export Project"
	print "[99] Exit"

	option = raw_input("Chose your Project Option: ")

	print ""

	if option == '1':
		configure_project()
		
	elif option == '2':
		project_status()

	elif option == '3':
		os.system("clear")
		nmap()

	elif option == '4':
		eyewitness()

	elif option == '5':
		nessus()

	elif option == '6':
		listener()

	elif option == '7':
		generate_reports()

	elif option == '8':
		export_reports()

	elif option == '99':
		print "Exiting Optimus..."
		time.sleep(1)
		os.system("clear")
		sys.exit()

	else:
		print ""
		print "Invalid Input"
		print ""
		time.sleep(1)
		os.system("clear")
		optimus()

def configure_project():
	name = raw_input("What is the name of your project?: ")
	if os.path.exists(name):
		print "Project already exists: " +name
		print ""
		print "Returning to Menu"
		optimus()
		
	else:
		print ""
		print "Creating new project named: " +name
		os.makedirs(name)
		directories = ['nmap' , 'eyewitness' , "nessus" , 'screenshots' , 'logs' , 'reports']
		root_path = name
		for directory in directories:
			os.makedirs(os.path.join(root_path, directory))
		print ""
		print "Project " +name+ " Successfully created."
		

def nmap():

    print "Scanning Options"
    print "[1] Intense Scan"
    print "[2] Intense Scan + UDP"
    print "[3] Intense Scan - all TCP ports"
    print "[4] Intense Scan w/out ping"
    print "[5] Ping Scan"
    print "[6] Quickie Scan"
    print "[7] Quick Traceroute"
    print "[8] Normal Scan"
    print "[9] Send Bad Checksums"
    print "[10] Generate Randon Mac Adress Spoofing for Evasion"
    print "[11] Fragment Packets"
    print "[12] Return to Project Options"
    print "[99] Exit Optimus"

    option = raw_input("Choose your Scanning Option:")

    print ""

    if option == '1':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap -T4 -A -v "+ip+ " -oX intense.xml")
        print "\n[**] Done \n"
        nmap()

    elif option == '2':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap -sS -sU -T4 -A -v "+ip)
        print "\n[**] Done \n"
        nmap()

    elif option == '3':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap -p 1-65535 -T4 -A -v "+ip)
        print "\n[**] Done \n"
        nmap()

    elif option == '4':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap -T4 -A -v -Pn "+ip)
        print "\n[**] Done \n"
        nmap()

    elif option == '5':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap -sn "+ip)
        print "\n[**] Done \n"
        nmap()

    elif option == '6':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap -T4 -F "+ip)
        print "\n[**] Done \n"
        nmap()

    elif option == '7':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap -sn --traceroute "+ip)
        print "\n[**] Done \n"
        nmap()

    elif option == '8':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap "+ip)
        print "\n[**] Done \n"
        nmap()

    elif option == '9':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap --badsum "+ip)
        print "\n[**] Done \n"
        nmap()

    elif option == '10':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap -sT -Pn --spoofmac 0 "+ip)
        print "\n[**] Done \n"
        nmap()

    elif option == '11':
        ip = raw_input("Input IP Address / Hostname:")
        os.system("nmap -f "+ip)
        print "\n[**] Done \n"
        nmap()

    elif option == '12':
        print "[**] Returning to Project Options\n"
        time.sleep(2)
        os.system("clear")
        optimus()

    elif option == '99':
		print "[**] Exiting Optimus...\n"
		time.sleep(2)
		os.system("clear")
		os.system("exit")

    else:
	print "\nInvalid Option..Let's try again >>\n"
        nmap()

# def eyewitness():

# def nessus():

# def listener():

def generate_reports():

	print "Report Generation Options"
	print "[1] Generate HTML nmap report"
	print "[2] Nessus report CSV"
	print "[3] Both"

	print ""

	options = raw_input("Select which reports you would like to generate")

	if option == '1':
		os.system("xsltproc ")

# def export_project():

if __name__ == "__main__":
    try:
    	os.system("clear")
        optimus()
        
    except KeyboardInterrupt: 
        print "\n Keyboard has been stopped :("
        time.sleep(2)
        pass