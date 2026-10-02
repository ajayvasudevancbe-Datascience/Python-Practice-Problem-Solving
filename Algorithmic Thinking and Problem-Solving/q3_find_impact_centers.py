""" Question 3: find_impact_centers """
"""
Input: 2D list of 0s and 1s representing electrical activity in an area
Output: List of [row, col]s where lightning directly struck
"""
def find_impact_centers(board):
     result=[]
     n=len(board)
     for row in range(n):
          for column in range(n):
               if board[row][column] == 1:
                count = 0
                if row == 0 or board[row-1][column] == 1:
                    count += 1
                if row == n-1 or board[row+1][column] == 1:
                    count += 1
                if column == 0 or board[row][column-1] == 1:
                    count += 1
                if column == n-1 or board[row][column+1] == 1:
                    count += 1
                if count == 4:
                    result.append([row, column])
                    print(board)
     return result
        
""" Test 3 """
def test_find_impact_centers():
    print("Testing find_impact_centers...", end="")
    data1 = [ [ 0, 0, 0, 0, 1 ],
              [ 0, 1, 0, 1, 1 ],
              [ 1, 1, 1, 0, 1 ],
              [ 0, 1, 1, 0, 0 ],
              [ 0, 1, 1, 1, 0 ] ]
    assert(sorted(find_impact_centers(data1)) == [ [1, 4], [2, 1], [4, 2] ])
    data2 = [ [ 1, 0, 0],
              [ 0, 0, 0],
              [ 0, 1, 0] ]
    assert(sorted(find_impact_centers(data2)) == [ ])
    data3 = [ [ 1, 1, 1, 1 ],
              [ 1, 1, 1, 1 ],
              [ 1, 1, 1, 1 ],
              [ 1, 0, 0, 1 ] ]
    assert(sorted(find_impact_centers(data3)) == [ [0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 3] ])
    print("... done!")


if __name__ == '__main__':
    test_find_impact_centers()