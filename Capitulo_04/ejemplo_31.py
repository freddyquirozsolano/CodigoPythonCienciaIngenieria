# Manejador de métodos HTTP
def procesar_solicitud_http(metodo, ruta, datos=None):
    match metodo.upper():
        case "GET":
            print(f"📥 GET: Obteniendo recurso en {ruta}")
            return {"accion": "read", "status": 200}
        
        case "POST":
            print(f"📤 POST: Creando recurso en {ruta}")
            return {"accion": "create", "status": 201}
        
        case "DELETE":
            print(f"🗑️  DELETE: Eliminando recurso")
            return {"accion": "delete", "status": 204}
        
        case _:
            return {"error": "Método no permitido", "status": 405}
