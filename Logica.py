class Procesos:
    def __init__(self, valor = 0.0, porcentaje = 0.0, monto_cuota = 0.0, total = 0.0, cant_cuota = 0.0,):
        self.valor = valor
        self.porcentaje = porcentaje
        self.monto_cuota = monto_cuota
        self.total = total
        self.cant_cuota = cant_cuota
    
    def calcular_cuota(self): #sabemos el valor total con intereces de cuotas
        self.total = self.valor + (self.valor * self.porcentaje / 100)
    
    def valor_cuota(self):
        if self.cant_cuota !=0: #evita errores si por error se divide por cero
            self.monto_cuota = self.total / self.cant_cuota
        else:
            self.monto_cuota = 0.0

    # Métodos getter y setter (no son tan comunes en Python, pero se implementan aquí para mantener el diseño original).
    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_porcentaje(self):
        return self.porcentaje

    def set_porcentaje(self, porcentaje):
        self.porcentaje = porcentaje

    def get_monto_cuota(self):
        return self.monto_cuota

    def set_monto_cuota(self, monto_cuota):
        self.monto_cuota = monto_cuota

    def get_total(self):
        return self.total

    def set_total(self, total):
        self.total = total

    def get_cant_cuota(self):
        return self.cant_cuota

    def set_cant_cuota(self, cant_cuota):
        self.cant_cuota = cant_cuota