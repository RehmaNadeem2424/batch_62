# STEP 1:
name = (input("enter your name:"))
print(name)
# STEP 2:
number= []
number.append(int(input("enter your 1st favourite number:")))
number.append(int(input("enter your 2nd favourite number:")))
number.append(int(input("enter your 3rd favourite number:")))
print(f"\n Hello , {name} let's explore your favourite numbers")
# STEP 3:
even_odd = []
for num in number:
    if num % 2 == 0:
        even_odd.append((num, "even"))
    else:
        even_odd.append((num,"odd")) 
for evenodd in even_odd:            
 print(f"\n the number is {evenodd}")
 # STEP 4:
print(f"\n Here are your number than square")
for num in number:
    square = num * num
    print(f"the square of {num} is :{square}")
# STEP 5:
sum = number[0] + number[1] + number[2]
print(f"\n the sum of three favourite number is :{sum}") 
print(f"great job , {name} number are fascinating aren't they?")
# STEP 6:
print(f"\n Wow {sum} is prime number") 