#greet the user
print("Hello, I'm a fortune teller.")
# ask the user if they want their fortune told
answer = input("Do you want a fortune? yes/no ")
#fortune given
while answer.lower() != "no":
#ask if user wants another fortune
    print("Fortune :)")
    answer = input("Do you want another fortune? yes/no ")
#repeat until user quits