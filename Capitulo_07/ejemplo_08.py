# Pacientes que tomaron medicamento A
medicamento_a = {'Juan', 'María', 'Carlos', 'Ana'}

# Pacientes que tomaron medicamento B
medicamento_b = {'María', 'Pedro', 'Ana', 'Luis'}

# UNIÓN: pacientes que tomaron A o B (o ambos)
ambos = medicamento_a | medicamento_b
# O usando método: medicamento_a.union(medicamento_b)
print(ambos)  # {'Juan', 'María', 'Carlos', 'Ana', 'Pedro', 'Luis'}

# INTERSECCIÓN: pacientes que tomaron A y B
comun = medicamento_a & medicamento_b
# O usando método: medicamento_a.intersection(medicamento_b)
print(comun)  # {'María', 'Ana'}

# DIFERENCIA: pacientes que tomaron A pero no B
solo_a = medicamento_a - medicamento_b
# O usando método: medicamento_a.difference(medicamento_b)
print(solo_a)  # {'Juan', 'Carlos'}

# DIFERENCIA SIMÉTRICA: pacientes que tomaron A o B, pero no ambos
solo_uno = medicamento_a ^ medicamento_b
# O usando método: medicamento_a.symmetric_difference(medicamento_b)
print(solo_uno)  # {'Juan', 'Carlos', 'Pedro', 'Luis'}
