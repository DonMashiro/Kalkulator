import logging
logging.basicConfig(level=logging.INFO)
def pobierz_liczby():
    number_1 = float(input("Podaj składnik 1: "))
    number_2 = float(input("Podaj składnik 2: "))
    logging.info(f"Składniki: {number_1}, {number_2}")
    return number_1, number_2

def dodawanie(number_1, number_2):
    result = number_1 + number_2
    logging.info(f"Dodaję {number_1} i {number_2}")
    return result

def odejmowanie(number_1, number_2):
    result = number_1 - number_2
    logging.info(f"Odejmuję {number_1} od {number_2}")
    return result

def mnozenie(number_1, number_2):
    result = number_1 * number_2
    logging.info(f"Mnożę {number_1} przez {number_2}")
    return result

def dzielenie(number_1, number_2):
    if number_2 == 0:
        print("Nie można dzielić przez zero!")
        return None
    result = number_1 / number_2
    logging.info(f"Dzielę {number_1} przez {number_2}")
    return result

def kalkulator():
    operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    number_1, number_2 = pobierz_liczby()
    if operation == 1:
        result = dodawanie(number_1, number_2)
    elif operation == 2:
        result = odejmowanie(number_1, number_2)
    elif operation == 3:
        result = mnozenie(number_1, number_2)
    elif operation == 4:
        result = dzielenie(number_1, number_2)
    else:
        print("Niepoprawny wybór działania.")
        return
    if result is not None:
        print(f"Wynik to {result}")

if __name__ == "__main__":
    kalkulator()
