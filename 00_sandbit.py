import random 
num1 = random.randint(1,144)
num2 = num1 /random.randint( 1,12) 

question = "{} / {} ".format(num1, num2)
print(question)
answer = eval(question) 
print(answer)