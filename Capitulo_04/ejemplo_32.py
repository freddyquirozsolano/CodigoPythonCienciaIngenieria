# Sistema de selección de materiales para diseño
def analizar_material(tipo_material, aplicacion):
    match (tipo_material.lower(), aplicacion.lower()):
        case ("acero", "estructural"):
            return {
                "material": "Acero A36",
                "resistencia": "250 MPa",
                "ventaja": "Económico y resistente"
            }
        
        case ("aluminio", "aeroespacial" | "automotriz"):
            return {
                "material": "Aluminio 6061-T6",
                "resistencia": "310 MPa",
                "ventaja": "Ligero y resistente"
            }
        
        case _:
            return {"material": "No especificado"}
