print("Welcome to Desire's Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
bread = input("Do you want thin bread? Y or N \n")
bill = 0

if size == "S":
    bill += 150
elif size == "M":
    bill += 200
else:
    bill += 250

if add_pepperoni == "Y":
    if size == "S":
      bill += 20
    else:
      bill += 30
    
if extra_cheese == "Y":
    bill += 10
  
if bread == "Y":
    bill += 50
  
print(f"Your final bill is: Rs.{bill}.")
