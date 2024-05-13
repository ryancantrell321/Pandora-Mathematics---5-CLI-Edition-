"""
Below are the necessary modules which will be needed to form the algorithm of my program.
"""


import sys
import webbrowser
from sympy import Eq, solve, symbols, simplify
import numpy as np
import matplotlib.pyplot as plt


def error():
    """
    Display Error Message for Input out of Range when called. Also tells the user to try again.
    :return: Input out of range! Please try again!
    """

    print("Input out of range! Please try again!")
    print()


def error2():
    """
    Display Error Message for invalid answer when called. Also tells the user to try again.
    :return: Invalid answer! Please try again!
    """

    print("Invalid answer! Please try again!")
    print()


def error3():
    """
    Display Error Message for invalid input when called. Also tells the user to try again.
    :return: Invalid Input! Please try again!
    """

    print("Invalid Input. Please try again.")
    print()


def thanks():
    """
    Thanks the user after the system concludes.
    :return: Thank you for using our interactive system. We hope you enjoyed it!
    """

    print()
    print("Thank you for using our interactive system. We hope you enjoyed it!")
    print()


def cc_license():

    """
    Displays Creative Commons License specified in the directory.
    :return:
    """

    creative_commons_license = "https://pandora-dynamics.rf.gd/software-licenses/pandora-mathematics-5-cli-python/LICENSE.html"
    webbrowser.open(creative_commons_license)


def display():
    """
    Displays chapters for the program.
    :return:
    """

    print("""This interactive program contains the following chapters.
Press the respective numbers for their respective chapters to get their questions or press 7 to exit:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Algebra
6. Geometry
7. Exit the program [You can always use 'CTRL + Z' on your keyboard to exit the program anytime]
""")


# Introducing the program, its licence, its contents
print()
print("Welcome to Pandora Mathematics - 5, an interactive mathematics program for 5th graders!")
print("Version: 1.0 (Python)")


cc_license()

display()

STATUS = True

# Looping the input and asking users to specify criteria:

while STATUS:

    try:
        while STATUS:
            print()
            choice = int(input("Enter your choice: "))
            print()

            if choice >= 8:
                error()
                break

            elif choice <= 0:
                error()
                break

            # Executing question 1:

            elif choice == 1:
                print("Solve the following by adding the numbers:")
                print()
                print("1. (-11) + 15 + 17 + (-11)")

                while STATUS:
                    ans = float(input("Enter your answer: "))
                    print(f"My answer: {int(ans)}")

                    S1 = -11 + 15 + 17 - 11

                    if ans == S1:
                        print("Your answer is correct! Proceeding to the chapter selection...")
                        print()
                        break

                    else:
                        error2()

                display()

            # Executing question 2:

            elif choice == 2:
                print("Solve the following by subtracting the numbers:")
                print()
                print("2. -2136 from 5761")

                while STATUS:
                    ans = float(input("Enter your answer: "))
                    print(f"My answer: {int(ans)}")

                    S2 = 5761 - (-2136)

                    if ans == S2:
                        print("Your answer is correct! Proceeding to the chapter selection...")
                        print()
                        break

                    else:
                        error2()

                display()

            # Executing question 3:

            elif choice == 3:
                print("Solve the following by multiplying the numbers:")
                print()
                print("3. 12 x (-2) x (-3) x (-5)")

                while STATUS:
                    ans = float(input("Enter your answer: "))
                    print(f"My answer: {int(ans)}")

                    S3 = 12 * (-2) * (-3) * (-5)

                    if ans == S3:
                        print("Your answer is correct! Proceeding to the chapter selection...")
                        print()
                        break

                    else:
                        error2()

                display()

            # Executing question 4:

            elif choice == 4:
                print("Solve the following by dividing the numbers:")
                print()
                print("4. (-166375) / (-11) ")

                while STATUS:
                    quotient = float(input("Enter your quotient: "))
                    remainder = float(input("Enter your remainder: "))
                    print(f"""My answer:
                    Quotient = {int(quotient)}
                    Remainder = {int(remainder)}""")
                    print()

                    S4 = (-166375) / (-11)
                    S5 = (-166375) % (-11)

                    if quotient == S4 and remainder == S5:
                        print("Your answer is correct! Proceeding to the chapter selection...")
                        print()
                        break

                    else:
                        error2()

                display()

            # Executing question 5:

            elif choice == 5:

                # Solve the equation

                x = symbols("x")
                equ = Eq(2*x - (3*x + 5) - 85, -9*x + (6*x-5) + 9)
                print("Solve the following algebraic mathematics: ")
                print()
                print("5. 2x - (3x + 5) - 85 = -9x + (6x-5) + 9")
                steps = solve(equ, x, dict=True)

                while STATUS:
                    ans = input("Enter the value of x: ")

                    if simplify(ans) == steps[-1][x]:
                        print("Your answer is correct! Proceeding to the chapter selection...")
                        print()
                        break

                    else:
                        error2()

                display()

            # Executing question 6:

            elif choice == 6:
                while STATUS:
                    try:
                        print("6. Enter the values below to form different lines: ")
                        a = float(input("Enter value a: "))
                        b = float(input("Enter value b: "))
                        print(f"Point 1 (x1, y1): {a, b}")
                        c = float(input("Enter value c: "))
                        d = float(input("Enter value d: "))
                        print(f"Point 2 (x2, y2): {c, d}")
                        e = float(input("Enter value e: "))
                        f = float(input("Enter value f: "))
                        print(f"Point 3 (x3, y3): {e, f}")
                        g = float(input("Enter value g: "))
                        h = float(input("Enter value h: "))
                        print(f"Point 4 (x4, y4): {g, h}")

                        p1 = np.array([(a, b), (c, d), (e, f), (g, h)])
                        plt.plot(p1, marker="o")
                        plt.show()
                        break

                    except ValueError:
                        error2()

                display()

            elif choice == 7:
                thanks()
                sys.exit()

    except ValueError:
        error3()
        continue
