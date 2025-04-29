user_input=input("Enter a string:")

with open("user_input_file.txt",'a') as save:
    save.write(user_input)
    save.write('\n')
