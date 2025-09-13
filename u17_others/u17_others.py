# age = 0 
# height = float(0)  
# rejected = 0
# rider = 0 
# age = int(input("Please enter your age" )) 
# height = float(input("Please enter your height "))  
# while age != 0 and height != 0: 
#     if age < 7 or age > 70 or height <= 1.3:  
#         if age < 7: 
#          print("You are too young to ride")  
#         if age > 70: 
#          print("You are too old to ride")  
#         if height <= 1.3: 
#          print("You are too short to ride")  
#         rejected += 1
#     else: 
#          print("You can ride the Roller Coaster")  
#          rider += 1
#     age = int(input("Please enter your age ")) 
#     height = float(input("Please enter your height "))  
# print("Number of people rejected: ", rejected)  
# print("Number of riders: ", rider) 
# rejected = 0
# rider = 0

# age = int(input("Please enter your age: "))
# height = float(input("Please enter your height: "))

# while age != 0 and height != 0:
#     if age < 7 or age > 70 or height <= 1.3:
#         if age < 7:
#             print("You are too young to ride")
#         if age > 70:
#             print("You are too old to ride")
#         if height <= 1.3:
#             print("You are too short to ride")
#         rejected += 1
#     else:
#         print("You can ride the Roller Coaster")
#         rider += 1

#     age = int(input("Please enter your age: "))
#     height = float(input("Please enter your height: "))

# print("Number of people rejected: ", rejected)
# print("Number of riders: ", rider)























# bags_rice = int(input("Please input the number of rice you want"))
# upper_bound = 5.1 
# lower_bound = 4.9 
# bags_under = []
# bags_over = []
# for count in range(bags_rice): 
#     bag_weight = float(input("Enter the weight of the bag of rice "))  
#     if bag_weight > upper_bound: 
#         print("The bag of rice is overweight") 
#         bags_over.append(bag_weight)
#     elif bag_weight < lower_bound: 
#         print("The bag of rice is underweight")
#         bags_under.append(bag_weight)
#     else:
#         print("The bag is accpetable")
# print(" The total number of overweight bags are:",len(bags_over))
# print("The total number of underweight bags are:",len(bags_under))
# TASK 3
# capital_cities = { 
#  'singapore':'Singapore', 
#  'japan':'Tokyo', 
#  'australia':'Canberra', 
#  'england':'London', 
#  'france':'Paris', 
#  'germany':'Berlin' 
# } 
# country = input("Please enter the name of a country: ").lower()
# remove = input("Would you like to remove any of the entries? (Y or N): ").lower()
# add = input("Would you like to add a new entry? (Y or N): ").lower()
# if country in capital_cities:
#     print(" The capital city of", country.title(),"is", capital_cities[country])
# else: 
#     print("SORRy")
# if remove == "y":
#     del capital_cities[country]
#     print([capital_cities])
# if add == "y":
#    x = input(f"What is the capital city of {country.title()}?").title()
#    capital_cities[country] = x
#    print(capital_cities)
# age = 0 
# height = float(0)  
# rejected = 0
# rider = 0 
# age = int(input("Please enter your age" )) 
# height = float(input("Please enter your height "))  
# while age != 0 and height != 0: 
#     if age < 7 or age > 70 or height <= 1.3:  
#         if age < 7: 
#             print("You are too young to ride")  
#         elif age > 70: 
#             print("You are too old to ride")  
#         elif height <= 1.3: 
#             print("You are too short to ride")  
#         rejected += 1
#     else: 
#         print("You can ride the Roller Coaster")  
#         rider += 1 
#     age = int(input("Please enter your age ")) 
#     height = float(input("Please enter your height "))  
# print("Number of people rejected: ", rejected)  
# print("Number of riders: ", rider) 

# while True:
#     players = int(input("What is the number of players"))
#     if players <= 0 :
#         print("That is invalid")
#     else:
#         break
# names = []
# pages_read = []
# for i in range(players):
#     name = input(f"Enter the name of participant {i+1} :")
#     pages = int(input(f"Enter pages read by {name}:"))
#     while pages < 0:
#         print("Pages read must be a postivie interger,")
#         pages = int(input(f"Re-enter pages by {name}:"))
#     names.append(name)
#     pages_read.append(pages)




# bags_rice = int(input("Please enter the amount of bags of rice"))
# upper_bound = 5.1 
# lower_bound = 4.9 
# bags_under = []
# bags_over = []
# for count in range(bags_rice): 
#     bag_weight = float(input("Enter the weight of the bag of rice "))  
#     if bag_weight > upper_bound: 
#         print("The bag of rice is overweight") 
#         bags_over.append(bag_weight)
#     elif bag_weight < lower_bound: 
#         print("The bag of rice is underweight")
#         bags_under.append(bag_weight)
#     else:
#         print("The bag of rice is the correct weight")
# length_over = len(bags_over)
# length_under = len(bags_under)
        
# print(f"The number of overweight rice bags are: {length_over}")
# print(f"The number of underweight rice bags are: {length_under}")


# capital_cities = { 
#  'singapore':'Singapore', 
#  'japan':'Tokyo', 
#  'australia':'Canberra', 
#  'england':'London', 
#  'france':'Paris', 
#  'germany':'Berlin' 
# } 
# country = input("Please enter the name of a country: ").lower()
# remove = input("Would you like to remove any of the entries? (Y or N): ").lower()
# add = input("Would you like to add a new entry? (Y or N): ").lower()
# if country in capital_cities:
#     print(f"The capital city of the", country.title(),"is",capital_cities[country])
#     print(capital_cities[country])
# if remove == "y":
#     del capital_cities[country]
#     print(capital_cities)
# if add == "y":
#     x = input("what country would u like to add")
#     y = input("What is the capital city of the country")
# else:
#     print("That country is not in the list")
#     capital_cities[x] = y.title()
#     print(capital_cities)


                  
# age = 0 
# height = float(0)  
# rejected = 0 #change from 100 to 0
# rider = 0 
# age = int(input("Please enter your age" )) #missing aporstroche
# height = float(input("Please enter your height "))  
# while age != 0 and height != 0: #not equal to
#  if age < 7 or age > 70 or height <= 1.3:  
#      if age < 7: 
#          print("You are too young to ride")  
#      elif age > 70: #70 not 90
#          print("You are too old to ride")  
#      elif height <= 1.3: 
#          print("You are too short to ride")  
#          rejected += 1 
#      else: 
#          print("You can ride the Roller Coaster")  
#          rider += 1 
#  age = int(input("Please enter your age ")) 
#  height = float(input("Please enter your height "))  
# print("Number of people rejected :", rejected)  
# print("Number of riders: ", rider) 

# Task 5.1
def shift(char):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
    else:
        return char
# Task 5.2
def encrypt(message, positions):
    encrypted_message = ""
    for char in message:
        shifted_char = char
        for _ in range(positions):
            shifted_char = shift(shifted_char)
        encrypted_message += shifted_char
    return encrypted_message
# Task 5.3
def shift_up(char):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') - 1) % 26 + ord('a'))
    else:
        return char
# Task 5.4
def decrypt(ciphertext, positions):
    decrypted_message = ""
    for char in ciphertext:
        shifted_char = char
        for _ in range(positions):
            shifted_char = shift_up(shifted_char)
        decrypted_message += shifted_char
    return decrypted_message
# Task 5.5
while True:
    mode = input("Enter 'E' to encrypt or 'D' to decrypt: ").strip().lower()
    if mode in ['e', 'd']:
        break
    print("Invalid choice. Please enter E or D.")

text = input("Enter your message: ")

while True:
    try:
        positions = int(input("Enter number of positions to shift: "))
        if positions > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if mode == 'e':
    result = encrypt(text, positions)
    print("Encrypted message:", result)
    with open("encrypted.txt", "w") as f:
        f.write(result)
elif mode == 'd':
    result = decrypt(text, positions)
    print("Decrypted message:", result