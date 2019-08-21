"""
Given a list of TreeNodes. TreeNode is standard LC class:

class TreeNode {
    TreeNode left;
    TreeNode right;
    int val;
}
Find out if all these nodes belong to the same valid binary tree.

public boolean isBinaryTree(List<TreeNode> nodes) {
}


	 1
	⤤ ⤦
	 2

TreeNode n1 = new TreeNode(1);
TreeNode n2 = new TreeNode(2);

n1.left = n2;
n2.left = n1;

Input: [n1, n2]
Output: false

If any node has in-degree more than 1 or out degree more than 2, it's not a tree (example 2)
If a cycle exists in the directed graph, it's not a tree (example 3)
If there are one or more graphs, separated from each other, it's not a tree, probably two or more tree (example 4)
Else, it's definitely a tree.
"""
def hasCycle(node, seen = set()):
    if node in seen: return True
    seen.add(node)
    if node.left and hasCycle(node.left, seen):
        return True
    if node.right and hasCycle(node.right, seen):
        return True
    return False


def detect_cycle(graph, start):
    """Traverse the graph, and see if we come back to a earlier visited vertex."""

    if graph is None:
        raise ValueError("We need a graph to detect cycles in")

    # Set all vertexes to None, as we don't know the status of it
    visited = {v : False for v in graph}

    stack = [start]

    # Traverse from start, adding connected nodes to the stack as we go
    while stack:
        vertex = stack.pop()

        # If we hit a vertex we've seen before, it is a cycle
        if visited[vertex]:
            return True

        # Mark this vertex as visited
        visited[vertex] = True

        # Add connected nodes to stack, if any
        stack.extend(graph[vertex])

    # If stack is empty, that means no cycle for this start vertex
    return False


def cycle_exists(graph):
    """Return whether the graph has cycles or not."""

    # Loop through each vertex, and check if it has cycles or not
    for vertex in graph:
         if detect_cycle(graph, vertex):
             return True

    return False