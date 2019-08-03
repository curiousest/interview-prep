from types import List
from heapq import heappush, heappop

class Section:
    def __init__(self, index, orientation):
        self.index = index
        self.orientation = orientation
        self.items = set()
    
    def __gt__(self, other):
        return len(self) > len(other)

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        verticals = [Section(i, 'vertical') for i in range(9)]
        horizontals = [Section(i, 'horzontal') for i in range(9)]
        squares = [[Section((i,j), 'square') for j in range(3)] for i in range(3)]

        full_verticals = set()
        full_horizontals = set()
        full_squares = set()

        for row, items in enumerate(board):
            for col, item in enumerate(items):
                if item != '.':
                    horizontals[row].items.add(item)
                    verticals[col].items.add(item)
                    squares[row // 3][col // 3].items.add(item)
                    
        
        section_heap = []
        for index, section in enumerate(verticals):
            if len(section.items) == 9:
                full_verticals.add(index)
            else:
                heappush(section_heap, section)
        for index, section in enumerate(horizontals):
            if len(section.items) == 9:
                full_horizontals.add(index)
            else:
                heappush(section_heap, section)
        for i, row in enumerate(squares):
            for j, section in enumerate(row):
                if len(section.items) == 9:
                    full_squares.add((i, j))
                else:
                    heappush(section_heap, section)
        if len(section_heap) == 0:
            return

        curr_section = heappop(section_heap)
        while curr_section is not None:
            missing_num = None
            for i in range(1,10):
                if i not in curr_section:
                    missing_num = i
                    break
            row = None
            col = None
            if curr_section.orientation == 'vertical':
                row = 
            elif curr_section.orientation == 'horizontal':
                pass
            else:
                pass
            

        



