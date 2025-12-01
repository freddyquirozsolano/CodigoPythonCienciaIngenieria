class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular  # Público
        self._numero_cuenta = self._generar_numero()  # Protegido
        self.__saldo = saldo_inicial  # Privado
        self.__historial = []  # Privado
    
    def _generar_numero(self):
        """Método protegido (uso interno)"""
        import random
        return f"CTA-{random.randint(10000, 99999)}"
    
    def depositar(self, monto):
        """Método público"""
        if monto > 0:
            self.__saldo += monto
            self.__registrar_transaccion("Depósito", monto)
            return True
        return False
    
    def retirar(self, monto):
        """Método público"""
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            self.__registrar_transaccion("Retiro", -monto)
            return True
        return False
    
    def __registrar_transaccion(self, tipo, monto):
        """Método privado (solo uso interno)"""
        from datetime import datetime
        self.__historial.append({
            'tipo': tipo,
            'monto': monto,
            'fecha': datetime.now()
        })
    
    def get_saldo(self):
        """Getter para saldo (acceso controlado)"""
        return self.__saldo
    
    def get_historial(self):
        """Getter para historial (copia, no original)"""
        return self.__historial.copy()
    
    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.__saldo:.2f}"

# Uso correcto
cuenta = CuentaBancaria("María López", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.get_saldo())  # Acceso controlado: 1300
print(cuenta)  # Usa __str__

# ❌ Esto no debería hacerse (pero Python lo permite)
# print(cuenta.__saldo)  # AttributeError
# print(cuenta._CuentaBancaria__saldo)  # Name mangling – evitar