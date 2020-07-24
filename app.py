import requests
import subprocess as sp
import sys
# https://notebooks.gesis.org/binder/jupyter/user/ipython-ipython-in-depth-zykvi430/notebooks/binder/Facelabs%20Python.ipynb#
# https://stackoverflow.com/questions/18937058/clear-screen-in-shell/47296211
response = requests.get('https://opentdb.com/api.php?amount=5&category=15&difficulty=easy&type=boolean').json()

#saving the score
score = 0

# for getting as much as questions in the future(no need to explicitly declare the variable)
i=sys.maxsize

#creating the basic UI
print("\t Welcome \t Python \t Quiz \t Maker\n")
print("**********\tRules of the Game:\t**********")
print("1. 5 Questions are going to asked\n")
print("2. Answer only in T/F/true/false/True/False/t/f\n")
print("3. Score will be shared after Full Quiz\n")
print("=======================================================")
# print("Please types only among them t/f/True/False/true/false")

for ques in response["results"]:

    # initialising string to get input as true/false 
    ans="good"
    
    #checking the value in string ans.
    if ans!="true" or ans!="false" or ans!='t' or ans!='f' or ans!="True" or ans!="False" or ans!='T' or ans!='F':
        while i!=0:
            print("=======================================================")
            # if ans is not correct we will continuously take the input for a particular let say 1. till we get  right
            # Right Input will be either true/false/t/f/T/F/True/False
            ans = input(ques["question"])
            if(ans=='t' or ans=="True" or ans=="true" or ans=="T"):
                ans="True"
                # tmp = sp.call('clear', shell=True)
                print("\nAnswer Submitted\n")
                break
            if(ans=='f' or ans=="False" or ans=="false" or ans=="F"):
                ans="False"
                # tmp = sp.call('clear', shell=True)
                print("\nAnswer Submitted\n")
                break
            else:
                print("\nWrong Input: Try Again\nPlease types only among them t/f/True/False/true/false\n")

        # iterate till all the answers are not given
        i-=1
    else:
        print("Answer Given!")

    
    if ans == ques["correct_answer"]: score+=1

print("\n\nCongratulations Your score Is- {}".format(score))