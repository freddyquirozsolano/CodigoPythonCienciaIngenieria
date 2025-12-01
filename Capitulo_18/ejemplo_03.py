# Análisis de secuencia de ADN con BioPython
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

# Crear una secuencia de ADN
secuencia_adn = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

print(f"Secuencia ADN: {secuencia_adn}")
print(f"Longitud: {len(secuencia_adn)} nucleótidos")

# Transcripción: ADN → ARN
secuencia_arn = secuencia_adn.transcribe()
print(f"\nSecuencia ARN: {secuencia_arn}")

# Traducción: ARN → Proteína
proteina = secuencia_arn.translate()
print(f"Proteína: {proteina}")

# Calcular contenido GC
contenido_gc = gc_fraction(secuencia_adn) * 100
print(f"\nContenido GC: {contenido_gc:.2f}%")

# Secuencia complementaria
complementaria = secuencia_adn.complement()
print(f"Secuencia complementaria: {complementaria}")

# Secuencia reversa complementaria
reversa_comp = secuencia_adn.reverse_complement()
print(f"Reversa complementaria: {reversa_comp}")