print("\n Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    choice = input("\nEnter your choice: ")

    match choice:
        case "1":
            print("\nSelect a pattern type:")
            print("1. Increasing Stars")
            print("2. Increasing Numbers")
            print("3. Decreasing Stars")
            print("4. Decreasing Numbers")
            print("5. Decreasing Start Numbers")

            pattern_choice = input("\nEnter your choice (1-5): ")

            if pattern_choice not in("1", "2", "3", "4", "5"):
                print("Invalid pattern choice.\n")
                continue

            user_input = input("Enter the number of rows for the pattern: ")

            if int(user_input) <= 0:
                print("Invalid input. Row count must be a positive whole number.\n")
                continue

            rows = int(user_input)
            print("\nPattern:")

            match pattern_choice:
                case "1":
                    for i in range(1, rows + 1):
                        print("*" * i)

                case "2":
                    for i in range(1, rows + 1):
                        for j in range(1, i + 1):
                            print(j, end="")
                        print()

                case "3":
                    for i in range(rows, 0, -1):
                        print("*" * i)

                case "4":
                    for i in range(rows, 0, -1):
                        for j in range(1, i + 1):
                            print(j, end="")
                        print()

                case "5":
                    for i in range(rows, 0, -1):
                        for j in range(i, rows + 1):
                            print(j, end=" ")
                        print()

        case "2":
             start = int(input("\nEnter the start of the range: "))
             end = int(input("Enter the end of the range: "))

             for num in range(start, end + 1):
                    print(f"{num} is even." if num % 2 == 0 else f"{num} is odd.")

        case "3":
            print("\nExiting the program. Goodbye! \n")
            break

        case _:
            print("Invalid choice. Please select 1, 2, or 3.\n")