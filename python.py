import random 
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["@","#","_","&","*","?","!","$"]
nr_letter=int(input("How many letters do u want to add?"))
nr_number=int(input("How many numbers do u want to add?"))
nr_symbol=int(input("How many symbols do u want to add?"))
password_type=input("What type of password do u want yo create?Type'easy'or 'hard':")
if password_type=="easy":
    password=""
    for char in range(1,nr_letter+1):
        password+=random.choice(letters)
    for char in range(1,nr_numbers+1):
        password+=random.choice(numbers)
    for char in range(1,nr_numbers+1):
        password+=random.choice(symbols)
    print (f"Your password is:{password}")
  else:
    password=[]
    for char in range(1,nr_letter+1):
        password.append(random.choice(letters))
    for char in range(1,nr_number+1):
        password+=random.choice(numbers)
    for char in range(1,nr_symbol+1):
        password+=random.choice(symbols)
random.shuffle(password)
password_list=""
for char in password:
    password_list+=char
print(f"The password is:{password_list}")
