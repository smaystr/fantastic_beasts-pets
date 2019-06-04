# elevator-python

This is an elevator state machine problem, for each step the elevator state machine will receive a line indicating what floor it's on, and what buttons are activated. There are 3 kinds of buttons, up, down, and elevator. Up buttons, like u9 indicate that someone on a particular floor has pushed the up button. Similarly for down buttons d2 would indicate that someone on the 2nd floor has pushed the down button. Elevator buttons indicate that someone on the elevator has pushed a button for a particular floor, e3 indicates that someone has pushed the button on the elevator for floor 3.

At each step, the elevator should output what action to take (up, down, stop) and also what to display on an indicator (up, down, stop). This should be in a tuple of (action, indicator).  Please ensure that the elevator's behavior does not zigzag or starve any floor indefinitely.  To put it more plainly, you should feel good about getting in this elevator, and know that it will take you where you want to go efficiently.

We provide you with 2 sample test inputs, test_input1.txt and test_input2.txt and their respective solutions (test_input1_solution.txt and test_input2_solution.txt).
You can run the following command to see what the skeleton does before you make modifications:

`cat test_input1.txt | python elevator_skeleton.py`

currently it will return
```
1 d6 e3 u6 e8 d8 ----> up, up
2 d6 e3 u6 e8 d8 ----> stop, up
3 d6 e3 u6 e8 d8 ----> up, up
3 d6 u6 e8 d8 ----> stop, up
4 d6 u6 e8 d8 ----> up, up
5 d6 u6 e8 d8 ----> stop, up
6 d6 u6 e8 d8 ----> up, up
6 d6 e10 e8 d8 ----> stop, up
7 d6 e10 e8 d8 ----> up, up
8 d6 e10 e8 d8 ----> stop, up
8 d6 e10 d8 ----> up, up
9 d6 e10 d8 ----> stop, up
10 d6 e10 d8 ----> up, up
10 d6 d8 ----> stop, up
9 d6 d8 ----> up, up
8 d6 d8 ----> stop, up
8 d6 e3 ----> up, up
7 d6 e3 ----> stop, up
6 d6 e3 ----> up, up
6 e3 e2 ----> stop, up
5 e3 e2 ----> up, up
4 e3 e2 ----> stop, up
3 e3 e2 ----> up, up
3 e2 ----> stop, up
2 e2 ----> up, up
```

This is incorrect behavior, all it does is continue to go up and stop at each floor on the way. It's also inconsistent with the behavior the input implies. 