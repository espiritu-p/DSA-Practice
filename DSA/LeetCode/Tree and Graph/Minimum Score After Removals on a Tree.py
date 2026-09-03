import collections
import math
from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = collections.defaultdict(
            list
        )  # key-value pairs where key is the node and value is a list of nodes it can traverse to
        children = collections.defaultdict(
            set
        )  # key-value pairs where key is the node and value is a set of its children
        subtree_xor = nums[:]  # contains the xor sum of a subtree
        degree = [0] * len(nums)  # number of edges linked to the node

        # initialize the graph containing key-value pairs; where key is the node and the value contains a list of nodes it can traverse to
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1

        root_xor = 0  # xor value of all nodes

        visited = set()
        dq = collections.deque()

        # iterate through all the nodes and calculate total XOR of tree
        for i in range(len(nums)):
            root_xor ^= nums[i]

            # add the leaf nodes to the deque where we'll start up to the root node
            if degree[i] == 1:
                dq.append(i)
                visited.add(i)

        # traverse through the tree starting from the leaf nodes
        while dq:
            cur_node = dq.popleft()

            for next_node in graph[cur_node]:
                if (
                    next_node not in visited
                ):  # if the next node was not visited yet, it is the parent node of current node
                    children[next_node].add(
                        cur_node
                    )  # add the current node as a child of next node
                    children[next_node] |= children[
                        cur_node
                    ]  # union operation to include child node
                    subtree_xor[next_node] ^= subtree_xor[
                        cur_node
                    ]  # update xor value of parent with child node
                degree[next_node] -= 1  # decrement degree of a node after visiting

                if degree[next_node] == 1:  # only the parent node remains to be visited
                    visited.add(next_node)  # pre-set parent node to visited
                    dq.append(next_node)  # add parent node to the queue

        ans = (
            math.inf
        )  # set to highest possible value since we want to store the minimum value

        for i in range(len(edges) - 1):  # iterate through all edges
            for j in range(
                i + 1, len(edges)
            ):  # iterate through all edges not including the current edge
                a, b = edges[i]  # get nodes a and b from the current edge

                if b in children[a]:  # swap a and b if b is a child of a
                    a, b = b, a

                c, d = edges[j]  # get nodes c and d from the another edge

                if d in children[c]:  # swap c and d if d is a child of c
                    c, d = d, c

                """
                NOTE:
                xor of root and xor of subtree a gives the values of the remaining nodes since:
                root_xor = subtree_xor[a] ^ subtree_root_xor_remaining_nodes
                root_xor ^ subtree_xor[a] = subtree[a] ^ subtree_xor_remaining_nodes ^ subtree_xor[a] (xor subtree_xor[a] both sides)
                root_xor ^ subtree_xor[a] = subtree_root_xor_remaining_nodes (since the xor of a number with itself is 0)

                same idea with subtree_xor[a] ^ subtree_xor[c] and vice versa since:
                subtree_xor[a] ^ subtree_xor[c] = node_a_value ^ subtree_xor[a]_remaining_nodes ^ subtree_xor[c]
                subtree_xor[a] ^ subtree_xor[c] ^ subtree_xor[c] = node_a_value ^ subtree_xor[a]_remaining_nodes ^ subtree_xor[c] ^ subtree_xor[c] (xor subtree_xor[c] both sides)
                subtree_xor[a] = node_a_value ^ subtree_xor[a]_remaining_nodes
                """
                # Case 1: subtree c is a child of subtree a
                if c in children[a]:

                    cur = [
                        subtree_xor[c],
                        subtree_xor[a] ^ subtree_xor[c],
                        root_xor ^ subtree_xor[a],
                    ]
                # Case 2: subtree a is a child of subtree c
                elif a in children[c]:
                    cur = [
                        subtree_xor[a],
                        subtree_xor[c] ^ subtree_xor[a],
                        root_xor ^ subtree_xor[c],
                    ]
                # Case 3: subtree a and subtree c are independent trees
                else:
                    cur = [
                        subtree_xor[a],
                        subtree_xor[c],
                        root_xor ^ subtree_xor[a] ^ subtree_xor[c],
                    ]

                # calculate the minimum score after removing the two edges
                ans = min(ans, max(cur) - min(cur))

        return ans
