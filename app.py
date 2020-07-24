import requests
import subprocess as sp
import sys
# https://notebooks.gesis.org/binder/jupyter/user/ipython-ipython-in-depth-zykvi430/notebooks/binder/Facelabs%20Python.ipynb#
# https://stackoverflow.com/questions/18937058/clear-screen-in-shell/47296211
response = requests.get('https://opentdb.com/api.php?amount=5&category=15&difficulty=easy&type=boolean').json()
score = 0
i=sys.maxsize
print("\t Welcome \t Python \t Quiz \t Maker\n")
print("**********\tRules of the Game:\t**********")
print("1. 5 Questions are going to asked\n")
print("2. Answer only in T/F/true/false/True/False/t/f\n")
print("3. Score will be shared after Full Quiz\n")
print("=======================================================")
# print("Please types only among them t/f/True/False/true/false")

for ques in response["results"]:
    # ans = input(ques["question"])
    ans="good"
    if ans!="true" or ans!="false" or ans!='t' or ans!='f' or ans!="True" or ans!="False" or ans!='T' or ans!='F':
        while i!=0:
            print("=======================================================")
            ans = input(ques["question"])
            if(ans=='t' or ans=="True" or ans=="true" or ans=="T"):
                ans="True"
                #pls remove the tmp line for the error if using MacOS/Windows
                # tmp = sp.call('clear', shell=True)
                print("\nAnswer Submitted\n")
                break
            if(ans=='f' or ans=="False" or ans=="false" or ans=="F"):
                ans="False"
                #pls remove the tmp line for the error if using MacOS/Windows
                # tmp = sp.call('clear', shell=True)
                print("\nAnswer Submitted\n")
                break
            else:
                print("\nWrong Input: Try Again\nPlease types only among them t/f/True/False/true/false\n")
 
        i-=1
    else:
        print("Answer Given!")

    
    if ans == ques["correct_answer"]: score+=1

print("\n\nCongratulations Your score Is- {}".format(score))