from time import *
import random as r
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error+1
        except:
            error = error+1 
    return error
def time_speed(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed  = len(userinput)/time_r
    return round(speed)
    
test=["My name is muhammad qasim and i love r and m",
"i love cricket and football","welcome to python"]
test1 = r.choice(test)
print("****** Typing speed ******")
print(test1)
print()
print()
time_1 = time()
testinput=input(" Enter : ")
time_2 = time()

print("Speed : ",time_speed(time_1,time_2,testinput),"w/sec")
print("Error :",mistake(test1,testinput))

