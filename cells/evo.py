import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm

class WrongValue(Exception):
    pass

def dec_to_other(num, system=3, list_length=27):
    ls = []
    for i in range(list_length):
        ls.append(num % system)
        num = num // system
    return ls[::-1]


def evolution(steps, initial_state, function):
    n = steps
    s0 = initial_state
    f = function
    state = [s0]
    list_tri = dec_to_other(f, 3, 27)
    size = len(s0)

    def evolve(L, C, R):
        nr = 9 * L + 3 * C + R      # konwercja do dziesiętnego
        h = list_tri[::-1]
        return h[nr]     # znowu odwracamy, bo cyfry są numerowane od prawej do lewej


    for t in range(n):
        s = []              # zmienna pomocnicza, do której zapisujemy nowe stany
        for x in range(size):
            s.append(evolve(state[t][x-1], state[t][x], state[t][(x+1) % size]))      # ilość automatów
        state.append(s)

    return state        # pytanie jest jeszcze o zwrot czasu, danie w tym miejscu "state[::-1]"
                        # odwróci wykres, lecz nie odróci osi przez co źle wygląda


def visualise_data(data):
    # colormap
    trimap = ListedColormap(['white', 'red', 'blue'])

    fig, ax = plt.subplots()
    img = ax.matshow(data, cmap=trimap,vmin=np.min(data) - 0.5, vmax=np.max(data) + 0.5)
    ax.axis(True)
    # make a color bar
    plt.colorbar(img, ticks=[0, 1, 2])
    plt.show()


initial_state_in = input("Proszę podać stan początkowy: ")

# bramka sprawdzająca czy stan jest dobry
try:
    initial_state_ints = [int(b) for b in initial_state_in]
    for a in initial_state_ints:
        if a > 2:
            raise WrongValue
except ValueError:
    print('Zły typ danych! Proszę wpisać ciąg 0, 1 i 2 (np.: 012012201)')
except WrongValue:
    print('Zła wartość w łańcuchu! Proszę wpisać ciąg 0, 1 i 2 (np.: 12000210)')
else:

    steps_in = input("Proszę podać ilość korków: ")

    # bramka sprawdzająca czy liczba kroków jest dobra
    try:
        steps_in = int(steps_in)
        if steps_in < 1:
            raise ValueError
    except ValueError:
        print('Zły typ danych! Proszę podać dodatnią liczbę całkowitą!')
    else:
        function_in = input("proszę podać funkcję zadającą ewolucję automatu: ")

        # bramka sprawdzająca czy funkcja zadająca jest dobra
        try:
            function_in = int(function_in)
            if function_in < 0 or function_in > 762559748498:
                raise ValueError
        except ValueError:
            print('Zły typ danych! Proszę podać liczbę naturalną z zakresu [0, 762559748498]!')
        else:
            # dane próbne do przetestowania:
            # steps_in = "20"
            # initial_state_in = "12212001021012"
            # function_in = "30"

            data = evolution(steps_in, initial_state_ints, int(function_in))
            visualise_data(data)