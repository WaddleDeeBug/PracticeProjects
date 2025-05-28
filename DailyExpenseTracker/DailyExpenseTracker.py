print("Welcome to the Daily Expense Tracker!")

# Display menu once
print("\n--- Daily Expense Tracker ---")
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

# Initialize an empty list to store expenses
expenses = []

while True:
    # Get user choice

    choice = input("Please select an option (1-5): ").strip()
    
    if choice == "1":
        # Add a new expense
        try:
            amount = float(input("Enter the expense amount: €"))
            expenses.append(amount)
            print(f"Expense of €{amount:.2f} added successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "2":
        # View all expenses
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]:.2f}")
    
    elif choice == "3":
        # Total and Average expense
        if not expenses:
            print("No expenses recorded yet.")
        else:
            total = sum(expenses)
            average = total / len(expenses)
            print(f"Total expense: €{total:.2f}")
            print(f"Average expense: €{average:.2f}")

    elif choice == "4":
        # Clear all expenses
        expenses.clear()
        print("All expenses cleared.")

    elif choice == "5":
        # Exit the program
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")