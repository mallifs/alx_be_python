task = input("Enter a task: ").lower()
priority = input("Enter priority (High,medium and low): ").lower()
time_bond = input("Yes/No: " ).lower()

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


