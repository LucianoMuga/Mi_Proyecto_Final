from ejemplo.models import Familiar

Familiar(nombre="Luciano", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Silvana", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Claudio", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Rodrigo", direccion="Rio Parana 745", numero_pasaporte=567567).save()

print("Se cargo con éxito los usuarios de pruebas")