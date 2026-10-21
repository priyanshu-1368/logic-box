border = "═" * 58
divider = "─" * 58

print("\n" + border)
print("  ╔══════════════════════════════════════════════════════╗")
print("  ║    PATTERN GENERATOR & NUMBER ANALYZER CLI APP       ║")
print("  ╚══════════════════════════════════════════════════════╝")
print(border)

while True:
    print("\n┌── [ MAIN MENU ] ───────────────────────────────────────┐")
    print("│  [1] Generate a Pattern                                │")
    print("│  [2] Analyze a Range of Numbers                        │")
    print("│  [3] Exit                                              │")
    print("└────────────────────────────────────────────────────────┘")
    choice = input(" ➤ Enter your choice: ").strip()

    match choice:
        case "1":
            print("\n" + divider + "\n")
            print("  ┌── [ SELECT PATTERN TYPE ] ───────────────────────────┐")
            print("  │  [1] Increasing Stars      [6] Hollow Square         │")
            print("  │  [2] Increasing Numbers    [7] Diamond Pattern       │")
            print("  │  [3] Decreasing Stars      [8] Butterfly Pattern     │")
            print("  │  [4] Decreasing Numbers    [9] Number Pyramid        │")
            print("  │  [5] Decreasing Start Num  [10] Star Pyramid         │")
            print("  └──────────────────────────────────────────────────────┘")

            pattern_choice = input("  ➤ Enter pattern choice (1-10): ").strip()

            if pattern_choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
                print("  [!] Invalid pattern choice.\n")
                continue

            user_input = input("  ➤ Enter the value: ").strip()

            if int(user_input) <= 0:
                print("  [!] Invalid input. Must be a positive whole number.\n")
                continue

            n = int(user_input)
            print("\n  ┌── [ PATTERN RESULT ] " + ("─" * 33))

            match pattern_choice:
                case "1":
                    for i in range(1, n + 1):
                        print("  │ " + ("*" * i))

                case "2":
                    for i in range(1, n + 1):
                        print("  │ ", end="")
                        for j in range(1, i + 1):
                            print(j, end="")
                        print()

                case "3":
                    for i in range(n, 0, -1):
                        print("  │ " + ("*" * i))

                case "4":
                    for i in range(n, 0, -1):
                        print("  │ ", end="")
                        for j in range(1, i + 1):
                            print(j, end="")
                        print()

                case "5":
                    for i in range(n, 0, -1):
                        print("  │ ", end="")
                        for j in range(i, n + 1):
                            print(j, end=" ")
                        print()

                case "6":
                    for i in range(n):
                        print("  │ ", end="")
                        for j in range(n):
                            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                                print("*", end=" ")
                            else:
                                print(" ", end=" ")
                        print()

                case "7":
                    for i in range(1, n + 1):
                        print("  │ " + " " * (n - i) + "*" * (2 * i - 1))
                    for i in range(n - 1, 0, -1):
                        print("  │ " + " " * (n - i) + "*" * (2 * i - 1))

                case "8":
                    for i in range(1, n + 1):
                        print("  │ " + "*" * i + " " * (2 * (n - i)) + "*" * i)
                    for i in range(n, 0, -1):
                        print("  │ " + "*" * i + " " * (2 * (n - i)) + "*" * i)

                case "9":
                    for i in range(1, n + 1):
                        print("  │ " + "  " * (n - i), end="")
                        for j in range(1, i + 1):
                            print(j, end=" ")
                        for j in range(i - 1, 0, -1):
                            print(j, end=" ")
                        print()

                case "10":
                    for i in range(1, n + 1):
                        print("  │ " + "  " * (n - i) + "* " * (2 * i - 1))
            print("  └" + ("─" * 54))

        case "2":
            print("\n" + divider)
            print("  ┌── [ NUMBER RANGE ANALYZER ] ─────────────────────────┐")
            start = int(input("  ➤ Enter the start of the range: "))
            end = int(input("  ➤ Enter the end of the range: "))
            print("  └──────────────────────────────────────────────────────┘")

            print("\n  ┌── [ ANALYSIS RESULT ] " + ("─" * 32))
            for num in range(start, end + 1):
                status = f"{num} is even." if num % 2 == 0 else f"{num} is odd."
                print(f"  │  {status}")
            print("  └" + ("─" * 54))

        case "3":
            print("\n" + border)
            print("  [✓] Exiting the program. Goodbye!")
            print(border + "\n")
            break

        case _:
            print("\n  [!] Invalid choice. Please select 1, 2, or 3.")
