from art1 import logo
from art1 import vs
from game_data import data
import random
import os
#clear = lambda: os.system('cls')
#clear()
def check_higher(higher,lower):
    '''TO check if 1st argument is higher than the second'''
    if data[higher]['follower_count']>data[lower]['follower_count']:
        return True
    else:
        return False
    
def display(first,second):
    '''display as A the 1st argument and B as the 2nd argument'''
    print(logo)
    print(f"Compare A: {data[first]["name"]},{data[first]["description"]},from {data[first]['country']}")
    print(f"Score:{score}")
    print(vs)
    print(f"Against B: {data[second]["name"]},{data[second]["description"]},from {data[second]['country']}")
    


data_dic = list(range(0,len(data)))

#print(data_dic)

to_compare = random.sample(data_dic,2)
#print(to_compare)
score = 0
a = to_compare[0]
b = to_compare[1]
correct=True

while correct and len(data_dic)!=0:
    #Removing the addresses as soon as used
    if a in data_dic:
        data_dic.remove(a)
    if b in data_dic:
        data_dic.remove(b)
    clear = lambda: os.system('cls')
    clear()
    display(first=a,second=b)
    if len(data_dic)==0:
        break
    prediction = input("Choose Who have higher follower: 'A' or 'B'? :  ").lower()

    if prediction == 'a':
        if check_higher(a,b):
            score += 1
            b = random.choice(data_dic)
            print(f"Correct prediction, Score:{score}")
        else:
            print(f"wrong prediction, score:{score}")
            correct = False
    elif prediction == 'b':
        if check_higher(b,a):
            score += 1
            a = int(b)
            b = random.choice(data_dic)
            print(f"Correct prediction, Score:{score}")
        else:
            print(f"wrong prediction, score:{score}")
            correct = False
    else:
        print("Enter a proper choice")   

if len(data_dic) == 0:
    print(f"You exhausted Names!!!! You won and your score:{score}") 