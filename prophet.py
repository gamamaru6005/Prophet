#!/usr/bin/env python

import app.scanner.scan_controller as scan_controller
from app.util import clean

living = True
while living:
	cmd = raw_input()
	if(cmd.lower() == "scan"):
		scan_controller.RunAll()

	elif(cmd.lower().startswith("parse ")):
		scan_controller.ParseScan(cmd.split(' ')[1])
	elif(cmd.lower() == "exit" or cmd.lower() == "quit"):
		living = False
	elif(cmd.lower() == "clean"):
		clean.clean()
	else:
		print("Valid commands are:")
		print("Scan: runs scan")
		print("Parse <scan id>: update reports based on the scan id")

		print("Exit: End Program")
		
