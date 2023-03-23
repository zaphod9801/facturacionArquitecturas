from enum import Enum


class TransaccionType(str, Enum):
    SALIDA = 'Salida'
    ENTRADA = 'Entrada'
