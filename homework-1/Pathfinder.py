'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest
from heapq import heappush, heappop

class Pathfinder:

    @staticmethod
    def solve(problem):
        current_node = SearchTreeNode(\
            state=problem.initial,\
            action=None,\
            parent=None,\
            totalCost=0,\
            heuristicCost=problem.heuristic(problem.initial))

        to_visit = heappush([], current_node) # priority q
        while not problem.goal_test(current_node.state):
            current_node = heappop(to_visit)
            children = problem.transitions(current_node.state)
            for child in children:
                child_action, child_cost, child_state = child
                child_node = SearchTreeNode(\
                state=child_state,\
                action=child_action,\
                parent=current_node,\
                totalCost=current_node.totalCost + child_cost,\
                heuristicCost=problem.heuristic(child_state))
                heappush(child_node)

        path = []
        while current_node.parent != None:
            path.append(current_node.action)
            current_node = current_node.parent

        return list(reversed(path))

class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze3(self):
        maze = ["XXXXX", "X..GX", "X.MMX", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze4(self):
        maze = ["XXXXXX", "X....X", "X*.XXX", "X..XGX", "XXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        self.assertFalse(soln)


if __name__ == '__main__':
    unittest.main()
