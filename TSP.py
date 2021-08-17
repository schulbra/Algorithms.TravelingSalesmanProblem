# -----------------------------------------------------------------------------|
# Name: Brandon Schultz
# Date: 8-5-21
# Assignment: Graph Algorithms
# Question 2   -   NP-Completeness and Heuristic Algorithms Problem):
# Sources:
# - https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
# - https://www.geeksforgeeks.org/travelling-salesman-problem-greedy-approach/
# -----------------------------------------------------------------------------|

'''-----------------------------------------------------------------------------
d.
- Implement the nearest neighbor heuristic for TSP problem. Consider the first 
node as problems starting point.
  -The Function is named: solve_tsp(G)
  -The input Graph is provided in the form of a 2-D matrix.
    -Sample input:
        G: [[0,1,3,7], [1,0,2,3],[3,2,0,1], [7,3,1,0]]
    -Sample Output:
        11
-----------------------------------------------------------------------------'''

#|-----------------------------------------------------------------|
# Implementation of the nearest neighbor heuristic for TSP problem:
# -----------------------------------------------------------------|
def solve_tsp(G, vertices):
    #|------------------------------------------------------------------------|
    # "prev_traveled" array for holding nodes/vertices already traveled by SP.
    #|------------------------------------------------------------------------|
    prev_traveled = []
    V = vertices
    weight = 0
    #|-------------------------------------------------------------|
    # Loop runs unitl prev_traveled arr contains all node vals of G.
    #|-------------------------------------------------------------|
    while vertices not in prev_traveled:
            #|---------------------------------------------------------------------|
            # currVEdges stores most recently trvaeled nodes edge weight val(s) to
            # use as basis for compariosn against vals making up solution to TSP up
            # to point of said comparison via minimum node and corresppnding edge
            # weights of min node represented by curr_V_Min_Weight, curr_V_Min.
            #|---------------------------------------------------------------------|
            curr_V_Edges = G[vertices]
            curr_V_Min_weight = -1
            curr_V_Min = -1
            prev_traveled.append(vertices)
            #|-----------------------------------------------------------------------------|
            # For loop scans edges of current node for smallest weighted and unvisited edge
            # before deciding on next node to travel towards and edge weight added to TSP
            # solution. Process continues until all nodes have been traversed.
            #|-----------------------------------------------------------------------------|
            for (A, B) in enumerate(curr_V_Edges):
             if (curr_V_Min_weight == -1) and (A not in prev_traveled):
                curr_V_Min_weight = B
                curr_V_Min = A
             elif (curr_V_Min_weight != -1) and (B < curr_V_Min_weight) and (A not in prev_traveled):
                curr_V_Min_weight = B
                curr_V_Min = A
            #|----------------------------------|
            # Next node traveled to:
            #|----------------------------------|
            if curr_V_Min != -1:
             vertices = curr_V_Min
            #|------------------------------------|
            # Cost of travel added to TSP solution:
            #|------------------------------------|
            if curr_V_Min_weight != -1:
             weight += curr_V_Min_weight
    #|-------------------------------------------------------------|
    # After full traversal of graph, weight of last node traveled 
    # is added to totaland value is displayed to user as answer to 
    # TSP problem:      
    #|-------------------------------------------------------------|
    weight += G[vertices][V]
    print(" Sample input: ")
    print(" G: [[0,1,3,7], [1,0,2,3],[3,2,0,1], [7,3,1,0]] ")  
    print(" Output: ", weight)
#|----------------------------------------------|
# Sample input  
# G: [[0,1,3,7], [1,0,2,3],[3,2,0,1], [7,3,1,0]] 
# Expected Output: 11
#|----------------------------------------------|
G =  [[0,1,3,7], [1,0,2,3],[3,2,0,1], [7,3,1,0]]
solve_tsp(G, 0)

