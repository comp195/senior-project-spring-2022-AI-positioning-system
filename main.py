import sys 
import math

def main():
    login()
    
def login():
    print("Welcome to use this project, new members")
    print("please set your name and password")
    print("the gust visit can just type guest and 123 as key to access the system")
    username="guest"
    password="123"
    print("Enter username : ")
    key=input()
    print("Enter password : ")
    key2=input()
  
    if key==username and key2==password:
        print("Welcome - Access system")
        menu()

def menu():
    print("************MAIN MENU**************")
    print()

    choice = input("""
                      A: upload your picture as png & jpg
                      B: Find similarity of pictures
                      C: Find text or numbers in picture
                      D: Find location
                      Q: Quit/Log Out
                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        upload()
    elif choice == "B" or choice =="b":
        similarity()
    elif choice == "C" or choice =="c":
        orcmessage()
    elif choice=="D" or choice=="d":
        location()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()

def upload():
    pass

def similarity():
    pass

def orcmessage():
    pass

def location():
    pass

main()
 
