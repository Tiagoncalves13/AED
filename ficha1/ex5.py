segundos = int(input("Digite um número de segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f"{segundos} segundos = {horas} horas, {minutos} minutos, {segundos_restantes} segundos")
