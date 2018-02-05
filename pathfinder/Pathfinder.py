"""
Natalia Dibbern
Juan Neri
"""

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest

class Pathfinder:

    def solve(problem):
        deb_count = 1 # for report
        current_node = SearchTreeNode(problem.initial, None, None)
        q = [current_node]
        while not problem.goal_test(current_node.state):
            current_node = q.pop(0)
            children = problem.transitions(current_node.state)
            for child in children:
                child_action, child_state = child
                child_node = SearchTreeNode(child_state, child_action, current_node)
                q.append(child_node)
                deb_count += 1

        path = []
        while current_node.parent != None:
            path.append(current_node.action)
            current_node = current_node.parent

        print("count: ", deb_count)
        return list(reversed(path))


class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", \
                "XG..X", \
                "XX..X", \
                "X*..X", \
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze3(self):
        maze = ["XXXXXXXXXXXX",\
                "XG.......XGX",\
                "X...XXX..X.X",\
                "X...XGX..X.X",\
                "X...XXX..X.X",\
                "X.......XX.X",\
                "X..........X",\
                "X......XXXXX",\
                "X.........*X",\
                "XXXXXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 15)

    # TODO: Add more unit tests!

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
