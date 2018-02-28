import re
import numpy as np

class MazeProblem:

    def __init__(self, maze):
        self.actions = {"U":(0, -1) , "D":(0, 1), "L":(-1, 0), "R":(1, 0)}
        self.maze = maze
        self.initial = self.where('*').pop()
        self.goals = self.where('G')

    def where(self, char):
        result = set()
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == char:
                    result.add((col, row))
        return result

    def goal_test(self, state):
        return state in self.goals

    def transitions(self, state):
        x, y = state
        transitions = []
        for action, delta in self.actions.items():
            dx, dy = delta
            result = (x+dx, y+dy)
            if self.valid(result):
                transitions.append((action, result))
        return transitions

    def valid(self, state):
        x, y = state
        try:
            return self.maze[y][x] != 'X'
        except:
            return False

    def soln_test(self, soln):
        trans = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
        s = self.initial
        for m in soln:
            s = (s[0] + trans[m][0], s[1] + trans[m][1])
            if self.maze[s[1]][s[0]] == "X":
                return (-1, False)
        return (len(soln), self.goal_test(s))

if __name__ == '__main__':
    problem = MazeProblem(\
        [ "XXXXX"\
        , "XG.GX"\
        , "XX..X"\
        , "X*..X"\
        , "XXXXX" ])
    print("Initial: ", problem.initial)
    print("Goal: ", problem.goals)
    print(problem.transitions((1,3)))
