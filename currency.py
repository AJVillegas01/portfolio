pesos = int(input('What do you have left in pesos?  '))
soles = int(input('What do you have left in soles?  '))
reais = int(input('What do you have left in reais?  '))
dolar_from_pesos = 0.056 * pesos 
dolar_from_soles = 0.260 * soles
dolar_from_reais = 0.200 * reais
dolar_total = (dolar_from_pesos + dolar_from_soles + dolar_from_reais)

dolar_total_formatted = "{:.2f}".format(dolar_total)
print("Your total currency in dolar is: ", dolar_total_formatted, "$")

#We can get two decimals in other way
formatted_cantidad_dinero = f"{dolar_total:.2f}"
print("The amounth is", formatted_cantidad_dinero, "$")