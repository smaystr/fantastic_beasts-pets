Congratulations on successfully getting thus far! This assignment will preapre you for the last week of the school.

You need to analyze the test data from the file **oxotestdata.json**, and find out **how many OXO game matches resulted in a draw** (i.e. no winner). There is a list of matches, every match is a list of player turns, every turn is a list of column number, row number, and player sign. For example:
```
Game field.
  0 1 2
0 _ _ _
1 _ _ _
2 _ _ _

Match: [[0,0,"O"],[1,2,"X"],[1,1,"O"],[1,0,"X"],[2,2,"O"]]
Turn 0: [0,0,"O"]
O _ _
_ _ _
_ _ _
Turn 1: [1,2,"X"]
O _ _
_ _ _
_ X _
Turn 2: [1,1,"O"]
O _ _
_ O _
_ X _
Turn 3: [1,0,"X"]
O X _
_ O _
_ X _
Turn 4: [2,2,"O"]
O X _
_ O _
_ X O
```
Player "O" wins.

Submit your result (number of draw matches, i.e. 15) to: https://goo.gl/forms/oYWY2rkSfbZ5mp1W2