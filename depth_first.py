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


def find(node, tree, direction='down', predecessors=[], target=None):
    '''Searches depth-first for a node, printing nodes as it goes'''

    if direction == 'down':
        print key[node]
        if key[node] == target:
            return                # Escape
    try:
        nxt = tree[node].index(1) # First child 
        tree[node][nxt] = 0       # Mark current as visited
        predecessors.append(node) 
        find(node=nxt, tree=tree, direction='down', 
             predecessors=predecessors, target=target)
    
    except ValueError:            # Childless node
        if node - 1 == -1:        # Stop (nothing before root)
            return None
        else:
            parent = predecessors.pop()
            find(node=parent, tree=tree, direction='up', 
                 predecessors=predecessors, target=target)    # Move up

find(0, T, target='d')
