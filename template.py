from os import system

TASK = ""

while TASK != "x":
    system("clear")
    TASK = input("""Please type a number to chose the task:
[1] - Task 1
[2] - Task 2
[3] - Task 3
[4] - Task 4
[x] - Exit
""")
    print()

    # Task 1
    if TASK == "1":
        print("<INSTRUCTIONS>")
        print()

        print("Your result should look like this: ")
        print("<Teacher example>")
        print()

        # Write your code here
        print("<Student code 1>")

    # Task 2
    elif TASK == "2":
        print("<INSTRUCTIONS>")
        print()

        print("Your result should look like this: ")
        print("<Teacher example>")
        print()

        # Write your code here
        print("<Student code 2>")

    # Task 3
    elif TASK == "3":
        print("<INSTRUCTIONS>")
        print()

        print("Your result should look like this: ")
        print("<Teacher example>")
        print()

        # Write your code here
        print("<Student code 3>")

    # Task 4
    elif TASK == "4":
        print("<INSTRUCTIONS>")
        print()

        print("Your result should look like this: ")
        print("<Teacher example>")
        print()

        # Write your code here
        print("<Student code 4>")

    # Task 5
    elif TASK == "5":
        print("<INSTRUCTIONS>")
        print()

        print("Your result should look like this: ")
        print("<Teacher example>")
        print()

        # Write your code here
        print("<Student code 5>")
        
    # Task 6
    elif TASK == "6":
        print("<INSTRUCTIONS>")
        print()

        print("Your result should look like this: ")
        print("<Teacher example>")
        print()

        # Write your code here
        print("<Student code 7>")

    # Task 7
    elif TASK == "7":
        print("<INSTRUCTIONS>")
        print()

        print("Your result should look like this: ")
        print("<Teacher example>")
        print()

        # Write your code here
        print("<Student code 8>")

    if TASK != "x":
        input("Press Enter to continue...")
        continue
    else:
        print("Alright, see you!")