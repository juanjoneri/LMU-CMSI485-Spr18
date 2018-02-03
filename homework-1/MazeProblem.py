'''
Homework 1 MazeProblem Formalization:
MazeProblems represent 2D pathfinding problems, as programmatically
formalized via:

=== Mazes ===
Represented as a list of strings in which:
  X = impassable wall
  * = the initial state
  . = open cells (movement cost of 1)
  M = mud tiles (movement cost of 3)
  G = goal states (movement cost of 1)
All valid mazes have:
  - Exactly 1 initial state
  - At least 1 goal state
  - A border of walls (plus possibly other walls)
[!] Note: for HW1, a valid maze may *not* have a solution!
(We'll ignore invalid maze states as possible inputs, for simplicity)

Maze elements are indexed starting at (0, 0) [top left of maze]. E.g.,
["XXXXX", "X..GX", "X.M.X", "X*..X", "XXXXX"] is interpretable as:
  01234
0 XXXXX
1 X..GX
2 X.M.X
3 X*..X
4 XXXXX

=== States ===
Representing the position of the agent, as tuples in which:
(x, y) = (col, row)
(0, 0) is located at the top left corner; Right is +x, and Down is +y

=== Actions ===
Representing the allowable Up, Down, Left, and Right movement capabilities
of the agent in the 2D Maze; we'll simply use string representations:
"U", "D", "L", "R"

=== Transitions ===
Given some state s, the transitions will be represented as a list of tuples
of the format:
[(action1, cost_of_action1, result(action1, s)), ...]
For example, if an agent is at state (1, 1), and can only move right and down
into clear tiles (.), then the transitions for that s = (1, 1) would be:
[("R", 1, (2, 1)), ("D", 1, (1, 2))]
'''
import numpy as np
import math
class MazeProblem:
    # Static costMap for maze components and the cost to move onto them
    # Any component not listed assumed to have a cost of 1
    costMap = {"M": 3, ".": 1}
    actions = {"U":(0, -1) , "D":(0, 1), "L":(-1, 0), "R":(1, 0)}

    # MazeProblem Constructor:
    # Constructs a new pathfinding problem from a maze, described above
    def __init__(self, maze):
        self.maze = maze
        self.initial = None
        self.goals = []

        for r in list(enumerate(maze)):
            for c in list(enumerate(r[1])):
                state = (c[0], r[0])
                if c[1] is "*":
                    self.initial = state
                if c[1] is "G":
                    self.goals.append(state)

    # goalTest is parameterized by a state, and
    # returns True if the given state is a goal, False otherwise
    def goalTest(self, state):
        try:
            col, row = state
            return self.maze[row][col] == 'G'
        except:
            return False

    @staticmethod
    def _distance(initial_state, final_state):
        return np.linalg.norm(np.array(initial_state)-np.array(final_state))

    def valid(self, state):
        col, row = state
        try:
            return self.maze[row][col] != 'X'
        except:
            return False

    # Implements the Manhattan Distance Heuristic, which (given a state)
    # provides the cell-distance to the nearest goal state
    def heuristic(self, state):
        min_distance = math.inf
        for goal in self.goals:
            min_distance = min(min_distance, _distance(state, goal))
        return min_distance

    # transitions returns a list of tuples in the format:
    # [(action1, cost_of_action1, result(action1, s), ...]
    # corresponding to allowable actions of the given state, as well
    # as the next state the action leads to
    def transitions(self, state):
        col, row = state
        transitions = []
        for action, delta in MazeProblem.actions.items():
            d_col, d_row = delta
            result = (col+d_col, row+d_row)
            if self.valid(result):
                transitions.append((action, self.cost(result), result))
        return transitions

    # cost returns the cost of moving onto the given state, and employs
    # the MazeProblem's costMap
    def cost(self, state):
        cm = MazeProblem.costMap
        cell = self.maze[state[1]][state[0]]
        return cm[cell]

    # solnTest will return a tuple of the format (cost, isSoln) where:
    # cost = the total cost of the solution,
    # isSoln = true if the given sequence of actions of the format:
    # [a1, a2, ...] successfully navigates to a goal state from the initial state
    # If NOT a solution, return a cost of -1
    def solnTest(self, soln):
        trans = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
        s = self.initial
        tc = 0
        for m in soln:
            s = (s[0] + trans[m][0], s[1] + trans[m][1])
            tc += self.cost(s)
            if self.maze[s[1]][s[0]] == "X":
                return (-1, False)
        return (tc, self.goalTest(s))
