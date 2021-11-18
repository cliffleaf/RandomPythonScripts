Matrix multiplication: suppose A1 * A2, then the number of columns in A1 should be equal to the number of rows in A2. The resulting matrix is A3.

It basically follows the algorithm of:

1. choose a row in A1, choose a column in A2
2. find A1[row][i] * A2[i][col] for i from 1 to k
3. The sum from Step 2 is the entry for A3[row][column]
