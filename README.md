# Some tools/scripts I wrote during my study of computer science
Sorting the order (smallest to largest) of 4 numbers, without turning them into a list and employ sorting algorithms like bubble sort. The code is written in Python. But since no lists are used, it should be easily convertable into other languages. 

In prior, the readers should be able to sort the order of 3 numbers:  # 3, 4, 5
1. find out the min and max   # 3, 5
2. calculate the total (num1 + num2 + num3)  # 3 + 4 + 5 = 12
3. calculate the middle value using (total - min - max)  # 12 - 3 - 5 = 4

Among the 4 numbers case, we first divide the numbers in two parts randomly. Each part contains 2 of the 4 numbers.

1. finding out the min and max of the first two numbers. 
2. compare the min from Round 1 with the other two numbers. Subsequently, the min from this round would be the actual smallest among all 4 numbers. We also get a temporary maximum and a temporary middle value
3. compare the max from Round 1 with temp max and temp middle from Round 2. Now we will get the actual largest. The min from this round will be the actual second smallest, and the middle value will be the actual third smallest (second largest)

------------------------------------------------------------------------------------------

Matrix multiplication: suppose A1 * A2, then the number of columns in A1 should be equal to the number of rows in A2. The resulting matrix is A3.

It basically follows the algorithm of:
1. choose a row in A1, choose a column in A2
2. find A1[row][i] * A2[i][col] for i from 1 to k
3. The sum from Step 2 is the entry for A3[row][column]
