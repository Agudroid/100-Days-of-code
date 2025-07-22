def calculate_bill(bill: float, tip: int, num_person:int) -> float:
    total_pay = bill * (float(tip)/100) + 1
    pay_per_person = total_pay/5
    return pay_per_person

if __name__ == "__main__":
    print("Welcome to the tip calculator!")
    total_bill = float(input("What was the total bill?"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
    num_person = int(input("How many people to split the bill? "))
    result = calculate_bill(total_bill, tip, num_person)
    result = float("{:.2f}".format(result))
    print(f"Each person should pay: ${result}")