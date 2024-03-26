# num_list = [12, 12, 14]

# total = 0
# for num in num_list:
#     total += num
#     print(f"Current total: {total}")

attempts = 1

while attempts != 3:
    prompt = input("Password? ")
    attempts += 1
    if prompt == "hi":
        print("Welcome")
        break
    else:    
        print("Incorrect password")
        attempts += 1
       