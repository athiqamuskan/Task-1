first_val = float(input("Enter the first value: "))
second_val = float(input("Enter the second value: "))
print("\nSelect an operation to perform:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
operation = input("Enter your choice (a/b/c/d): ")
if operation == 'a':
    outcome = first_val + second_val
    print("Answer:", outcome)
elif operation == 'b':
    outcome = first_val - second_val
    print("Answer:", outcome)
elif operation == 'c':
    outcome = first_val * second_val
    print("Answer:", outcome)
elif operation == 'd':
    if second_val != 0:
        outcome = first_val / second_val
        print("Answer:", outcome)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid option selected")
