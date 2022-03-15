


def next_prime(n):
    i = n + 1
    while True:
        if is_prime(i):
            return i
        i += 1
    

# sprawdza czy liczba jest pierwsza
def is_prime(n) -> bool:
    i = 2
    # sprawdza po kolei dla wszystkich liczb mniejszych
    while i < n:
        # czy n jest podzielne przez i
        if n%i == 0:
            # daje fałsz i kończy działanie
            return False
        i+=1
    # skończyło rekurencję bez wyrzucenia fałszu - jest pierwsza, daje prawdę
    return True



print(next_prime(2135))