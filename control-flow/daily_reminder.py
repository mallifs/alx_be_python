task = input("Enter your task: ").lower()
priority = input("Priority (High,medium and low): ").lower()
time_bond = input("Is it time-bound? (Yes/No): " ).lower()

reminder = ""

match priority:
    case "high":
        reminder = f"{task} is a high priority"
    case "medium":
        reminder = f"{task} is a medium priority"
    case "low":
        reminder = f"{task} is a low priority"        


if time_bond == "yes":
    reminder += ". That requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print("Reminder:", reminder)


