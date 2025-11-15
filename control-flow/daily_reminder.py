task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(
            f"Reminder: '{task}' is a high priority task"
            + (" that requires immediate attention today!" if time_bound == "yes" else "")
        )
    case "medium":
        print(
            f"Reminder: '{task}' is a medium priority task"
            + (" that requires immediate attention today!" if time_bound == "yes" else "")
        )
    case "low":
        print(
            f"Note: '{task}' is a low priority task"
            + (". Consider completing it when you have free time." if time_bound == "no" else "")
        )
    case _:
        print(f"Reminder: '{task}' has an unknown priority")
