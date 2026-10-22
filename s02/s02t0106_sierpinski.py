from array import array as arr

# parametros de la cuadricula
rows = 8
columna = 2 * rows-1

#creadno el grid 2D
matrix = []

#construyendo el grid (rejilla)
for _ in range(rows):
    new_row= arr('i', [0] * columna)
    matrix.append(new_row)

#validando la construccion del grid
print(f"cantidad de filas: {len(matrix)}")
print(f"cantidad de columnas: {len(matrix[0])}")

for row in matrix:
    print(list(row))
