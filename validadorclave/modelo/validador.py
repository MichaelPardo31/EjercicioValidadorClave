# TODO: Implementa el código del ejercicio aquí

from errores import (
    LongitudInvalidaError,
    FaltaMayusculaError,
    FaltaMinusculaError,
    FaltaNumeroError,
    FaltaCaracterEspecialError,
    FaltaCalistoError
)
from abc import ABC, abstractmethod
import re

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(x.isupper() for x in clave)

    def _contiene_minuscula(self, clave):
        return any(x.islower() for x in clave)

    def _contiene_numero(self, clave):
        return any(x.isdigit() for x in clave)
    
class ReglaValidacionGanimedes(ReglaValidacion):
     
     def contiene_caracter_especial(self, clave):
        return any(char in "@_#$%" for char in clave)
     
     def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise LongitudInvalidaError("La clave no cumple con la longitud mínima requerida.")
        if not self._contiene_mayuscula(clave):
            raise FaltaMayusculaError("La clave debe contener al menos una letra mayúscula.")
        if not self._contiene_minuscula(clave):
            raise FaltaMinusculaError("La clave debe contener al menos una letra minúscula.")
        if not self._contiene_numero(clave):
            raise FaltaNumeroError("La clave debe contener al menos un número.")
        if not self.contiene_caracter_especial(clave):
            raise FaltaCaracterEspecialError("La clave debe contener al menos un carácter especial.")
        return True
     
     class ReglaValidacionCalisto(ReglaValidacion):
         pass
     
class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)
     
     
