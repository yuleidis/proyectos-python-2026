#Estás programando la lógica de fin de mes de una pp de billetera digital.
#Por cada tranferencia completa, la app acumula un cashback de 2.000,
#Pero solo se acredita cada 5 tranferencia realizadas.
#Además, si el total mensual tranferido supera los $200.000,
#Se cobra una comision del 4% sobre el excedente.
# el usuario hizo 13 tranferencias:
# 10 de $18.000
#3 de $25.000
#¿Cuánto cashback recibe y cuánta comisión paga?

total_tranferencias = 18000*10 + 25000 * 3
#18.000 * 10
#25.000 * 3
cashback = (10 + 3) * 2000

print(f"El total de cashback es: { cashback} cop")

cashback_pendiente = (13%5) * 2000

print(f"El cashback pendiente es: {cashback_pendiente}")

cashback_recibido = cashback-cashback_pendiente

print(f"El cashback ya acreditado es de: {cashback_recibido}")

comision = (total_tranferencias-200000) * 0.04

print(f"la comision a pagar es: {comision}")

balance = cashback - comision
print(f"El usuario ganó: {balance}") 

