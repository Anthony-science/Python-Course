# Initialise total_int = 0
# user_count = 0
# Prompt for number from user = user_int
# Check whether user_int == -1
    # If user_int != -1, add user_int to total_int
    # Count number of occurences of user input
    # If user_int == -1 then calcuate mean of numbers entered (excluding -1) as (total_int + 1) / count

total_int = 0
user_count = 0
user_int = int(input("Please enter a number: "))

while user_int != -1:
    user_count += 1
    total_int = total_int + user_int
    user_int = int(input("Please enter a number: "))
    if user_int == -1:
        print(f"Average of inputted numbers = {total_int / user_count}")
        break
    





