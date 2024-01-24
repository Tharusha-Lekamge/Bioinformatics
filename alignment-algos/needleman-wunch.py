# Needleman-Wunch algorithm for global alignment

# Input: 2 strings
# Output: 2 strings aligned

# Example:
# Input:
# CATGT
# ACGCTG

# Output:
# CATGT-
# AC-GCTG

# Some Limitations:
# 1. Only 2 sequences
# 2. Only 2 costs (match, mismatch)
# 3. Only 1 gap penalty
# 4. Only 1 traceback path


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
    gene_1 = "CATGT"
    gene_2 = "ACGCTG"
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

#print("After filling first row and column")
#print_val_matrix()
#print_ptr_matrix()

# Fill the rest of the matrix
for i in range(1, len_2 + 1):
    for j in range(1, len_1 + 1):
        # Calculate current cost
        cost_i_j = COST_MATCH if gene_2[i-1] == gene_1[j-1] else COST_MISMATCH
        #print(gene_2[i-1], gene_1[j-1], cost_i_j )

        # Calculate 3 costs
        cost_1 = matrix[i-1][j-1]["val"] + cost_i_j
        cost_2 = matrix[i-1][j]["val"] - 1
        cost_3 = matrix[i][j-1]["val"] - 1

        cost_max = max(cost_1, cost_2, cost_3)
        max_ptr = (i-1, j-1) if cost_1 == cost_max else (i-1, j) if cost_2 == cost_max else (i, j-1)

        #print(cost_1, cost_2, cost_3, cost_max, max_ptr)

        matrix[i][j] = {"prev_ptr": max_ptr, "val": cost_max}

print("Final matrix")

print_val_matrix()
print_ptr_matrix()

# Traceback
i = len_2
j = len_1
alignment_1 = ""
alignment_2 = ""

while i != 0 or j != 0:
    print(i, j)
    prev_ptr = matrix[i][j]["prev_ptr"]
    if prev_ptr[0] == i - 1 and prev_ptr[1] == j - 1:
        alignment_1 = gene_1[j - 1] + alignment_1
        alignment_2 = gene_2[i - 1] + alignment_2
    elif prev_ptr[0] == i - 1:
        alignment_1 = "-" + alignment_1
        alignment_2 = gene_2[i - 1] + alignment_2
    else:
        alignment_1 = gene_1[j - 1] + alignment_1
        alignment_2 = "-" + alignment_2
    i = prev_ptr[0]
    j = prev_ptr[1]

print(alignment_1)
print(alignment_2)