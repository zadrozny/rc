#!/usr/bin/python
# -*- coding: utf-8 -*-


'''

Depth-first searcher

    a
   / \
  b   c
 /|\   \
d e f   g
        |
        h

Write code that can search a tree of nodes, depth first. The code should take a node name and tree. If it finds the named node, it should return the node. For example, if the code is given "g" and a tree with the structure above, it should return the node named "g".

During your interview, you'll pair on writing code that can do a breadth first search.

'''

# Model the tree as an adjacency matrix
#     a  b  c  d  e  f  g  h      
T = [[0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0]]

key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def find(tree, target):
    current_gen = [0]                          # The root
    children = []

    while True:
        node = current_gen.pop(0)              # Take a sibling
        
        if key[node] == target:    
            print 'Target reached:', key[node] # Print row
            return                             # Escape
        else:
            print 'We are at ', key[node] 

        children.extend([child for child in range(len(T[0])) 
                                if T[node][child] == 1])

        if current_gen == []:                 # No more siblings
            if children == []:                # No more children
                break 
            else:
                current_gen.extend(children) # Move to next gen
                children = []

find(0, 'c')