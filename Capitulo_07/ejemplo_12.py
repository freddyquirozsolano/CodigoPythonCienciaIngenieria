# ==============================================================================
# CAPÍTULO 7 - PROYECTO INTEGRADOR
# Sistema de Gestión de Información
# ==============================================================================

print("=" * 80)
print("           PROYECTO INTEGRADOR - CAPÍTULO 7")
print("           Sistema de Gestión de Información")
print("=" * 80)
print()
print("Selecciona tu área de especialización:")
print("1. 🏥 Biomédica - Sistema de Gestión de Pacientes")
print("2. 🤖 Mecatrónica - Sistema de Gestión de Robots")
print("3. 💻 Sistemas - Sistema de Gestión de Usuarios")
print("4. 🔧 Ingeniería - Sistema de Gestión de Materiales")
print()

area = input("Ingresa el número de tu área (1-4): ")

# ==============================================================================
# 🏥 PROYECTO 1: SISTEMA DE GESTIÓN DE PACIENTES (BIOMÉDICA)
# ==============================================================================

if area == "1":
    print("\n" + "=" * 80)
    print("🏥 SISTEMA DE GESTIÓN DE PACIENTES")
    print("=" * 80)
    
    # Base de datos de pacientes usando diccionarios
    pacientes = {
        'P001': {
            'nombre': 'María López',
            'edad': 45,
            'tipo_sangre': 'O+',
            'alergias': {'penicilina', 'polen'},
            'medicamentos': {'aspirina', 'metformina'},
            'diagnosticos': ['hipertensión', 'diabetes']
        },
        'P002': {
            'nombre': 'Juan Pérez',
            'edad': 32,
            'tipo_sangre': 'A+',
            'alergias': {'penicilina'},
            'medicamentos': {'ibuprofeno'},
            'diagnosticos': ['apendicitis']
        },
        'P003': {
            'nombre': 'Ana García',
            'edad': 28,
            'tipo_sangre': 'B-',
            'alergias': {'mariscos'},
            'medicamentos': {'paracetamol'},
            'diagnosticos': ['asma']
        }
    }
    
    # Medicamentos disponibles en farmacia (set)
    farmacia = {'aspirina', 'paracetamol', 'ibuprofeno', 'metformina', 'amoxicilina'}
    
    continuar = True
    
    while continuar:
        print("\n" + "-" * 60)
        print("MENÚ PRINCIPAL")
        print("-" * 60)
        print("1. Ver lista de pacientes")
        print("2. Buscar paciente por ID")
        print("3. Agregar nuevo paciente")
        print("4. Verificar medicamento para paciente")
        print("5. Análisis de alergias comunes")
        print("6. Buscar pacientes por tipo de sangre")
        print("7. Reporte de medicamentos más usados")
        print("8. Salir")
        print()
        
        opcion = input("Selecciona una opción (1-8): ")
        
        # OPCIÓN 1: Ver lista de pacientes
        if opcion == "1":
            print("\n📋 LISTA DE PACIENTES:")
            print("-" * 60)
            for id_paciente in pacientes:
                print(f"ID: {id_paciente} - {pacientes[id_paciente]['nombre']} "
                      f"({pacientes[id_paciente]['edad']} años)")
        
        # OPCIÓN 2: Buscar paciente por ID
        elif opcion == "2":
            id_buscar = input("\nIngresa el ID del paciente (ej: P001): ").upper()
            
            if id_buscar in pacientes:
                p = pacientes[id_buscar]
                print(f"\n✓ Paciente encontrado:")
                print(f"   Nombre: {p['nombre']}")
                print(f"   Edad: {p['edad']} años")
                print(f"   Tipo de sangre: {p['tipo_sangre']}")
                print(f"   Alergias: {', '.join(p['alergias']) if p['alergias'] else 'Ninguna'}")
                print(f"   Medicamentos actuales: {', '.join(p['medicamentos'])}")
                print(f"   Diagnósticos: {', '.join(p['diagnosticos'])}")
            else:
                print(f"✗ No se encontró paciente con ID: {id_buscar}")
        
        # OPCIÓN 3: Agregar nuevo paciente
        elif opcion == "3":
            print("\n➕ AGREGAR NUEVO PACIENTE")
            print("-" * 60)
            
            nuevo_id = input("ID del nuevo paciente (ej: P004): ").upper()
            
            if nuevo_id in pacientes:
                print(f"✗ Error: Ya existe un paciente con ID {nuevo_id}")
            else:
                nombre = input("Nombre completo: ")
                edad = int(input("Edad: "))
                tipo_sangre = input("Tipo de sangre (ej: O+): ")
                
                # Alergias (convertir input a set)
                alergias_str = input("Alergias (separadas por coma, o Enter si no tiene): ")
                if alergias_str.strip():
                    alergias = set(a.strip() for a in alergias_str.split(','))
                else:
                    alergias = set()
                
                # Medicamentos (convertir input a set)
                medicamentos_str = input("Medicamentos actuales (separados por coma): ")
                if medicamentos_str.strip():
                    medicamentos = set(m.strip() for m in medicamentos_str.split(','))
                else:
                    medicamentos = set()
                
                # Diagnósticos (lista)
                diagnosticos_str = input("Diagnósticos (separados por coma): ")
                if diagnosticos_str.strip():
                    diagnosticos = [d.strip() for d in diagnosticos_str.split(',')]
                else:
                    diagnosticos = []
                
                # Agregar al diccionario
                pacientes[nuevo_id] = {
                    'nombre': nombre,
                    'edad': edad,
                    'tipo_sangre': tipo_sangre,
                    'alergias': alergias,
                    'medicamentos': medicamentos,
                    'diagnosticos': diagnosticos
                }
                
                print(f"\n✓ Paciente {nuevo_id} agregado exitosamente")
        
        # OPCIÓN 4: Verificar medicamento para paciente
        elif opcion == "4":
            print("\n💊 VERIFICAR MEDICAMENTO")
            print("-" * 60)
            
            id_paciente = input("ID del paciente: ").upper()
            
            if id_paciente not in pacientes:
                print(f"✗ No se encontró paciente con ID: {id_paciente}")
            else:
                medicamento = input("Medicamento a verificar: ").lower()
                
                # Verificar si causa alergia
                alergias_paciente = pacientes[id_paciente]['alergias']
                es_alergico = False
                
                for alergia in alergias_paciente:
                    if medicamento.lower() in alergia.lower():
                        es_alergico = True
                        break
                
                if es_alergico:
                    print(f"⚠️ ALERTA: Paciente alérgico a {medicamento}")
                elif medicamento not in farmacia:
                    print(f"⚠️ ADVERTENCIA: {medicamento} no disponible en farmacia")
                else:
                    print(f"✓ {medicamento} es seguro para el paciente")
                    print(f"✓ {medicamento} está disponible en farmacia")
        
        # OPCIÓN 5: Análisis de alergias comunes
        elif opcion == "5":
            print("\n🔍 ANÁLISIS DE ALERGIAS COMUNES")
            print("-" * 60)
            
            # Contar frecuencia de cada alergia
            conteo_alergias = {}
            
            for id_paciente in pacientes:
                alergias_paciente = pacientes[id_paciente]['alergias']
                
                for alergia in alergias_paciente:
                    if alergia in conteo_alergias:
                        conteo_alergias[alergia] = conteo_alergias[alergia] + 1
                    else:
                        conteo_alergias[alergia] = 1
            
            # Ordenar por frecuencia (de mayor a menor)
            # Crear lista de tuplas (alergia, conteo)
            lista_alergias = []
            for alergia in conteo_alergias:
                lista_alergias.append((alergia, conteo_alergias[alergia]))
            
            # Ordenamiento simple por burbuja (sin usar sorted)
            for i in range(len(lista_alergias)):
                for j in range(len(lista_alergias) - 1 - i):
                    if lista_alergias[j][1] < lista_alergias[j + 1][1]:
                        # Intercambiar
                        temp = lista_alergias[j]
                        lista_alergias[j] = lista_alergias[j + 1]
                        lista_alergias[j + 1] = temp
            
            # Mostrar resultados
            print("Alergias más comunes:")
            for alergia, conteo in lista_alergias:
                print(f"   • {alergia}: {conteo} paciente(s)")
        
        # OPCIÓN 6: Buscar por tipo de sangre
        elif opcion == "6":
            print("\n🩸 BUSCAR POR TIPO DE SANGRE")
            print("-" * 60)
            
            tipo_buscar = input("Tipo de sangre a buscar (ej: O+): ")
            
            encontrados = []
            
            for id_paciente in pacientes:
                if pacientes[id_paciente]['tipo_sangre'] == tipo_buscar:
                    encontrados.append(id_paciente)
            
            if encontrados:
                print(f"\nPacientes con tipo de sangre {tipo_buscar}:")
                for id_paciente in encontrados:
                    nombre = pacientes[id_paciente]['nombre']
                    print(f"   • {nombre} (ID: {id_paciente})")
            else:
                print(f"No se encontraron pacientes con tipo de sangre {tipo_buscar}")
        
        # OPCIÓN 7: Reporte de medicamentos más usados
        elif opcion == "7":
            print("\n📊 MEDICAMENTOS MÁS USADOS")
            print("-" * 60)
            
            # Contar medicamentos
            conteo_medicamentos = {}
            
            for id_paciente in pacientes:
                medicamentos_paciente = pacientes[id_paciente]['medicamentos']
                
                for medicamento in medicamentos_paciente:
                    if medicamento in conteo_medicamentos:
                        conteo_medicamentos[medicamento] = conteo_medicamentos[medicamento] + 1
                    else:
                        conteo_medicamentos[medicamento] = 1
            
            # Mostrar resultados
            for medicamento in conteo_medicamentos:
                print(f"   • {medicamento}: {conteo_medicamentos[medicamento]} paciente(s)")
        
        # OPCIÓN 8: Salir
        elif opcion == "8":
            print("\n✓ Saliendo del sistema...")
            continuar = False
        
        else:
            print("\n✗ Opción no válida. Intenta de nuevo.")

# ==============================================================================
# 🤖 PROYECTO 2: SISTEMA DE GESTIÓN DE ROBOTS (MECATRÓNICA)
# ==============================================================================

elif area == "2":
    print("\n" + "=" * 80)
    print("🤖 SISTEMA DE GESTIÓN DE ROBOTS")
    print("=" * 80)
    
    # Base de datos de robots
    robots = {
        'ROBOT-001': {
            'modelo': 'AutoNav-X1',
            'estado': 'operativo',
            'sensores': {'ultrasonico', 'infrarrojo', 'camara'},
            'bateria': 85,
            'posicion': [10, 20]
        },
        'ROBOT-002': {
            'modelo': 'ManipBot-3000',
            'estado': 'operativo',
            'sensores': {'camara', 'tactil', 'fuerza'},
            'bateria': 92,
            'posicion': [0, 0]
        },
        'ROBOT-003': {
            'modelo': 'AutoNav-X1',
            'estado': 'mantenimiento',
            'sensores': {'ultrasonico', 'camara'},
            'bateria': 20,
            'posicion': [5, 15]
        }
    }
    
    continuar = True
    
    while continuar:
        print("\n" + "-" * 60)
        print("MENÚ PRINCIPAL")
        print("-" * 60)
        print("1. Ver lista de robots")
        print("2. Buscar robot por ID")
        print("3. Agregar nuevo robot")
        print("4. Actualizar batería")
        print("5. Alertas de batería baja")
        print("6. Comparar sensores de dos robots")
        print("7. Robots operativos vs en mantenimiento")
        print("8. Sensores más comunes")
        print("9. Salir")
        print()
        
        opcion = input("Selecciona una opción (1-9): ")
        
        # OPCIÓN 1: Ver lista de robots
        if opcion == "1":
            print("\n📋 LISTA DE ROBOTS:")
            print("-" * 60)
            for id_robot in robots:
                r = robots[id_robot]
                print(f"ID: {id_robot} - {r['modelo']} | Estado: {r['estado']} | Batería: {r['bateria']}%")
        
        # OPCIÓN 2: Buscar robot por ID
        elif opcion == "2":
            id_buscar = input("\nIngresa el ID del robot (ej: ROBOT-001): ").upper()
            
            if id_buscar in robots:
                r = robots[id_buscar]
                print(f"\n✓ Robot encontrado:")
                print(f"   Modelo: {r['modelo']}")
                print(f"   Estado: {r['estado']}")
                print(f"   Batería: {r['bateria']}%")
                print(f"   Posición: ({r['posicion'][0]}, {r['posicion'][1]})")
                print(f"   Sensores: {', '.join(r['sensores'])}")
            else:
                print(f"✗ No se encontró robot con ID: {id_buscar}")
        
        # OPCIÓN 3: Agregar nuevo robot
        elif opcion == "3":
            print("\n➕ AGREGAR NUEVO ROBOT")
            print("-" * 60)
            
            nuevo_id = input("ID del nuevo robot (ej: ROBOT-004): ").upper()
            
            if nuevo_id in robots:
                print(f"✗ Error: Ya existe un robot con ID {nuevo_id}")
            else:
                modelo = input("Modelo: ")
                estado = input("Estado (operativo/mantenimiento): ")
                bateria = int(input("Nivel de batería (0-100): "))
                pos_x = int(input("Posición X: "))
                pos_y = int(input("Posición Y: "))
                
                sensores_str = input("Sensores (separados por coma): ")
                sensores = set(s.strip() for s in sensores_str.split(','))
                
                robots[nuevo_id] = {
                    'modelo': modelo,
                    'estado': estado,
                    'sensores': sensores,
                    'bateria': bateria,
                    'posicion': [pos_x, pos_y]
                }
                
                print(f"\n✓ Robot {nuevo_id} agregado exitosamente")
        
        # OPCIÓN 4: Actualizar batería
        elif opcion == "4":
            print("\n🔋 ACTUALIZAR BATERÍA")
            print("-" * 60)
            
            id_robot = input("ID del robot: ").upper()
            
            if id_robot not in robots:
                print(f"✗ No se encontró robot con ID: {id_robot}")
            else:
                nueva_bateria = int(input("Nuevo nivel de batería (0-100): "))
                robots[id_robot]['bateria'] = nueva_bateria
                print(f"✓ Batería de {id_robot} actualizada a {nueva_bateria}%")
        
        # OPCIÓN 5: Alertas de batería baja
        elif opcion == "5":
            print("\n⚠️ ALERTAS DE BATERÍA BAJA (< 30%)")
            print("-" * 60)
            
            alertas = []
            
            for id_robot in robots:
                if robots[id_robot]['bateria'] < 30:
                    alertas.append(id_robot)
            
            if alertas:
                for id_robot in alertas:
                    bateria = robots[id_robot]['bateria']
                    print(f"   ⚠️ {id_robot}: {bateria}% - REQUIERE RECARGA")
            else:
                print("   ✓ Todos los robots tienen batería adecuada")
        
        # OPCIÓN 6: Comparar sensores
        elif opcion == "6":
            print("\n🔍 COMPARAR SENSORES DE DOS ROBOTS")
            print("-" * 60)
            
            id1 = input("ID del primer robot: ").upper()
            id2 = input("ID del segundo robot: ").upper()
            
            if id1 not in robots or id2 not in robots:
                print("✗ Uno o ambos robots no existen")
            else:
                sensores1 = robots[id1]['sensores']
                sensores2 = robots[id2]['sensores']
                
                # Sensores en común (intersección)
                comunes = sensores1 & sensores2
                
                # Sensores únicos
                solo1 = sensores1 - sensores2
                solo2 = sensores2 - sensores1
                
                print(f"\nSensores comunes: {', '.join(comunes) if comunes else 'Ninguno'}")
                print(f"Solo en {id1}: {', '.join(solo1) if solo1 else 'Ninguno'}")
                print(f"Solo en {id2}: {', '.join(solo2) if solo2 else 'Ninguno'}")
        
        # OPCIÓN 7: Robots por estado
        elif opcion == "7":
            print("\n📊 ROBOTS POR ESTADO")
            print("-" * 60)
            
            operativos = []
            mantenimiento = []
            
            for id_robot in robots:
                if robots[id_robot]['estado'] == 'operativo':
                    operativos.append(id_robot)
                else:
                    mantenimiento.append(id_robot)
            
            print(f"Operativos ({len(operativos)}): {', '.join(operativos)}")
            print(f"En mantenimiento ({len(mantenimiento)}): {', '.join(mantenimiento)}")
        
        # OPCIÓN 8: Sensores más comunes
        elif opcion == "8":
            print("\n📊 SENSORES MÁS COMUNES")
            print("-" * 60)
            
            conteo_sensores = {}
            
            for id_robot in robots:
                sensores_robot = robots[id_robot]['sensores']
                
                for sensor in sensores_robot:
                    if sensor in conteo_sensores:
                        conteo_sensores[sensor] = conteo_sensores[sensor] + 1
                    else:
                        conteo_sensores[sensor] = 1
            
            for sensor in conteo_sensores:
                print(f"   • {sensor}: {conteo_sensores[sensor]} robot(s)")
        
        # OPCIÓN 9: Salir
        elif opcion == "9":
            print("\n✓ Saliendo del sistema...")
            continuar = False
        
        else:
            print("\n✗ Opción no válida. Intenta de nuevo.")

# ==============================================================================
# 💻 PROYECTO 3: SISTEMA DE GESTIÓN DE USUARIOS (SISTEMAS)
# ==============================================================================

elif area == "3":
    print("\n" + "=" * 80)
    print("💻 SISTEMA DE GESTIÓN DE USUARIOS")
    print("=" * 80)
    
    # Base de datos de usuarios
    usuarios = {
        'admin001': {
            'nombre': 'Carlos Admin',
            'rol': 'administrador',
            'permisos': {'read', 'write', 'delete', 'admin'},
            'proyectos': ['web_app', 'mobile_app'],
            'activo': True
        },
        'dev001': {
            'nombre': 'María Dev',
            'rol': 'desarrollador',
            'permisos': {'read', 'write'},
            'proyectos': ['web_app', 'api'],
            'activo': True
        },
        'analyst001': {
            'nombre': 'Ana Analista',
            'rol': 'analista',
            'permisos': {'read'},
            'proyectos': ['reporting'],
            'activo': True
        }
    }
    
    continuar = True
    
    while continuar:
        print("\n" + "-" * 60)
        print("MENÚ PRINCIPAL")
        print("-" * 60)
        print("1. Ver lista de usuarios")
        print("2. Buscar usuario")
        print("3. Agregar nuevo usuario")
        print("4. Verificar permiso de usuario")
        print("5. Comparar permisos entre usuarios")
        print("6. Usuarios por rol")
        print("7. Proyectos compartidos")
        print("8. Salir")
        print()
        
        opcion = input("Selecciona una opción (1-8): ")
        
        # OPCIÓN 1: Ver lista de usuarios
        if opcion == "1":
            print("\n📋 LISTA DE USUARIOS:")
            print("-" * 60)
            for id_user in usuarios:
                u = usuarios[id_user]
                estado = "✓ Activo" if u['activo'] else "✗ Inactivo"
                print(f"ID: {id_user} - {u['nombre']} | Rol: {u['rol']} | {estado}")
        
        # OPCIÓN 2: Buscar usuario
        elif opcion == "2":
            id_buscar = input("\nIngresa el ID del usuario: ").lower()
            
            if id_buscar in usuarios:
                u = usuarios[id_buscar]
                print(f"\n✓ Usuario encontrado:")
                print(f"   Nombre: {u['nombre']}")
                print(f"   Rol: {u['rol']}")
                print(f"   Permisos: {', '.join(u['permisos'])}")
                print(f"   Proyectos: {', '.join(u['proyectos'])}")
                print(f"   Estado: {'Activo' if u['activo'] else 'Inactivo'}")
            else:
                print(f"✗ No se encontró usuario con ID: {id_buscar}")
        
        # OPCIÓN 3: Agregar nuevo usuario
        elif opcion == "3":
            print("\n➕ AGREGAR NUEVO USUARIO")
            print("-" * 60)
            
            nuevo_id = input("ID del nuevo usuario (ej: dev002): ").lower()
            
            if nuevo_id in usuarios:
                print(f"✗ Error: Ya existe un usuario con ID {nuevo_id}")
            else:
                nombre = input("Nombre completo: ")
                rol = input("Rol (administrador/desarrollador/analista): ")
                
                permisos_str = input("Permisos (read, write, delete, admin - separados por coma): ")
                permisos = set(p.strip() for p in permisos_str.split(','))
                
                proyectos_str = input("Proyectos (separados por coma): ")
                proyectos = [p.strip() for p in proyectos_str.split(',')]
                
                usuarios[nuevo_id] = {
                    'nombre': nombre,
                    'rol': rol,
                    'permisos': permisos,
                    'proyectos': proyectos,
                    'activo': True
                }
                
                print(f"\n✓ Usuario {nuevo_id} agregado exitosamente")
        
        # OPCIÓN 4: Verificar permiso
        elif opcion == "4":
            print("\n🔐 VERIFICAR PERMISO")
            print("-" * 60)
            
            id_user = input("ID del usuario: ").lower()
            
            if id_user not in usuarios:
                print(f"✗ No se encontró usuario con ID: {id_user}")
            elif not usuarios[id_user]['activo']:
                print(f"✗ El usuario {id_user} está inactivo")
            else:
                permiso = input("Permiso a verificar (read/write/delete/admin): ").lower()
                
                if permiso in usuarios[id_user]['permisos']:
                    print(f"✓ El usuario {id_user} SÍ tiene permiso de '{permiso}'")
                else:
                    print(f"✗ El usuario {id_user} NO tiene permiso de '{permiso}'")
        
        # OPCIÓN 5: Comparar permisos
        elif opcion == "5":
            print("\n🔍 COMPARAR PERMISOS ENTRE USUARIOS")
            print("-" * 60)
            
            id1 = input("ID del primer usuario: ").lower()
            id2 = input("ID del segundo usuario: ").lower()
            
            if id1 not in usuarios or id2 not in usuarios:
                print("✗ Uno o ambos usuarios no existen")
            else:
                permisos1 = usuarios[id1]['permisos']
                permisos2 = usuarios[id2]['permisos']
                
                comunes = permisos1 & permisos2
                solo1 = permisos1 - permisos2
                solo2 = permisos2 - permisos1
                
                print(f"\nPermisos comunes: {', '.join(comunes) if comunes else 'Ninguno'}")
                print(f"Solo {id1}: {', '.join(solo1) if solo1 else 'Ninguno'}")
                print(f"Solo {id2}: {', '.join(solo2) if solo2 else 'Ninguno'}")
        
        # OPCIÓN 6: Usuarios por rol
        elif opcion == "6":
            print("\n📊 USUARIOS POR ROL")
            print("-" * 60)
            
            administradores = []
            desarrolladores = []
            analistas = []
            
            for id_user in usuarios:
                rol = usuarios[id_user]['rol']
                if rol == 'administrador':
                    administradores.append(id_user)
                elif rol == 'desarrollador':
                    desarrolladores.append(id_user)
                elif rol == 'analista':
                    analistas.append(id_user)
            
            print(f"Administradores ({len(administradores)}): {', '.join(administradores)}")
            print(f"Desarrolladores ({len(desarrolladores)}): {', '.join(desarrolladores)}")
            print(f"Analistas ({len(analistas)}): {', '.join(analistas)}")
        
        # OPCIÓN 7: Proyectos compartidos
        elif opcion == "7":
            print("\n🔍 PROYECTOS COMPARTIDOS ENTRE USUARIOS")
            print("-" * 60)
            
            id1 = input("ID del primer usuario: ").lower()
            id2 = input("ID del segundo usuario: ").lower()
            
            if id1 not in usuarios or id2 not in usuarios:
                print("✗ Uno o ambos usuarios no existen")
            else:
                proyectos1 = set(usuarios[id1]['proyectos'])
                proyectos2 = set(usuarios[id2]['proyectos'])
                
                compartidos = proyectos1 & proyectos2
                
                if compartidos:
                    print(f"Proyectos compartidos: {', '.join(compartidos)}")
                else:
                    print("No tienen proyectos en común")
        
        # OPCIÓN 8: Salir
        elif opcion == "8":
            print("\n✓ Saliendo del sistema...")
            continuar = False
        
        else:
            print("\n✗ Opción no válida. Intenta de nuevo.")

# ==============================================================================
# 🔧 PROYECTO 4: SISTEMA DE GESTIÓN DE MATERIALES (INGENIERÍA)
# ==============================================================================

elif area == "4":
    print("\n" + "=" * 80)
    print("🔧 SISTEMA DE GESTIÓN DE MATERIALES")
    print("=" * 80)
    
    # Base de datos de materiales
    materiales = {
        'MAT-001': {
            'nombre': 'Acero A36',
            'resistencia': 250,  # MPa
            'densidad': 7850,    # kg/m³
            'aplicaciones': {'estructuras', 'puentes', 'edificios'},
            'proveedores': {'Aceros Unidos', 'MetalCorp'},
            'stock': 15000,      # kg
            'costo': 0.80        # USD/kg
        },
        'MAT-002': {
            'nombre': 'Aluminio 6061',
            'resistencia': 310,
            'densidad': 2700,
            'aplicaciones': {'aeronautica', 'automotriz'},
            'proveedores': {'AlumCorp', 'MetalCorp'},
            'stock': 8000,
            'costo': 2.50
        },
        'MAT-003': {
            'nombre': 'Concreto fc280',
            'resistencia': 280,
            'densidad': 2400,
            'aplicaciones': {'edificios', 'puentes'},
            'proveedores': {'ConcretoMix'},
            'stock': 50000,
            'costo': 0.12
        }
    }
    
    continuar = True
    
    while continuar:
        print("\n" + "-" * 60)
        print("MENÚ PRINCIPAL")
        print("-" * 60)
        print("1. Ver lista de materiales")
        print("2. Buscar material por ID")
        print("3. Agregar nuevo material")
        print("4. Materiales para aplicación específica")
        print("5. Calcular costo de proyecto")
        print("6. Proveedores comunes")
        print("7. Alertas de stock bajo")
        print("8. Comparar relación resistencia/peso")
        print("9. Salir")
        print()
        
        opcion = input("Selecciona una opción (1-9): ")
        
        # OPCIÓN 1: Ver lista de materiales
        if opcion == "1":
            print("\n📋 LISTA DE MATERIALES:")
            print("-" * 60)
            for id_mat in materiales:
                m = materiales[id_mat]
                print(f"ID: {id_mat} - {m['nombre']} | Stock: {m['stock']} kg | ${m['costo']}/kg")
        
        # OPCIÓN 2: Buscar material
        elif opcion == "2":
            id_buscar = input("\nIngresa el ID del material (ej: MAT-001): ").upper()
            
            if id_buscar in materiales:
                m = materiales[id_buscar]
                print(f"\n✓ Material encontrado:")
                print(f"   Nombre: {m['nombre']}")
                print(f"   Resistencia: {m['resistencia']} MPa")
                print(f"   Densidad: {m['densidad']} kg/m³")
                print(f"   Aplicaciones: {', '.join(m['aplicaciones'])}")
                print(f"   Proveedores: {', '.join(m['proveedores'])}")
                print(f"   Stock: {m['stock']} kg")
                print(f"   Costo: ${m['costo']}/kg")
            else:
                print(f"✗ No se encontró material con ID: {id_buscar}")
        
        # OPCIÓN 3: Agregar nuevo material
        elif opcion == "3":
            print("\n➕ AGREGAR NUEVO MATERIAL")
            print("-" * 60)
            
            nuevo_id = input("ID del nuevo material (ej: MAT-004): ").upper()
            
            if nuevo_id in materiales:
                print(f"✗ Error: Ya existe un material con ID {nuevo_id}")
            else:
                nombre = input("Nombre del material: ")
                resistencia = int(input("Resistencia (MPa): "))
                densidad = int(input("Densidad (kg/m³): "))
                stock = int(input("Stock inicial (kg): "))
                costo = float(input("Costo (USD/kg): "))
                
                aplicaciones_str = input("Aplicaciones (separadas por coma): ")
                aplicaciones = set(a.strip() for a in aplicaciones_str.split(','))
                
                proveedores_str = input("Proveedores (separados por coma): ")
                proveedores = set(p.strip() for p in proveedores_str.split(','))
                
                materiales[nuevo_id] = {
                    'nombre': nombre,
                    'resistencia': resistencia,
                    'densidad': densidad,
                    'aplicaciones': aplicaciones,
                    'proveedores': proveedores,
                    'stock': stock,
                    'costo': costo
                }
                
                print(f"\n✓ Material {nuevo_id} agregado exitosamente")
        
        # OPCIÓN 4: Materiales para aplicación
        elif opcion == "4":
            print("\n🔍 MATERIALES PARA APLICACIÓN ESPECÍFICA")
            print("-" * 60)
            
            aplicacion = input("Aplicación (ej: puentes, edificios): ").lower()
            
            encontrados = []
            
            for id_mat in materiales:
                if aplicacion in materiales[id_mat]['aplicaciones']:
                    encontrados.append(id_mat)
            
            if encontrados:
                print(f"\nMateriales para '{aplicacion}':")
                for id_mat in encontrados:
                    m = materiales[id_mat]
                    print(f"   • {m['nombre']} - Resistencia: {m['resistencia']} MPa")
            else:
                print(f"No se encontraron materiales para '{aplicacion}'")
        
        # OPCIÓN 5: Calcular costo de proyecto
        elif opcion == "5":
            print("\n💰 CALCULAR COSTO DE PROYECTO")
            print("-" * 60)
            
            costo_total = 0
            materiales_proyecto = {}
            
            print("Ingresa los materiales y cantidades para el proyecto")
            print("(Escribe 'fin' cuando termines)")
            
            while True:
                id_mat = input("\nID del material (o 'fin'): ").upper()
                
                if id_mat == 'FIN':
                    break
                
                if id_mat not in materiales:
                    print(f"✗ Material {id_mat} no existe")
                    continue
                
                cantidad = int(input("Cantidad (kg): "))
                materiales_proyecto[id_mat] = cantidad
            
            # Calcular costos
            print("\n" + "-" * 60)
            print("RESUMEN DEL PROYECTO")
            print("-" * 60)
            
            for id_mat in materiales_proyecto:
                cantidad = materiales_proyecto[id_mat]
                m = materiales[id_mat]
                costo = cantidad * m['costo']
                costo_total = costo_total + costo
                
                print(f"{m['nombre']:25} {cantidad:8} kg × ${m['costo']:6.2f}/kg = ${costo:10.2f}")
            
            print("-" * 60)
            print(f"{'COSTO TOTAL':25} {' ':18} ${costo_total:10.2f}")
        
        # OPCIÓN 6: Proveedores comunes
        elif opcion == "6":
            print("\n🔍 PROVEEDORES COMUNES ENTRE DOS MATERIALES")
            print("-" * 60)
            
            id1 = input("ID del primer material: ").upper()
            id2 = input("ID del segundo material: ").upper()
            
            if id1 not in materiales or id2 not in materiales:
                print("✗ Uno o ambos materiales no existen")
            else:
                prov1 = materiales[id1]['proveedores']
                prov2 = materiales[id2]['proveedores']
                
                comunes = prov1 & prov2
                
                if comunes:
                    print(f"Proveedores comunes: {', '.join(comunes)}")
                else:
                    print("No tienen proveedores en común")
        
        # OPCIÓN 7: Alertas de stock bajo
        elif opcion == "7":
            print("\n⚠️ ALERTAS DE STOCK BAJO (< 2000 kg)")
            print("-" * 60)
            
            alertas = []
            
            for id_mat in materiales:
                if materiales[id_mat]['stock'] < 2000:
                    alertas.append(id_mat)
            
            if alertas:
                for id_mat in alertas:
                    m = materiales[id_mat]
                    print(f"   ⚠️ {m['nombre']}: {m['stock']} kg - REQUIERE REABASTECIMIENTO")
            else:
                print("   ✓ Todos los materiales tienen stock adecuado")
        
        # OPCIÓN 8: Comparar resistencia/peso
        elif opcion == "8":
            print("\n📊 RELACIÓN RESISTENCIA/PESO")
            print("-" * 60)
            
            print(f"{'Material':25} {'Resistencia':15} {'Densidad':15} {'Ratio':10}")
            print("-" * 70)
            
            for id_mat in materiales:
                m = materiales[id_mat]
                ratio = m['resistencia'] / m['densidad']
                print(f"{m['nombre']:25} {m['resistencia']:15} {m['densidad']:15} {ratio:.4f}")
        
        # OPCIÓN 9: Salir
        elif opcion == "9":
            print("\n✓ Saliendo del sistema...")
            continuar = False
        
        else:
            print("\n✗ Opción no válida. Intenta de nuevo.")

else:
    print("\n✗ Opción no válida. El programa terminará.")

print("\n" + "=" * 80)
print("Gracias por usar el Sistema de Gestión de Información")
print("¡Hasta pronto!")
print("=" * 80)
