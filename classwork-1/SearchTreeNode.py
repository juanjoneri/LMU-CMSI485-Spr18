class SearchTreeNode:

    def __init__(self, state, action, parent):
        self.state = state
        self.action = action
        self.parent = parent
        self.children = []
