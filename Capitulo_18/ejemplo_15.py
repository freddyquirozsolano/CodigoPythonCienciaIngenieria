# Cálculo simbólico con SymPy
import sympy as sp

# Definir símbolos
x, y, t = sp.symbols('x y t')
E, I, w = sp.symbols('E I w', positive=True, real=True)

print("=== CÁLCULO DE VIGAS ===")
# Ecuación de deflexión de viga
# Viga simplemente apoyada con carga uniforme
L = sp.Symbol('L', positive=True)
deflexion = (w * x**2 * (L - x)**2) / (24 * E * I)

print(f"Deflexión: {deflexion}")

# Derivada (pendiente)
pendiente = sp.diff(deflexion, x)
print(f"\nPendiente: {sp.simplify(pendiente)}")

# Punto de máxima deflexión (derivada = 0)
punto_critico = sp.solve(pendiente, x)
print(f"Punto de máxima deflexión: x = {punto_critico}")

print("\n=== CINEMÁTICA ===")
# Posición, velocidad y aceleración
posicion = t**3 - 6*t**2 + 9*t
velocidad = sp.diff(posicion, t)
aceleracion = sp.diff(velocidad, t)

print(f"Posición: s(t) = {posicion}")
print(f"Velocidad: v(t) = {velocidad}")
print(f"Aceleración: a(t) = {aceleracion}")

# Cuando la velocidad es cero
t_reposo = sp.solve(velocidad, t)
print(f"Velocidad = 0 cuando t = {t_reposo}")

print("\n=== ECUACIONES ===")
# Resolver sistema de ecuaciones
# x + y = 5
# 2x - y = 1
ecuaciones = [x + y - 5, 2*x - y - 1]
solucion = sp.solve(ecuaciones, [x, y])
print(f"Solución: {solucion}")

# Integral definida
print("\n=== INTEGRALES ===")
funcion = x**2 + 2*x + 1
integral_indefinida = sp.integrate(funcion, x)
integral_definida = sp.integrate(funcion, (x, 0, 2))
print(f"∫({funcion})dx = {integral_indefinida}")
print(f"∫[0,2]({funcion})dx = {integral_definida}")