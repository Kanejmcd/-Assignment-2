"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    return float(annual_cost) / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    return float(annual_cost) / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    return float(annual_cost) / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    return float(annual_cost) / (SEMESTERS_PER_YEAR * credits)


def cost_per_class(annual_cost, credits):
    return (
        float(annual_cost)
        / (SEMESTERS_PER_YEAR * credits)
        * CS1430_CREDITS
        / CS1430_MEETINGS_PER_SEMESTER
    )


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the annual cost of college: "))
    # Then ask for the credits this semester.
    credits = int(input("Enter the number of credits for this semester: "))

    while True:
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"Cost per day: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per class: ${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "Q":
            break
        else:
            print("Invalid option. Please try again.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
