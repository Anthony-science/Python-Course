# def add(num1, num2):
#     """This is a function that returns the sum of num1 and num2"""
#     return num1 + num2


# ans = add(23, 80)

# print(ans)

# num = 0
# while num < 20:
#     num += 1
#     print(num)

total = 0

guess_the_number = int(input("Enter number (-1 to exit)"))

while guess_the_number != -1:
    total += guess_the_number

    guess_the_number = int(input("Enter number (-1 to exit)"))
    
    if guess_the_number == -1:
        print(total)
        break
print("Finished.")