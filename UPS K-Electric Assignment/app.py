k_electric = input("Electricity is available? Reply with yes or no: ").strip().lower()

# Logic
if k_electric in ["yes", "y"]:
    ups = "no ups"  # UPS will not work if electricity is available
    print("Electricity is available, UPS is off.")
elif k_electric in ["no", "n"]:
    ups = "ups working"  # UPS will work if electricity is not available
    print("Electricity is not available, UPS is working.")
else:
    print("Invalid input, please reply with 'yes' or 'no'.")
