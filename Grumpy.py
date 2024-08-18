def maxSatisfied(customers, grumpy, minute):
    happy_customer = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
    additional_happy_customer = sum(
        customers[i] for i in range(minute) if grumpy[i] == 1
    )
    max_happy_customer = additional_happy_customer
    for i in range(minutes, len(customers)):
        if grumpy[i] == 1:
            additional_happy_customer += customers[i]
        if grumpy[i - minute] == 1:
            additional_happy_customer -= customers[i - minute]
        max_happy_customer = max(additional_happy_customer, max_happy_customer)

    return max_happy_customer + happy_customer


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
print(maxSatisfied(customers, grumpy, minutes))
