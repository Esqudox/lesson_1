proceeds = int(input('Введите выручку - '))
costs = int(input('Введите издержки - '))
if costs < proceeds:
    profit = proceeds - costs
    print(f'\nПоздравляем! Ваша прибыль составила - {profit}')
    rent = ((proceeds - costs) / proceeds) * 100
    print(f'\nРентабельность выручки - {rent} процентов')
    staff = int(input('\nКакое количество сотрудников работает у вас? - '))
    staff_profit = (proceeds - costs) / staff
    print(f'\nПрибыль на каждого сотрудника - {staff_profit}')
elif proceeds == costs:
    print('\nВы работаете в ноль, уже не плохо!')
else:
    print('\nВы работаете в убыток. Не переживайте, скоро все наладится.')

