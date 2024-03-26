stars = "*"
for i in range (1, 9):       # Set range for number of lines
    if i <= 4:              # If statement to go up to 5 stars
        print(stars)
        stars = stars + "*"  # Increment star number 
    else:
        print(stars)
        stars = stars[:-1]   # Decrease star number
print("*")
