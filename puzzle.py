# Name: Adrian Melendrez
# Class: CS 325 section: 400 W2022
# Email: melendra@oregonstate.edu
# Assignment: Homework 8 Problem 3
# Date: 02/26/2022

import heapq

def solve_puzzle(Board, Source, Destination):
    """
    Function that finds the min number of steps
    it takes to reach a cell 'Destination' from
    cell 'Source'. It returns the min number of
    steps. Uses a Breadth First approach.

    EXTRA CREDIT: Does the above and returns a set of
    possible directions in the form of a string.
    """

    if len(Board[0]) >= 3 and len(Board) >= 3:
        #we start at 0 in computer science so -1 to reflect that.
        m = Source[0] - 1
        n = Source[1] - 1
        end_m = Destination[0] - 1
        end_n = Destination[1] - 1

        temp_storage = {}
        visited = [[False for i in range(len(Board[0]))] for j in range(len(Board))]
        steps = 0
        path = []
        pq = [(steps, m, n)]
        path.append(['previous value',(m,n), 'Direction: U, D, L or R'])

        while len(pq) > 0:
            visited[m][n] = True
            steps, m, n = heapq.heappop(pq)

            #UP
            if (m-1) >= 0 and Board[m-1][n] != '#':
                #NOT VISITED
                if (visited[m-1][n] != True):
                    temp_storage[(m-1,n)] = steps + 1
                    path.append([(m, n), (m-1,n), 'U'])

            #DOWN
            if (m+1) < len(Board) and Board[m+1][n] != '#':
                # NOT VISITED
                if (visited[m+1][n] != True):
                    temp_storage[(m + 1, n)] = steps + 1
                    path.append([(m, n), (m+1, n), 'D'])

            #LEFT
            if (n-1) >= 0 and Board[m][n-1] != '#':
                # NOT VISITED
                if (visited[m][n-1] != True):
                    temp_storage[(m, n-1)] = steps + 1
                    path.append([(m, n), (m,n-1), 'L'])

            #RIGHT
            if (n+1) < len(Board[0]) and Board[m][n+1] != '#':
                # NOT VISITED
                if (visited[m][n+1] != True):
                    temp_storage[(m, n+1)] = steps + 1
                    path.append([(m, n), (m,n+1), 'R'])

            #find the value with the min amount of steps from Start
            min_steps = min(temp_storage.values())

            #looks at the keys and values of those keys at the specified value at min_steps
            next_key = list(temp_storage.keys())[list(temp_storage.values()).index(min_steps)]
            heapq.heappush(pq, (min_steps, next_key[0], next_key[1]))


            #if we have reach destination coordinates
            if (end_m, end_n) in temp_storage:

                #get the final amount of steps - 1 since we dont count the end cordinates.
                total_steps = temp_storage.get((end_m, end_n)) - 1

                end_cord = (end_m, end_n)
                find = []

                #helper method to return directions in form of a string
                path_directions = find_path_helper(path, find, end_cord)

                return total_steps, path_directions


            # if we have reach edges of row and column and no solution
            if (len(Board) - 1, len(Board[0]) - 1) in temp_storage:
                return None

            #pop the next_key value above from temp_storage so we dont re-use the (m,n) cordinates.
            temp_storage.pop(next_key)

            #these are the next cordinates
            m = next_key[0]
            n = next_key[1]


def find_path_helper(path,find, end_cord):
    """
    helper method to return
    directions in form of a string
    """
    path.reverse()
    # We start at the end cordinates and use its
    # previous value to move back to the Start.
    # Save each direction in find array
    for i in path:
        if i[1] == end_cord:
            find.append(i[2])
            end_cord = i[0]
    find.reverse()
    find.pop(0)
    finds = ''.join(find)
    return finds


# Driver Code
if __name__ == '__main__':
    Board = [['-','-', '-', '-', '-'],
            ['-','-', '#', '-', '-'],
            ['-','-', '-', '-', '-'],
            ['#','-', '#', '-', '-'],
            ['-','#', '-', '-','-']]

    Source = (1,3)
    Destination = (5,5)
    print(solve_puzzle(Board,Source, Destination))