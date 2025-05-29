def transpose(lst):
    if not lst or not lst[0]:
        return []
    return [[row[i] for row in lst] for i in range(len(lst[0]))]

# Get matrix input from user
rows = int(input("Enter the number of rows in the matrix: "))
matrix = []

for i in range(rows):
    row = input(f"Enter row {i + 1} (space-separated numbers): ")
    matrix.append([int(x) for x in row.split()])

# Transpose the matrix
transposed = transpose(matrix)

# Display the result
print("Transposed matrix:")
for row in transposed:
    print(row)