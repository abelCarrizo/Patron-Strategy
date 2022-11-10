from abc import ABC, abstractmethod
from datetime import date


#Clase contexto
class Cliente():
    @abstractmethod
    def pagar(self):
        pass

#Clase abstracta Strategy()
class MedioPago(ABC):
    @abstractmethod
    def pagar(self):
        pass

#Estrategias concretas (Subclases)
class Tarjeta(MedioPago):
    
    def __init__(self, nombre:str, numeroTarjeta:int ,cvv:int ,expiracion:date):
        self._nombre = nombre
        self._numeroTarjeta = numeroTarjeta
        self._cvv = cvv
        self._expiracion = expiracion
    
    #Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def numeroTarjeta(self, numeroTarjeta):
        return self._numeroTarjeta

    @numeroTarjeta.setter
    def numeroTarjeta(self, numeroTarjeta):
        self._numeroTarjeta = numeroTarjeta

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        self._cvv = cvv

    @property
    def expiracion(self):
        return self._expiracion

    @expiracion.setter
    def expiracion(self, expiracion):
        self._expiracion = expiracion

    def verficar_tarjeta(self,nombre,expiracion,cvv,estado):
        #Si el ESTADO de la tarjeta esa habilitada, se genera el pago
        #asigna los valores de la tarjeta ingresados
        if estado == True:

            self.nombre = nombre
            self.expiracion = expiracion
            self.cvv = cvv

            self.pagar()
        

    def pagar(self,pagar):
        pagar = self.conectar_posnet()
        return pagar

    def conectar_posnet(self):
        pass

class Monedero(MedioPago):
    def __init__(self,nombre = str,codigo = str,divisa = str,mail = str):
        self._nombre = nombre
        self._codigo = codigo
        self._divisa = divisa
        self._mail = mail

    
    #Getters y Setters
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre


    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def divisa(self):
        return self._divisa

    @divisa.setter
    def divisa(self, divisa):
        self._divisa = divisa

    @property
    def mail(self):
        return self._mail

    @codigo.setter
    def mail(self, mail):
        self._mail = mail


    def verificar_entidad(self,nombre,codigo,divisa,mail=None,estado=None):
        if estado == True:

            self._nombre = nombre
            self._codigo = codigo
            self._divisa = divisa
            self._mail = mail


            self.pagar()

    def pagar(self):
        pagar = self.verificar_entidad()
        return pagar
            
class Efectivo(MedioPago): 
    
    def abrir_caja_registradora(self):
        pass

    def pagar(self):
        
        self.abrir_caja_registradora()



