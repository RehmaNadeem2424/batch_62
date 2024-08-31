# STEP 1:
name = (input("enter your name:"))
# STEP 2:
num_list= []
number = int(input("enter your 1st favourite number:"))
number = int(input("enter your 2nd favourite number:"))
number = int(input("enter your 3rd favourite number:"))
num_list.append(number)
print(f"\n Hello , {name} let's explore your favourite number") 
# STEP 3:
for x in num_list:
    if x  % 2 == 0:
        print(f"the number is {x} is even")
    else: 
        print(f"the number is {x} odd") 
# STEP 4:
for x in num_list:
    print(f"the number {x} and its square:({x} , {x ,2})")