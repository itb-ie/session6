while True:
    try:
        num = int(input("Enter a number: "))
        break  # break out of the loop
    except ValueError:
        print("That's not a number!")

print("You entered: ", num)
