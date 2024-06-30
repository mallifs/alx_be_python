task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (Yes/No): " ).lower()

reminder = ""

match priority:
    case "high":
        reminder = f"{task} is a high priority"
    case "medium":
        reminder = f"{task} is a medium priority"
    case "low":
        reminder = f"{task} is a low priority"        


if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print("Reminder:", reminder)


