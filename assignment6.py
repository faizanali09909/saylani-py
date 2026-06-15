pin = 1234
balance = 50000

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    print("\nWelcome Kashan Bank ATM\n")
    while True:
        print("Choose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n✅ Your balance is:", balance, "\n")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount < 0:
                print("\n❌ Amount cannot be negative\n")
            else:
                balance = balance + amount
                print("\n✅ Deposit successful. New balance:", balance, "\n")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("\n❌ Amount must be greater than 0\n")
            elif amount > balance:
                print("\n❌ Insufficient Balance\n")
            else:
                balance = balance - amount
                print("\n✅ Withdrawal successful. New balance:", balance, "\n")

        elif choice == "4":
            old_pin = int(input("Enter old PIN: "))
            if old_pin != pin:
                print("\n❌ Old PIN is incorrect\n")
            else:
                new_pin = input("Enter new PIN: ")
                if not (new_pin.isdigit() and len(new_pin) == 4):
                    print("\n❌ New PIN must be 4 digits\n")
                elif int(new_pin) == old_pin:
                    print("\n❌ New PIN cannot be the same as old PIN\n")
                else:
                    pin = int(new_pin)
                    print("\n✅ PIN changed successfully\n")

        elif choice == "5":
            print("\nThank you for using Kashan Bank ATM. Goodbye!\n")
            break

        else:
            print("\n❌ Invalid option. Please try again.\n")

else:
    print("\n❌ Wrong PIN. Access blocked.\n")