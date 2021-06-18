
import random 

chosen_number = random.randint(1,20)
choose_number = num_2 = "{}".format(int(input)/chosen_number)


question = "{} / {}".format(chosen_number,choose_number)
answer = eval(question)

print(question)
print(answer)