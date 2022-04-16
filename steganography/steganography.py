import sys
from PIL import Image as img
from sympy import ceiling

class Too_short_file(Exception):
    pass


class Point:
    def __init__(self, x, y, c) -> None:
        self.x = int(x)
        self.y = int(y)
        self.c = int(c)
    def go_one_color_back(self, borders):
        if self.c != 0:
            self.c -= 1
        else: 
            self.c = 2
            if self.x != 0:
                self.x -= 1
            else:
                self.x = borders[0] - 1
                if self.y != 0:
                    self.y -=1
                else:
                    print('bi bop Nie można wracać z zerowego pixela trrrt')


class Symbol:
    def __init__(self, bits) -> None:
        self.binary = ''
        for bit in bits:
            self.binary += str(bit)
    def return_symbol(self):
        return chr(int(self.binary, base=2))


class PixelRow:
    def __init__(self, row) -> None:
        self.row = row
    def get_first(self):
        a = self.row[0]
        self.row.remove(a)
        return a


# zamienia listę metod przyzywania pomocy na słowo
def verbalise_help_commands(commands):
    txt = ''
    for h in commands:
        txt = txt.__add__(h + ', ')
    return txt.removesuffix(', ')


# komenda wywoływana kiedy wystąpiły złe argumenty wywołania albo użyto -h --help
def help_info():
    with open('help_message.txt', 'r', encoding="utf-8") as f:
        print(f.read())


# zamienia str - listę znaków na listę odpowiadającym im kodom binarnym
def binarise(line):
    encoded = []
    for char in line:
        encoded.append(bin(ord(char)).removeprefix('0b'))
    return encoded


# głowna funkcja zakodowania wiadomości
def encode_message(message, input, output):
    try:
        # odczytuje wiadomość z pliku
        with open(message, 'r', encoding="ascii") as f:
            encoding_machine_go_brr(f.readlines(), input, output)
    except UnicodeDecodeError:
        print('W pliku jest niedozwolony znak, który nie ma kody ASCII')
    except:
        print('Wystąpił błąd')  


# zakodowuje linie z odczytanego tekstu
def encoding_machine_go_brr(lines, input, output):
    print('trrrt Tekst odczytany bip bip')
    # zawiera informacje o aktualnym miejscu pixela odczytywanego
    # pierwsze miejsce - x miejsce pixela w macierzy (0-(im.size[0]-1))
    # drugie miejsce - y miejsce pixela w macierzy (0-(im.size[1]-1))
    # trzecie miejsce - numer aktualnego koloru (0-2)
    point = Point(0,0,0)
    try:
        im = img.open(input)
        borders = im.size
        pixels_needed = ceiling(sum([len(l) for l in lines]))
        file_size = borders[0]*borders[1]
        if pixels_needed > file_size:
            raise Too_short_file
    except Too_short_file:
        print('Plik jest za mały, by zakodować tą wiadomość!')
    except:
        print('Coś poszło nie tak we wczytywaniu pliku :c')
    else:
        print('Bip ba bup -- obrazek wczytany, zaczynam kodować tekst -- trrryt')
        # wybiera kolejne linie tekstu
        for line in lines:
            # zakodowuje linię wraz ze spacją i zapisuje w liście
            point, im = encode_line(line, point, im, borders)
        # skończył wszystkie linie, postaw 0 na końcu
        point.go_one_color_back(borders)
        coordinates = point.x, point.y
        px = im.getpixel(coordinates)
        # changes it to list because tuples, that's why
        px = [px[0], px[1], px[2]]
        px[point.c] = 0
        # bruh, tuples again
        px = (px[0], px[1], px[2])
        im.putpixel(coordinates, px)
        im.save(output)
        print('bip bap bup Obrazek zakodowany i zapisany. Dziękuję za współpracę trrrt wshoooooow')


def encode_line(line, _point, im, borders):
    point = _point
    # data of binarised info to encode
    bin = binarise(line)
    # sets coordinates
    coordinates = point.x, point.y
    # sets current color processed
    c = point.c
    # gets pixel to process
    px = im.getpixel(coordinates)
    # changes it to list because tuples, that's why
    px = [px[0], px[1], px[2]]
    # starts itering next letters in a word
    for symbol in bin:
        while len(symbol) != 7:
            symbol = '0' + symbol
        # starts itering in following bits in symbol binary code
        for bit in symbol:
            # current color processed
            b = px[c]
            # changes last bit of data and saves it
            if int(bit) == 1:
                px[c] = b | 1
            else:
                px[c] = b & ~1
            # sets processing to next color
            c += 1
            # point out of ranges
            if c == 3:
                # bruh, tuples again
                px = (px[0], px[1], px[2])
                # puts fully processed pixel
                im.putpixel(coordinates, px)
                # gets next x point
                point.x += 1
                # sets color to 0 for next point
                c = 0
                # checks if point is in x bounds
                if point.x == borders[0]:
                    # sets x position to 0
                    point.x = 0
                    # gets to next y row
                    point.y += 1
                # sets new coordinates after changing pixel and gets a new pixel
                coordinates = point.x, point.y
                px = im.getpixel(coordinates)
                px = [px[0], px[1], px[2]]
        # ends symbol marking, same as before, but places 1
        # current color processed
        b = px[c]
        # changes last bit of data and saves it
        px[c] = b | 1
        # sets processing to next color
        c += 1
        # point out ranges
        if c == 3:
            # changes back to tuple, because it doesn't like lists
            px = (px[0], px[1], px[2])
            # puts fully processed pixel
            im.putpixel(coordinates, px)
            # gets next x point
            point.x += 1
            # sets color to 0 for next point
            c = 0
            # checks if point is in x bounds
            if point.x == borders[0]:
                # sets x position to 0
                point.x = 0
                # gets to next y row
                point.y += 1
            # sets new coordinates after changing pixel and gets a new pixel
            coordinates = point.x, point.y
            px = im.getpixel(coordinates)
            px = [px[0], px[1], px[2]]
    if c != 0:
        # changes back to tuple, because it doesn't like lists
        px = (px[0], px[1], px[2])
        im.putpixel(coordinates, px)
    point.c = c
    return point, im


def get_LSB(pixel):
    # returns LSB of the pixel
    return [pixel[0] & 1, pixel[1] & 1, pixel[2] & 1]


def decode_message(input, text_file):
    file = open(text_file, 'w')
    im = img.open(input)
    row_num = 0
    size_x = im.size[0]
    size_y = im.size[1]
    px_row = PixelRow([im.getpixel((x, row_num)) for x in range(size_x)])
    row_num += 1
    bl = True
    while bl:
        # pixels list
        px = []
        # load 8 pixels -- equivalent of 3 symbols
        for i in range(8):
            # check if row in not empty
            if len(px_row.row) == 0:
                # gets next row
                px_row = PixelRow([im.getpixel((x, row_num)) for x in range(size_x)])
                row_num += 1
                if row_num == size_y:
                    print('Brrt plik jest źle zakodowany i się nie kończy pprt')
                    bl = False
                    break
            px.append(px_row.get_first())

        bits = []
        for p in px:
            bits.extend(get_LSB(p))

        ## first symbol ##
        sym = Symbol(bits[:7])
        file.write(sym.return_symbol())
        # check for bit wether to read further or stop
        if int(bits[7]) == 0:
            # end the file reading
            bl = False
            break

        ## second symbol ##
        sym = Symbol(bits[8:15])
        file.write(sym.return_symbol())
        # check for bit wether to read further or stop
        if int(bits[15]) == 0:
            # end the file reading
            bl = False
            break

        ## third symbol ##
        sym = Symbol(bits[16:-1])
        file.write(sym.return_symbol())
        # check for bit wether to read further or stop
        if int(bits[-1]) == 0:
            # end the file reading
            bl = False
    file.close()
    print('Dekodowanie skończone, plik zapisany')
    return 

# listy przywołania pomocy działania pliku
help_commands = ['-h', '-help', '--help', '/?']


try:
    args = sys.argv[1:]
    run_type = args[0]
except:
    print('Nie podano argumentów!')
else:
    if len(args) != 0:
        if run_type == 'encode':
            message = args[1]
            input = args[2]
            output = args[3]
            encode_message(message, input, output)
        elif run_type == 'decode':
            input = args[1]
            output = args[2]
            decode_message(input, output)
        elif help_commands.__contains__(run_type):
            help_info()
        else:
            print(f'\nNieznana komenda \'{run_type}\'. Skorzystaj z komend: encode,'+
    f' decode lub wpisz {verbalise_help_commands(help_commands)} by otrzymać instrukcję.\n')