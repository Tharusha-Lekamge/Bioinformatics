# Needleman-Wunch algorithm for global alignment


def print_val_matrix():
    for i in range(0, len_2 + 1):
        for j in range(0, len_1 + 1):
            # use format string to print the grid
            print("{:3}".format(matrix[i][j]["val"]), end=" ")
        print()


def print_ptr_matrix():
    for i in range(0, len_2 + 1):
        for j in range(0, len_1 + 1):
            # use format string to print the grid
            print(
                "({:2},{:2})".format(
                    matrix[i][j]["prev_ptr"][0], matrix[i][j]["prev_ptr"][1]
                ),
                end=" ",
            )
        print()


mode = input("Enter 1 for automatic mode, 2 for manual mode: ")
if mode == "1":
    gene_1 = "ACGCTG"
    gene_2 = "CATGT"
else:
    gene_1 = input("Enter first gene: ")
    gene_2 = input("Enter second gene: ")

len_1 = len(gene_1)
len_2 = len(gene_2)

# Initialize the matrix
matrix = [
    [{"prev_ptr": (-1, -1), "val": 0} for x in range(len_1 + 1)]
    for y in range(len_2 + 1)
]

print_val_matrix()

COST_MATCH = 2
COST_MISMATCH = -1

# Fill the first row and column
for i in range(1, len_2 + 1):
    matrix[i][0]["val"] = matrix[i - 1][0]["val"] - 1
    matrix[i][0]["prev_ptr"] = (i - 1, 0)

for j in range(1, len_1 + 1):
    matrix[0][j]["val"] = matrix[0][j - 1]["val"] - 1
    matrix[0][j]["prev_ptr"] = (0, j - 1)

print("After filling first row and column")
print_val_matrix()
print_ptr_matrix()
