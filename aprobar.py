nota_examen = float(input("Ingresar la nota del examen: "))
clases_totales = 50
asistencia_clase = int(input("Ingresar número de clases asistidas: "))
if nota_examen < 0 or nota_examen >100 or asistencia_clase < 0 or asistencia_clase > 50:
 print("Datos introducidos no válidos")
else:
 if nota_examen >= 70 and asistencia_clase >= 40 and nota_examen <= 100 and asistencia_clase <= 50:
  print("Aprobaste la asignatura")
 else:
  print("No aprobaste la asignatura, estudia más vago")