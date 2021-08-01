print ("Hi! Welcome to MJ's online clinic.")
import time
time.sleep(2)
print ("Here I will screen your symtomps by asking you simple questions.")
time.sleep(3)
print ("This will allow you to only spend the nessessary time in the hospital.") ###
time.sleep(3)
print ("I will also be assessing how critical your condition is.")
print ("  ")
time.sleep(2)
print ("To start off, I will ask you general questions about yourself.")
time.sleep(2)
age = int(input("1-How old are you? (if you are 42, only write : 42) "))
activity = int(input("2-How many times do you do sports per week? "))
weight = float(input("3-What's you weight in kg? "))
height = float(input("4-What's your height in m? "))
imc = weight // (height**2)
print ("Your body mass index is : ", imc, ".")
print ("Allo c'est la que chu rendue parce qu'il est tard!")
       

