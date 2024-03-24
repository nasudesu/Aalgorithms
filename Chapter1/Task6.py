total = 0
while True:
    try:
        number = float(input("Give a num: "))
        if number == 0:
            print(f"The grand total is {total}")
            break
        total += number
        print(f"The total is now {total}")
    except Exception as e:
        print("That wasn’t a number.")