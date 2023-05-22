sallary = input("Введите сумму вашей ЗП:")
credit = input("Введите сумму платежа по кредиту:")
communal = input("Ваша задолженность за коммунальные услуги:")

balance = sallary - credit - communal

print("У вас осталось:", balance, "тг.")
