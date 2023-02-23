# Read two numbers from the user and divide them
while True:
    try:
        num = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        if num2 == 0:
            print("Can't divide by zero!")
            continue
        break  # break out of the loop
    except ValueError:
        print("That's not a number!")
print("The result is: ", num / num2)

