"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

from collections import deque
letters = list('abcdefghijklmnopqrstuvwxyz')
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        def findAllNeighbors(word_dist, wordList, queue, explored):
            for i in range(len(word_dist[0])):
                for l in letters:
                    neighbor = word_dist[0][:i]+ l + word_dist[0][i+1:]
                    if neighbor != word_dist[0] and neighbor in wordList and neighbor not in explored:
                        queue.append((neighbor, word_dist[1]+1))
                        explored.add(neighbor)
        word_set = set(wordList)
        queue = deque()
        queue.append((beginWord,1))
        explored = set()
        while(len(queue)>0):
            word_dist = queue.popleft()
            if word_dist[0] == endWord:
                return word_dist[1]
            findAllNeighbors(word_dist, word_set, queue, explored)
        return 0
