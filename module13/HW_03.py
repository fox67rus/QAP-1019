# ЗАДАНИЕ 13.8.19 (HW-03)

total_cost = 0
number_of_tickets = int(input("Введите количество билетов, которое вы хотите приобрести: "))

for visitor in range(1, number_of_tickets + 1):
    visitor_age = int(input(f"Введите возраст {visitor}-го посетителя: "))
    if visitor_age < 18:
        continue
    elif 18 <= visitor_age < 25:
        total_cost += 990
    else:
        total_cost += 1390

total_cost = int(total_cost * 0.9 if number_of_tickets > 3 else total_cost)
print(f'Сумма к оплате: {total_cost} рублей.')
