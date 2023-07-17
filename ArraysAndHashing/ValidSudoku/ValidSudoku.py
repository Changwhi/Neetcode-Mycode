class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Utilizing has sets
        # Initialize three has sets, one for checking rows, one for checking columns, one for checking sub-boxes
        # Iterate through the input array and check if it is already present in the corresponding row, colum, or sub-box has set
        # If the element is already present, return False
        # If the elements is not a duplicate, store it in the respective has sets
        # After iteraing through the entire array without finding any duplicates, return True

        # delcare set, you can declare by using hashSet = set()
        checkRow = collections.defaultdict(set)
        checkCol = collections.defaultdict(set)
        checkSubBox = collections.defaultdict(set)

        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    continue
                if (board[row][column] in checkRow[row] or
                board[row][column] in checkCol[column] or
                board[row][column] in checkSubBox[row // 3, column // 3]): # using // to get an integer value
                    return False

                checkCol[column].add(board[row][column])
                checkRow[row].add(board[row][column])
                checkSubBox[row // 3, column // 3].add(board[row][column])
        return True
