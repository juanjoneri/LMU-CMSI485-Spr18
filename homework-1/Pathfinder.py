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

        to_visit = [current_node] # priority q
        visited_states = set()

        deb_count = 1 # for report

        while any(to_visit) and not problem.goalTest(current_node.state):
            current_node = heappop(to_visit)
            if current_node.state in visited_states:
                continue
            else:
                visited_states.add(current_node.state)

            transitions = problem.transitions(current_node.state)
            for transition in transitions:
                child_action, child_cost, child_state = transition
                child_node = SearchTreeNode(\
                    state=child_state,\
                    action=child_action,\
                    parent=current_node,\
                    totalCost=current_node.totalCost + child_cost,\
                    heuristicCost=problem.heuristic(child_state))
                heappush(to_visit, child_node)
                deb_count += 1

        print("count: ", deb_count)
        if not problem.goalTest(current_node.state):
            return None

        path = []
        while current_node.parent != None:
            path.append(current_node.action)
            current_node = current_node.parent

        return list(reversed(path))

class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", \
                "X..GX", \
                "X...X", \
                "X*..X", \
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", \
                "XG..X", \
                "XX..X", \
                "X*..X", \
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze3(self):
        maze = ["XXXXX", \
                "X..GX", \
                "X.MMX", \
                "X*..X", \
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze4(self):
        maze = ["XXXXXX", \
                "X....X", \
                "X*.XXX", \
                "X..XGX", \
                "XXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        self.assertFalse(soln)


if __name__ == '__main__':
    # unittest.main()
    maze_1 = \
        ["XXXXXXXXXXXX",\
        "XG.......XGX",\
        "X...XXX..X.X",\
        "X...XGX..X.X",\
        "X...XXX..X.X",\
        "X.......XX.X",\
        "X..........X",\
        "X......XXXXX",\
        "X.........*X",\
        "XXXXXXXXXXXX"]

    maze_2 =\
        ["XXXXXXXXXXXXX",\
        "X..G.G.G.G..X",\
        "X.G.G.G.G.G.X",\
        "X..G.G.G.G..X",\
        "X...........X",\
        "X...........X",\
        "X...........X",\
        "X.XX.XXX.XX.X",\
        "X.....*.....X",\
        "XXXXXXXXXXXXX"]

    maze_3 = \
        ["XXXXXXXXXXXXXXXXX",\
        "X...............X",\
        "X.XXXXX...XXXXX.X",\
        "X.X...........X.X",\
        "X.X....*......X.X",\
        "X.X...........X.X",\
        "X.XXXXXXXXXXXXX.X",\
        "X.......G.......X",\
        "XXXXXXXXXXXXXXXXX"]

    mazes = [maze_1, maze_2, maze_3]

    for maze in mazes:
        problem = MazeProblem(maze)
        solution = Pathfinder.solve(problem)
        # make sure its correct
        print("solution: ", len(solution))
