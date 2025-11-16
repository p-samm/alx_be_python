# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next row
    row += 1
