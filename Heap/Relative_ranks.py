"""
ある人のスコアの列としてscore配列が与えられる
その人のスコアの順位をranks配列の同じindexに保存する
heapでの実装のためindexがその都度かわるため、scoreのindexをハッシュマップで保存する
popされたscoreであるtargetのindexをindexes[target]で見つける

下の実装は、ソートしてindexをハッシュで保存する方がかんたんじゃねと思って実装
時間は二つとも変わらないけど、下の方が直感的にわかりやすいと思う
"""
import heapq
from typing import List
from collections import deque
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexes = {sc: index for index, sc in enumerate(score)}
        ranks = [None]*len(score)
        score = list(map(lambda x: -x, score))
        heapq.heapify(score)
        rank = 1
        while score:
            target = heapq.heappop(score)*-1
            if rank == 1:
                ranks[indexes[target]] = 'Gold Medal'
            elif rank == 2:
                ranks[indexes[target]] = 'Silver Medal'
            elif rank == 3:
                ranks[indexes[target]] = 'Bronze Medal'
            else:
                ranks[indexes[target]] = str(rank)
            rank += 1

        return ranks
    

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexes = {sc: index for index, sc in enumerate(score)}
        ranks = [None]*len(score)
        score.sort(reverse=True)
        score = deque(score)
        rank = 1
        while score:
            target = score.popleft()
            if rank == 1:
                ranks[indexes[target]] = 'Gold Medal'
            elif rank == 2:
                ranks[indexes[target]] = 'Silver Medal'
            elif rank == 3:
                ranks[indexes[target]] = 'Bronze Medal'
            else:
                ranks[indexes[target]] = str(rank)
            rank += 1
        
        return ranks