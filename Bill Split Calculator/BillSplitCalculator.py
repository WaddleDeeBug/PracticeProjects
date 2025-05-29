print('Bill Split Calculator')
bill_amount = float(input(f'Enter bill amount: '))
tip_percentage = float(input(f'Enter tip percentage from (1-100): '))
amount_of_people = int(input(f'Enter amount of people: '))
tip_amount = (tip_percentage / 100) * bill_amount
total = tip_amount + bill_amount
total_per_person = total / amount_of_people
print(f'Total (including tip): €{total}')
print(f'Each person pays: €{total_per_person}')