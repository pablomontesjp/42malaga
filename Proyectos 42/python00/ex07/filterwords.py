
# EX07 - FILTERWORDS.PY #

'''Crea un programa que tome una cadena de texto S y un entero N como argumento, 
e imprima la lista de palabras en S que contengan más 
de N caracteres que no sean de puntuación.'''

import sys
import string

if len(sys.argv) != 3:
    print("ERROR")
    exit()
list_w = sys.argv[1].split()

try:
    len_s = int(sys.argv[2])
except Exception:
    print("ERROR")
    exit()
list_fin = []

for w in list_w:
    w = w.translate(str.maketrans('', '', string.punctuation))
    if len(w) > len_s:
        list_fin.append(w)
print(list_fin)
