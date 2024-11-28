from Tree import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root
    
    def is_empty(self):
        return self.root is None

    def insert_left(self, target_val, val):
        new_node = TreeNode(val)
        target_node = self.find(target_val)
        
        if target_node and not target_node.left:
            target_node.left = new_node

    def insert_right(self, target_val, val):
        new_node = TreeNode(val)
        target_node = self.find(target_val)
        
        if target_node and not target_node.right:
            target_node.right = new_node
    
    def insert(self, val):
        new_node = TreeNode(val)
        
        if not self.root:
            self.root = new_node
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            
            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)
            
            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)
    
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.val, end=" ")
            self.in_order_traversal(node.right)
    
    def pre_order_traversal(self, node):
        if node:
            print(node.val, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
    
    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.val, end=" ")
    
    def level_order_traversal(self):
        if not self.root:
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    def find(self, val):
        if not self.root:
            return None
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            
            if node.val == val:
                return node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return None
    
    def children(self, val):
        node = self.find(val)
        if node:
            children_list = []
            if node.left:
                children_list.append(node.left.val)
            if node.right:
                children_list.append(node.right.val)
            return children_list if children_list else None
        else:
            return None
    
if __name__=='__main__':
    bt = BinaryTree()

    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    bt.insert(6)
    bt.insert(7)

    print("In-order Traversal:")
    bt.in_order_traversal(bt.root)
    print("\nPre-order Traversal:")
    bt.pre_order_traversal(bt.root)
    print("\nPost-order Traversal:")
    bt.post_order_traversal(bt.root) 
    print("\nLevel-order Traversal:")
    bt.level_order_traversal()

    val_to_find = 5
    node = bt.find(val_to_find)
    if node:
        print(f"\nNode with value {val_to_find} found.")
    else:
        print(f"\nNode with value {val_to_find} not found.")
