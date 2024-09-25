import logging
logging.basicConfig(level=logging.INFO)
def calculator():
  operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
  number_1 = float(input("Podaj składnik 1: "))
  number_2 = float(input("Podaj składnik 2: "))
  logging.info(f"Składniki: {number_1}, {number_2}")
  if operation == 1:
    result = number_1 + number_2
    logging.info(f"Dodaję {number_1} i {number_2}")
  elif operation == 2:
    result = number_1 - number_2
    logging.info(f"Odejmuję {number_1} od {number_2}")
  elif operation == 3:
    result = number_1 * number_2
    logging.info(f"Mnożę {number_1} przez {number_2}")
  elif operation == 4:
    result = number_1 / number_2
    logging.info(f"Dzielę {number_1} przez {number_2}")
  else:
    print("Niepoprawny wybór działania.")
    return
  print(f"Wynik to {result}")
calculator()