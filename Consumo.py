import requests, colorama, sys, time
from datetime import datetime
from colorama import Fore, Style

colorama.init()

def slowprint(s):  # SLOW TEXT
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./500)

logo = """
  _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
"""

slowprint(colorama.Fore.GREEN + logo)

# Pregunta al usuario el nombre del dispositivo y los Watts que consume
print("")
watts = int(input(Fore.RED + "¿ CUANTOS WATTS CONSUME EL DISPOSITIVO?: " + Style.RESET_ALL))

# Transforma los Watts a kW
kwh = watts / 1000

# Consulta el precio de la luz
response = requests.get("https://api.preciodelaluz.org/v1/prices/now?zone=PCB")
price = response.json()["price"] / 1000

# Pregunta al usuario cuántas horas ha estado funcionando el dispositivo
print("")
hours_used = int(input(Fore.RED + "¿CUANTAS HORAS ESTA EN FUNCIONAMIENTO ?: " + Style.RESET_ALL))

# Calcula el precio que ha consumido el dispositivo
total_price = price * kwh * hours_used

print("")
print(Fore.GREEN + "----------------------------------------------" + Style.RESET_ALL)
print(f"PRECIO LUZ {Fore.GREEN}{round(price, 5)} €/kWh {Style.RESET_ALL}")

# Calcula el precio que ha consumido el dispositivo en un día
daily_price = total_price
print(Fore.GREEN + "----------------------------------------------" + Style.RESET_ALL)
print("")
print(f"AL DÍA CONSUME {Fore.GREEN}{round(daily_price, 4)} €{Style.RESET_ALL}")

# Calcula el precio que ha consumido el dispositivo en un mes
now = datetime.now()
month = now.month
if month == 2:
    monthly_price = daily_price * 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    monthly_price = daily_price * 30
else:
    monthly_price = daily_price * 31

print("")
print(f"AL MES CONSUME {Fore.GREEN}{round(monthly_price, 4)} €{Style.RESET_ALL}")

# Calcula el precio que ha consumido el dispositivo en un año
annual_price = monthly_price * 12
print("")
print(f"AL AÑO CONSUME {Fore.GREEN}{round(annual_price, 4)} €{Style.RESET_ALL}")
print("")
print(Fore.GREEN + "----------------------------------------------" + Style.RESET_ALL)
