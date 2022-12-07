from abc import ABC


class Node(ABC):
    def __init__(self, name, type, parent=None, children=None, size=0):
        self.name = name
        self.type = type
        self.size = size
        self.parent = parent
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, children):
        self.children.extend(children)

    def get_total_size(self):
        """Recursively get the total size of the node and its children."""
        return self.size + sum(child.get_total_size() for child in self.children)


class Dir(Node):
    def __init__(self, name, parent=None, children=None):
        super().__init__(name, "dir", parent, children)


class File(Node):
    def __init__(self, name, size, parent=None):
        super().__init__(name, "file", parent, size=size)
