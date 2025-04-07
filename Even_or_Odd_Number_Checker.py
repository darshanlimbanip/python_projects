while True:
    try:
        print("-_-_-_-_-_-_-_-_-_-_-")
        print("Let's find out, Number is Even or Odd? 🔍")
        
        user_input = (input("please enter your number or Type 'exit' to stop: "))

        if user_input.lower() == "exit":
            print("\n-_-_-_-_\n\nThank You 👋\n-_-_-_-_\n")
            break

        number = int(user_input)

        if number %2 == 0:
            print("\nThis is evne number\n")
        else:
            print("\nThis is odd number\n")

    except ValueError:
        print("\nPlease enter a valid number.\n")
