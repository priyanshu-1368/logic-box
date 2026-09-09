print("Welcome to the Pattern Generator and Number Analyzer!")

running = True

while running:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nSelect a pattern type:")
        print("1.Increasing Stars")
        print("2.Increasing Numbers")
        print("3.Decreasing Stars")
        print("4.Decreasing Numbers")
        print("5.Hollow Stars")
        pattern_choice = input("Enter your choice (1-5): ")

        if pattern_choice not in ("1", "2", "3", "4", "5"):
            print("Invalid pattern choice.")
            continue

        user_input = input("Enter the number of rows for the pattern: ")

        if not user_input.isdigit():
            print("Invalid input. Please enter a positive whole number.")
            continue

        rows = int(user_input)

        if rows <= 0:
            print("Row count must be greater than zero.")
            continue

        print("\nPattern:")

        if pattern_choice == "1":
            i = 1
            while i <= rows:
                for j in range(i):
                    print("*", end="")
                print()
                i += 1

        elif pattern_choice == "2":
            i = 1
            while i <= rows:
                for j in range(1, i + 1):
                    print(j, end="")
                print()
                i += 1

        elif pattern_choice == "3":
            i = rows
            while i >= 1:
                for j in range(i):
                    print("*", end="")
                print()
                i -= 1

        elif pattern_choice == "4":
            i = rows
            while i >= 1:
                for j in range(1, i + 1):
                    print(j, end="")
                print()
                i -= 1

        elif pattern_choice == "5":
            i = 1
            while i <= rows:
                for j in range(1, i + 1):
                    if j == 1 or j == i or i == rows:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()
                i += 1

    elif choice == "2":
        start_input = input("Enter the start of the range: ")
        end_input = input("Enter the end of the range: ")

        if not (start_input.lstrip("-").isdigit() and end_input.lstrip("-").isdigit()):
            print("Invalid input. Please enter whole numbers only.")
            continue

        start = int(start_input)
        end = int(end_input)

        if end < start:
            print("End of range must be greater than or equal to start.")
            continue

        total = 0
        for num in range(start, end + 1):
            if num == 0:
                pass
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")
            total += num

        print(f"Sum of all numbers from {start} to {end} is: {total}")

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        running = False
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
