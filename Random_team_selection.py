import random
from typing import OrderedDict
from colorama import Fore
class human:
    team_A=OrderedDict()
    team_B=OrderedDict()
    def __init__(self,random_list):
        self.random_list=random_list
class Soccer(human):
    list_A=[]
    def team(self):
        while True:
            len_random=2/len(self.random_list)
            for i in self.random_list:
                human.team_A[i]="team A"
                Soccer.list_A.append(i)
                if len(Soccer.list_A)==len(self.random_list)/2:
                    break
            if len(human.team_A)==len(self.random_list)/2:
                    break
        while True:
            for i in self.random_list:
                if i not in Soccer.list_A:
                    human.team_B[i]="team B"
                if len(human.team_B)==len(random_list)/2:
                    break
            if len(human.team_B)==len(random_list)/2:
                break
    def print(self):
        for key,value in human.team_A.items():
            print(Fore.RED,key,"= "+value)
        for key,value in human.team_B.items():
            print(Fore.BLUE,key,"= "+value)
print(Fore.YELLOW+'''please Please separate the 22 names using a hyphen (-) 
so that the program can run correctly =(Hossein - Maziar - Akbar - Nima - Mahdi - Farhad
- Mohammad - Khashayar - Milad - Mustafa - Amin - Saeed - Puya - Pouria - Reza - Ali - Behzad - Sohail - Behrouz - Shahroz - Saman - Mohsen)''')
body_list=[]
bodys=input(Fore.CYAN+"enter the bodys name: ")
bodys=[body_list.append(i)for i in bodys.strip().split("-")]
random_list=[]
while True:
    random_body = random.choice(body_list)
    if random_body not in random_list:
        random_list.append(random_body)
    if len(random_list)==len(body_list):
        break

body=human(random_list)
kian=Soccer(random_list)
kian.team()
kian.print()
