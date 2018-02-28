import unittest
from collections import Counter

class MazeClause:

    def __init__(self, props):
        self.props = {}
        self.valid = False
        # ("X", (1, 1)), True)
        for coord, status in props:
            if coord not in self.props:
                self.setProp(coord, status)
            elif status != self.getProp(coord):
                self.delProp(coord)
                self.valid = True

    @classmethod
    def emptyClause(cls):
        return cls([])

    def setProp(self, coord, status):
        self.props[coord] = status

    def delProp(self, coord):
        del self.props[coord]

    def getProp(self, coord):
        try:
            return self.props[coord]
        except:
            return None

    def isValid(self):
        return self.valid

    def isEmpty(self):
        return not any(self.props)

    def __eq__(self, other):
        return self.props == other.props \
           and self.valid == other.valid

    def __hash__(self):
        return hash(frozenset(self.props.items()))

    def __str__ (self):
        return f'Valid: {self.valid}\nProps: {self.props}'

    @staticmethod
    def _invert(prop):
        coord, status = prop
        return (coord, not status)

    @staticmethod
    def _remove_inverse(props):
        altered = False # Flag to check if something changed
        for prop in props:
            inverse_prop = MazeClause._invert(prop)
            if inverse_prop in props:
                props -= {prop, inverse_prop}
                altered = True
                break
        return props, altered

    @staticmethod
    def resolve(clause_1, clause_2):
        if clause_1.isEmpty() or clause_2.isEmpty() or\
           clause_1.isValid() or clause_2.isValid():
            return set()

        union = set(clause_1.props.items()) | set(clause_2.props.items())
        resolution, altered = MazeClause._remove_inverse(union)
        new_clause = MazeClause(resolution)

        if not altered or new_clause.isValid():
            return set()
        else:
            return {new_clause}



class MazeClauseTests(unittest.TestCase):
    def test_mazeprops1(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (2, 1)), True), (("Y", (1, 2)), False)])
        self.assertTrue(mc.getProp(("X", (1, 1))))
        self.assertTrue(mc.getProp(("X", (2, 1))))
        self.assertFalse(mc.getProp(("Y", (1, 2))))
        self.assertTrue(mc.getProp(("X", (2, 2))) is None)
        self.assertFalse(mc.isEmpty())

    def test_mazeprops2(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (1, 1)), True)])
        self.assertTrue(mc.getProp(("X", (1, 1))))
        self.assertFalse(mc.isEmpty())

    def test_mazeprops3(self):
        mc = MazeClause([(("X", (1, 1)), True), (("Y", (2, 1)), True), (("X", (1, 1)), False)])
        self.assertTrue(mc.isValid())
        self.assertFalse(mc.getProp(("X", (1, 1))))
        self.assertFalse(mc.isEmpty())

    def test_mazeprops4(self):
        mc = MazeClause([])
        self.assertFalse(mc.isValid())
        self.assertTrue(mc.isEmpty())

    def test_mazeprops5(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)
    #
    def test_mazeprops6(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([]) in res)

    def test_mazeprops7(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (2, 2)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([(("Y", (1, 1)), True), (("Y", (2, 2)), True)]) in res)

    def test_mazeprops8(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)

    def test_mazeprops9(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0) # changed from 0 to 1

    def test_mazeprops10(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), False), (("W", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([(("Y", (1, 1)), False), (("Z", (1, 1)), True), (("W", (1, 1)), False)]) in res)

if __name__ == "__main__":
    unittest.main()
