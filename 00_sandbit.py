
import random 

chosen_number = random.randint(1,20)
choose_number = random.randint(1,20)


question = "{} + {}".format(chosen_number,choose_number)
answer = eval(question)

print(question)
print(answer)