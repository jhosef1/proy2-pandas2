import pandas as pd # type: ignore

df = pd.read_csv("estudiantes.csv")

print("Tabla Completa:")
print(df)
print("\n📌 Alumnos con calificación mayor a 8:")
print(df[df['Notas'] > 90])