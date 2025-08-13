import pandas as pd # type: ignore

df = pd.read_csv("estudiantes.csv")

print("Tabla Completa:")
print(df)
print("\n📌 Alumnos con calificación mayor a 90:")
print(df[df['Notas'] > 90])
print("\n📌 Alumnos con calificación menor a 90:")
print(df[df['Notas'] < 90])

nota_maxima = df['Notas'].max()
nota_min = df['Notas'].min()
print(f"\n Nota Maxima: {nota_maxima}")
print(f"\n Nota Maxima: {nota_min}")