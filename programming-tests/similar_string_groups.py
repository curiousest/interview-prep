from typing import List

def a(inp, answer_func, sol):
    print('-------------')
    result = answer_func(inp)
    if result != sol:
        print('Input: ', inp)
        print('Real answer: ', sol)
        print('Answer: ', result)
    else:
        print('Correct ', result)

def strings_two_off(str1, str2):
    num_different = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            num_different += 1
            if num_different > 2:
                return False
    return True

def explore_acyclic_graph(graph, parent_node):
    node_items = graph[parent_node]
    del graph[parent_node]
    for item in node_items:
        if item in graph:
            graph[item].remove(parent_node)
            explore_acyclic_graph(graph, item)

class Solution:

    def numSimilarGroups(self, A: List[str]) -> int:
        base_list = list(set(A))

        # build acyclic graph
        graph = {item: set() for item in base_list}
        for index, item in enumerate(base_list):
            for other_item in base_list[index + 1:]:
                if strings_two_off(item, other_item):
                    graph[item].add(other_item)
                    graph[other_item].add(item)
        

        # explore graph
        groups_count = 0
        for item in base_list:
            if item in graph:
                print(graph)
                groups_count += 1
                explore_acyclic_graph(graph, item)
        return groups_count


s = Solution()

a(["tars","rats","arts","star"], s.numSimilarGroups, 3)
a(["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"], s.numSimilarGroups, 5)

