# [Recurse Center] (https://www.recurse.com/) problems

## Tic Tac Toe game

Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal. The program should let the players take turns to input their moves. The program should report the outcome of the game.

During your interview, you will pair on adding support for a computer player to your game.



## Depth-first searcher

`
    a
   / \
  b   c
 /|\   \
d e f   g
        |
        h
`

Write code that can search a tree of nodes, depth first. The code should take a node name and tree. If it finds the named node, it should return the node. For example, if the code is given "g" and a tree with the structure above, it should return the node named "g".

During your interview, you'll pair on writing code that can do a breadth first search.



## Database server

Before your interview, write a program that runs a server that is accessible on http://localhost:4000/. When your server receives a request on http://localhost:4000/set?somekey=somevalue it should store the passed key and value in memory. When it receives a request on http://localhost:4000/get?key=somekey it should return the value stored at somekey.

During your interview, you will pair on saving the data to a file.



## Lisp parser

Write code that takes some Lisp code and returns an abstract syntax tree. The AST should represent the structure of the code and the meaning of each token. For example, if your code is given "(first (list 1 (+ 2 3) 9))", it could return a nested array like ["first", ["list", 1, ["+", 2, 3], 9]].

During your interview, you will pair on writing an interpreter to run the AST.



## Your own project

If you have an existing project that you are particularly excited about working on for your pairing interview, you can submit that. Ideally, the project should be something you've written from scratch (i.e., not using a framework).

If you submit an existing project, please say what you would like to pair on during your interview. You can choose a bug to fix, a feature to add, or a refactor to do. The interview is only thirty minutes long, so pick something that could be reasonably accomplished in twenty minutes.