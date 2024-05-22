# Escriba una función en Python que lea un archivo de texto 
# y cuente el número de direcciones de correo electrónico válidas. 
# Use expresiones regulares para identificar las direcciones de correo electrónico.

import re

def count_email(archivo):
    with open(archivo, 'r') as f:
        content = f.read()

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    match = re.findall(regex, content)
    return len(match)
