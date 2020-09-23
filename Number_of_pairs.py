'''
Problem 2 Number of pairs
Jack works at a clothing store. He has a large pile of gloves that he must pair by color for sale. Given an array of
integers representing the color of each glove, determine how many pairs of gloves with matching colors there
are.
For example, there are n=8 gloves with colors ar=[1,2,1,2,1,2,2,3]. There is one pair of color 1 and two of color 2.
There are two odd gloves left, one of each color. The number of pairs is 3 .
Input format:
Enter n value which determines the number of gloves (integer).
Enter elements of array ar comprising the integer values corresponding to sock colour:
Output format:
Return the total number of matching pairs of gloves that jack can sell.
'''
from collections import Counter
n = int(input())
Socks = Counter(map(int,input().strip().split()))
Number_Of_Pairs = 0
for Sock in Socks:
    Number_Of_Pairs += Socks[Sock]//2
print(Number_Of_Pairs)

'''
output:
10
1 3 2 1 5 4 6 5 9 9
3
'''
