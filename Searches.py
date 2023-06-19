class Node(object):
    """This class represents a node in a graph."""

    def __init__(self, label: str = None):
        """
        Initialize a new node.

        Args:
            label: the string identifier for the node
        """
        self.label = label
        self.children = []

    def __lt__(self, other):
        """
        Perform the less than operation (self < other).

        Args:
            other: the other Node to compare to
        """
        return (self.label < other.label)

    def __gt__(self, other):
        """
        Perform the greater than operation (self > other).

        Args:
            other: the other Node to compare to
        """
        return (self.label > other.label)

    def __repr__(self):
        """Return a string form of this node."""
        return '{} -> {}'.format(self.label, self.children)

    def add_child(self, node, cost=1):
        """
        Add a child node to this node.

        Args:
            node: the node to add to the children
            cost: the cost of the edge (default 1)
        """
        edge = Edge(self, node, cost)
        self.children.append(edge)


class Edge(object):
    """This class represents an edge in a graph."""

    def __init__(self, source: Node, destination: Node, cost: int = 1):
        """
        Initialize a new edge.

        Args:
            source: the source of the edge
            destination: the destination of the edge
            cost: the cost of the edge (default 1)
        """
        self.source = source
        self.destination = destination
        self.cost = cost

    def __repr__(self):
        """Return a string form of this edge."""
        return '{}: {}'.format(self.cost, self.destination.label)


def depthLimited(node, goal, depth):
    if node.label == goal:
        return [node]
    elif depth == 0:
        return None
    else:
        for edge in node.children:
            result = depthLimited(edge.destination, goal, depth - 1)
            if result:
                result.insert(0, node)
                return result


def iterativeDeep(root, goal):
    depth = 0
    while True:
        result = depthLimited(root, goal, depth)
        if result:
            return result
        depth += 1


from queue import Queue


def bidirectional_search(start_node, end_node):
    # initialize the queues and visited sets for the start and end directions
    start_queue = Queue()
    start_visited = set()
    start_queue.put(start_node)
    start_visited.add(start_node)

    end_queue = Queue()
    end_visited = set()
    end_queue.put(end_node)
    end_visited.add(end_node)

    # initialize the parent dictionaries for the start and end directions
    start_parent = {}
    end_parent = {}
    start_parent[start_node] = None
    end_parent[end_node] = None

    # iterate over the two queues until a common node is found or both queues are empty
    while not start_queue.empty() and not end_queue.empty():
        # first, explore the start direction
        current_node = start_queue.get()
        for child_edge in current_node.children:
            child_node = child_edge.destination
            if child_node not in start_visited:
                start_queue.put(child_node)
                start_visited.add(child_node)
                start_parent[child_node] = current_node

            # if the child node has been visited from the end direction, return the path
            if child_node in end_visited:
                path = [child_node]
                while current_node is not None:
                    path.append(current_node)
                    current_node = start_parent[current_node]
                path.reverse()
                current_node = child_node
                while current_node is not None:
                    path.append(current_node)
                    current_node = end_parent[current_node]
                return path

        # second, explore the end direction
        current_node = end_queue.get()
        for child_edge in current_node.children:
            child_node = child_edge.destination
            if child_node not in end_visited:
                end_queue.put(child_node)
                end_visited.add(child_node)
                end_parent[child_node] = current_node

            # if the child node has been visited from the start direction, return the path
            if child_node in start_visited:
                path = [child_node]
                while current_node is not None:
                    path.append(current_node)
                    current_node = end_parent[current_node]
                path.reverse()
                current_node = child_node
                while current_node is not None:
                    path.append(current_node)
                    current_node = start_parent[current_node]
                return path

    # if no common node was found, there is no path
    return None


def ucs(root, goal):
    print("---UCS---")
    """
    Return the uniform cost search path from root to gaol.

    Args:
        root: the starting node for the search
        goal: the goal node for the search

    Returns: a list with the path from root to goal

    Raises: ValueError if goal isn't in the graph
    """
    # create a priority queue of paths
    queue = PriorityQueue()
    queue.put((0, [root]))
    # iterate over the items in the queue
    while not queue.empty():
        # get the highest priority item
        pair = queue.get()
        current = pair[1][-1]
        # if it's the goal, return
        if current.label == goal:
            return pair[1]
        # add all the edges to the priority queue
        for edge in current.children:
            # create a new path with the node from the edge
            new_path = list(pair[1])
            new_path.append(edge.destination)
            # append the new path to the queue with the edges priority
            queue.put((pair[0] + edge.cost, new_path))


if __name__ == '__main__':
    S = Node('S')
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    G = Node('G')

    # create all childs
    S.add_child(A, 1)
    S.add_child(G, 12)

    A.add_child(B, 3)
    A.add_child(C, 1)

    B.add_child(D, 3)

    C.add_child(D, 1)
    C.add_child(G, 2)
    D.add_child(G, 3)
    # show all the nodes
    _ = [print(node) for node in [S, A, B, C, D, G]]

    from queue import PriorityQueue

    print("UCS")
    print(ucs(S, 'G'))
    print("---Iterative Deepening Search---")
    print(iterativeDeep(S, 'G'))
    print("---Depth Limited Search---")
    print(depthLimited(S, 'G', 3))
    print("---Bidirectional Search---")
    print(bidirectional_search(S, G))