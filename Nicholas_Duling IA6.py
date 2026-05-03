# Define the main function to control the program flow
def main():

    #  set the daily steps goal
    def set_steps_goal():
        goal = int(input("Enter your daily steps goal: "))
        return goal

    # Define a function for recordIng daily steps for 7 days
    def record_daily_steps():
        total_steps = 0

        # Loop through the 7 days of the week
        for day in range(1, 8):
            steps = int(input(f"Enter the number of steps for day {day}: "))
            total_steps = total_steps + steps

        return total_steps

    #  Evaluate the weekly performance
    def evaluate_weekly_performance(goal, total_steps):

        # Calculate the average daily steps
        average_steps = total_steps / 7

        # Display Average daily steps.
        print(f"\nYour average daily steps for the week is {average_steps:.2f}.")

        # Compare the average with the daily goal
        if average_steps > goal:
            print(f"You exceeded your daily steps goal on average.")
        elif average_steps == goal:
            print(f"You met your daily steps goal on average.")
        else:
            print(f"You did not meet your daily steps goal on average.")

    # get your daily goal
    steps_goal = set_steps_goal()

    # Call the function to record the weekly steps
    weekly_total = record_daily_steps()

    # Call the function to evaluate the weekly performance
    evaluate_weekly_performance(steps_goal, weekly_total)


# Call the main function to start the program
main()