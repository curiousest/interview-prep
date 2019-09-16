# Purpose

To prepare for programming problems.

# Practice Problems

I attempt problems, usually with a time limit. 90% of the problems I attempt aren't "finished" within the time limit. I review "the correct solution" afterwards.

I've found that programming tests fall into one of the following categories:

* "Use the applicable data structure" problems
    * Trees & Graphs (binary trees, tries, b-trees, graphs)
        * Search (breadth-first, depth-first)
    * Hashmaps
    * Arrays (arrays, sets, queues/stacks, heaps)
        * Search (binary)
        * Sort (merge, quick, radix)
    * Linked lists
* Dynamic programming problems
* Math problems

# Dynamic programming base problems/solutions

Many dynamic programming problems roughly reduce to these problems, so their solutions are useful inspiration. Edge cases to these problems aren't described here.

## Memoization (top-down recursion)

### Problem

The problem can be solved by recursively solving smaller sub-problem(s) of the same type. The output of a problem is always the same for a given set of inputs. The sub-problems must be solved multiple times in the tree of recursive calls.

### Solution

Memoize the recursive call to solving subproblems.

```python3
from functools import lru_cache

@lru_cache(maxsize=None)
def recursive_problem(*args):
    subproblems = get_subproblems(args)
    results = [recursive_problem(*params) for params in subproblems]
    return combine_results(results)
```

## Backtracking (bottom-up tabulation)

### Problem

The problem can be solved by building a tree of alternative possibilities. All descendents of a node of the tree can be pruned by evaluating that node alone.

### Solution

Store a priority queue of nodes (possible solutions) to explore. Continually dequeue from the priority queue, evaluate:

1. Whether a solution has been reached.
2. Whether the node is part of a possible solution (whether the node can be pruned). If it is part of a possible solution, add all of its children to the priority queue.

```python3
q = empty_priority_queue()
q.enqeue(base_case)

while q is not empty:
    node = q.dequeue()
    if solution_reached(node):
        return solution(node)
    if part_of_possible_solution(node):
        for child in children(node):
            q.enqueue(child)
return solution_not_reached()

```

## Shortest path (Bellman-Ford)

### Problem

Edges in a graph have a cost to traverse. What is the smallest cost to traverse from vertex A to vertex B?

### Solution

Start with the distance of each vertex except the source equal to infinity. For each edge in the graph check if it reduces the distance to the destination vertex and update. Do this `len(vertices) - 1` times.

Time: O(VE)

Space: O(V+E)

```python3
for v in vertices:
    distance[v] = infinity

distance[source] = 0

for _ in range(vertices-1):
    for source, destination, weight in edges:
        distance[destination] = min(distance[destination], distance[source] + weight)
result = distance[final_destination]
```

## 0-1 Knapsack

### Problem

Given a set of items, each with a weight and a value how many of each item should be included in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

### Solution

For each item i with weight t and value v, for each weight leading up to the actual knapsack weight (w in 0..W): either include the item or exclude it starting from i=0, w=0. To decide whether to include at each (i, w), compare value(i-1, w) to value(i, w-t) + v. Either exclude the item and consider what happened with previous items or combine the item with the maximum value achieved with the rest of the available space.

Time: O(nW)

Space: O(nW)

```python3
value = [[0 for w in range(W + 1)] for i in range(items)]

for i, item_weight, item_value in items:
    for w in range(knapsack_weight + 1):
        if item_weight > w:
            value[i][w] = value[i-1][w]
        else:
            value[i][w] = max(value[i-1][w], value[i][w-item_weight] + item_value)

result = value[-1][-1]
```

## Edit distance (Levenshtein distance)

### Problem

Edit distance is a way of quantifying how dissimilar two lists of symbols are to one another by counting the minimum number of operations required to transform one into the other.

Convert list X[1..m] to list Y[1..n] by performing edit operations on X.

### Solution

Convert X[1..i] to Y[1..j] by performing edit operations on X, for every combination of i in 0..m, j in 0..n starting from i=0, j=0.

Case 1: i=0 or j=0. Distance is `max(i, j)`.

Case 2: i>0 and j>0. The distance from X[1..i-1] to Y[1..j] has been computed already. The distance from X[1..i] to Y[1..j-1] has been computed already. The difference between those two subproblems and X[1..i] to Y[1..j] is one additional character. Figure out what operation must happen to get from those subproblems to the current problem, and pick the smallest resulting distance: `min(distance(i-1, j) + O1, distance(i, j-1) + O2)`

Time: O(mn)

Space: O(mn)

```python3

computed = [[0 for i in range(len(m + 1))] for j in range(len(n + 1))]

for i in range(1, len(n) + 1):
    for j in range(1, len(m) + 1):
        option_1 = computed[i-1][j] + cost_of_operation((i, j), (i-1, j))
        option_2 = computed[i][j-1] + cost_of_operation((i, j), (i, j-1))
        computed[i, j] = min(option_1, option_2)

result = computed[n,m]
```
