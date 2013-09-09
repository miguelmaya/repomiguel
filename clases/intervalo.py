# -*- coding: utf-8 -*-

class Intervalo(object):
    """
Se define la clase 'Intervalo', y los métodos para la aritmética básica de intervalos,
es decir, suma, resta, multiplicación y división. Se incluyen otras funciones
que serán útiles.
"""
    def __init__(self,lo,hi=None):
        """
Definimos las propiedades del objeto Intervalo a partir de sus bordes,
lo y hi, donde lo <= hi. En el caso en que el intervalo sólo tenga
un número, éste se interpreta como un intervalo 'delgado' o 'degenerado'.
"""
        if hi is None:
            hi = lo
        elif (hi < lo):
            lo, hi = hi, lo
        
        self.lo = lo
        self.hi = hi
        
    def __repr__(self):
        return "Intervalo [{},{}]".format(self.lo,self.hi)
    
    def __str__(self):
        # Esta función sirve con 'print'
        return "[{},{}]".format(self.lo,self.hi)

    def _repr_html_(self):
        return "[{}, {}]".format(self.lo, self.hi)
    
    def _repr_latex_(self):
        return "$[{}, {}]$".format(self.lo, self.hi)

    # Aquí vienen las operaciones aritméticas
    def __add__(self, otro):
        """
Suma de intervalos
"""
        try:
            return Intervalo(self.lo + otro.lo, self.hi + otro.hi)
        except:
            return self + Intervalo(otro)

    def __radd__(self, otro):
        return self + otro
        
    def __mul__(self, otro):
        try:
            S=[self.lo*otro.lo , self.lo * otro.hi , self.hi * otro.lo , self.hi * otro.hi ]
            return Intervalo( min(S), max(S) )
        except:
            return self * Intervalo(otro)

    def __rmul__(self, otro):
        return self * otro

    # Esta es la funcion igualdad para intervalos
    
    def __eq__(self, otro):
        """
        función igualdad para int6ervalos 

        """
        try:
            if self.lo == otro.lo and self.hi == otro.hi:
                return True
            else:
                return False
        except:
            if self.lo == Intervalo(otro).lo and self.hi == Intervalo(otro).hi:
                return True
            else:
                return False
  

    #interseccion
    def __and__(self, otro):
        """
        Intersección de intervalos
        Funciona con la sintaxis &, (como el AND bitwise)
        """
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)
        if (self.lo > otro.hi) | (self.hi < otro.lo):
            return None
        else:
            a = max( self.lo, otro.lo )
            b = min( self.hi, otro.hi )
            return Intervalo(a,b)
    
    #interseccion por la izquierda
    def __rand__(self, otro):
        """
        Interseccion de intervalos (por la izquierda)
        """
        return self & otro
    
    #negativo del intervalo
    def __neg__(self):
        """
        Devuelve el valor negativo del intervalo
        """
        return Intervalo(-self.hi, -self.lo)
        
    def __div__(self, otro):
        if otro.lo <= 0 <= otro.hi:
            raise ZeroDivisionError
        else:
            return Intervalo.__mul__(self,Intervalo(1./(otro.hi),1./(otro.lo)))

    def middle(self):
        '''
Calcula el punto medio del intervalo
'''
        return (self.lo+self.hi)/2
        
    def radio(self):
        '''
Calcula el radio del intervalo
'''
        return (self.hi-self.lo)/2
        
    def width(self):
        '''
Cacula la anchura
'''
        return self.hi-self.lo
        
    def Abs(self):
        
        return max([abs(self.lo),abs(self.hi)])

