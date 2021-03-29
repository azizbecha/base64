import os
import sys
import hashlib

class color:
	HEADER = '\033[95m' #move
	BLUE = '\033[94m' #blue
	GREEN = '\033[92m' #green
	WARNING = '\033[93m' #orange                                  
	FAIL = '\033[91m' #red
	END = '\033[0m' #end color
	BOLD = '\033[1m' #gras
	UNDERLINE = '\033[4m' #underline
        BLEUCIEL = '\033[1;36m' #bleuciel

def enc():
    string = raw_input(color.GREEN+color.BOLD+"[+] Enter String To Encode: "+color.END)
    command = ("echo '"+string+"' | base64 ")
    proces = os.popen(command)
    results = str(proces.read())
    print (color.WARNING+color.BOLD+"[+] Decoded String ==> "+string)
    print ("[+] Encoded String ==> "+results+color.END)
    save = raw_input(color.BLUE+color.BOLD+"[+] Save Output in File ? (y/n) "+color.END)
    if save in ['Y', 'y','yes', 'YES']:
     file_path = raw_input("Enter The File Path: ")
     file_ = open(file_path, "a+")
     file_.write(string+':'+results+"\n" )
     file_.close() 
     print (color.WARNING+color.BOLD+"[+] Results Are Succesfully Saved ..."+color.END)
    else:
      print (color.GREEN+color.BOLD+"[+] Results Will Not Be Saved..."+color.END)
      

def dec():
    string = raw_input("[+] Enter String To Decode: ")
    command = ("echo '"+string+"' | base64 -d")
    proces = os.popen(command)
    results = str(proces.read())
    print (color.WARNING+color.BOLD+"[+] Decoded String ==> "+string)
    print ("[+] Encoded String ==> "+results+color.END)
    save = raw_input(color.BLUE+color.BOLD+"[+] Save Output in File ? (y/n) "+color.END)
    if save in ['Y', 'y','yes', 'YES']:
     file_path = raw_input("Enter The File Path: ")
     file_ = open(file_path, "a+")
     file_.write(string+':'+results+"\n" )
     file_.close() 
     print (color.WARNING+color.BOLD+"[+] Results Are Succesfully Saved ..."+color.END)
    else:
      print (color.GREEN+color.BOLD+"[+] Results Will Not Be Saved..."+color.END)
   

def screen():
    os.system("clear")
    os.system("figlet Base64 Enc / Dec")
    print (color.BOLD+color.BLUE+"Select from the menu: \n")
    print ("{1}--- Encode Base64")
    print ("{2}--- Decode Base64")
    print ("{99}-- Exit"+color.END)
    choice = raw_input(color.BOLD+">>> "+color.END)
    if choice == "1":
       enc()
    elif choice == "2":
       dec()
    elif choice == "99":
       print ("Quitting ...") 
       sys.exit()   
    else:
      print ("Please Choose a number from the list")

screen()
