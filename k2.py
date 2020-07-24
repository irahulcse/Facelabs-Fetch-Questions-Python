
# #     print("*************")
# #     i += 1
# import requests

# response = requests.get('https://opentdb.com/api.php?amount=5&category=15&difficulty=easy&type=boolean').json()

# score = 0

# for ques in response["results"]:
#     print(ques["correct_answer"])
#     print("***********************")
#     ans = input(ques["question"])
#     if ans == ques["correct_answer"]:
#         score+=1

# print("Your score - {}".format(score))


# import requests

# response = requests.get('https://opentdb.com/api.php?amount=5&category=15&difficulty=easy&type=boolean').json()

# # print(response['results'])
# # print(response.keys())
# # print(type(response['results']))
# i = 0
# sizeofList = len(response['results']) 
# print(sizeofList)
# # substring="u'question"
# while i < sizeofList :
#     print(((response['results'])[i]))
#     i+=1

    


import requests
import subprocess as sp

response = requests.get('https://opentdb.com/api.php?amount=5&category=15&difficulty=easy&type=boolean').json()
score = 0
i=1000000000000000000000
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
            if(ans=='t' or ans=="True" or ans=="true"):
                ans="True"
                tmp = sp.call('clear', shell=True)
                print("\nAnswer Submitted\n")
                break
            if(ans=='f' or ans=="False" or ans=="false"):
                ans="False"
                tmp = sp.call('clear', shell=True)
                print("\nAnswer Submitted\n")
                break
            else:
                print("\nWrong Input\nPlease types only among them t/f/True/False/true/false\n")
 
        i-=1
    else:
        print("Answer Given!")

    
    if ans == ques["correct_answer"]: score+=1

print("\n\nCongratulations Your score Is- {}".format(score))