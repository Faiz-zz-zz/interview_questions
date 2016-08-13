"""
A gene is represented as a string of length n (where n is divisible by 4), composed of the letters G, A, C, and T. It is considered to be steady if each of the four letters occurs exactly n/4 times. For example, GACT and AAGTGCCT are both steady genes.

Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string . It is not necessarily steady. Fortunately, Limak can choose one (maybe empty) substring of and replace it with any substring of the same length.

Modifying a large substring of bear genes can be dangerous. Given a string s, can you help Limak find the length of the smallest possible substring that he can replace to make s a steady gene?

Note: A substring of a string s is a subsequence made up of zero or more consecutive characters of s.

Input Format

The first line contains an integer n divisible by 4, denoting the length of a string s. The second line contains a string s of length n. Each character is one of the four: G, A, C, T.

Output Format

On a new line, print the minimum length of the substring replaced to make s stable.

Sample Input

8  
GAAATAAA
Sample Output

5

"""
from collections import Counter 
gene = input()

gene_count = Counter()

for letter in gene:
	gene_count[letter] += 1

ideal = len(gene)//4
adj = {}
for letter in gene_count:
	if ideal < gene_count[letter]:
		adj[letter] = gene_count[letter] - ideal 
start = sum(adj.values())		

for i in range(start, len(gene)):
	for j in range(0, len(gene) - i):
		flag = True
		for letter in adj.keys():
			if (gene[j:i+j].count(letter) != adj[letter]):
				flag = False
		if flag:
			print(i)
			exit()		