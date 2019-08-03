import queue

class Codec:


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        node_q = queue.Queue()
        node_q.put(root)
        serialized_tree = ""

        while(not node_q.empty()):
            curr_node = node_q.get()
            if curr_node:
                print(curr_node.val)
            print('===')

            if curr_node is not None:
                serialized_tree += str(curr_node.val)
                node_q.put(curr_node.left)
                node_q.put(curr_node.right)
            else:
                serialized_tree += 'null'
            if not node_q.empty():
                serialized_tree += ','

        return serialized_tree

    def dequeue_from_encoded(self, data):
        next_occ = data.find(',')
        next_item = data[:next_occ] if next_occ != -1 else data
        data = data[next_occ + 1:] if next_occ != -1 else ''
        try:
            return int(next_item), data
        except ValueError:
            return None, data

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_q = queue.Queue()
        item, data = self.dequeue_from_encoded(data)
        root = TreeNode(item)
        if item is not None:
            node_q.put(root)
        while(not(node_q.empty())):
            curr_node = node_q.get()

            item, data = self.dequeue_from_encoded(data)
            if item is not None:
                curr_node.left = TreeNode(item)
                node_q.put(curr_node.left)
            
            item, data = self.dequeue_from_encoded(data)
            if item is not None:
                curr_node.right = TreeNode(item)
                node_q.put(curr_node.right)
            print_tree(root)
            print('---')
        return root
            
def print_tree(node):
    print(node.val)
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


        

# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.serialize(codec.deserialize("1,2,3,null,null,4,5")))