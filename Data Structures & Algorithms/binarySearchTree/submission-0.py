class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left == None:
                    cur.left = newNode
                    return
                cur = cur.left
            elif key > cur.key:
                if cur.right == None:
                    cur.right = newNode
                    return
                cur = cur.right
            else:
                cur.val = val
                return

    def get(self, key: int) -> int:

        cur = self.root
        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        cur = self.findMin(self.root)
        return cur.val if cur else -1

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node


    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val if cur else -1


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, cur, key):
        if cur == None:
            return None
        
        if key > cur.key:
            cur.right = removeHelper(cur.right, key)
        elif key < cur.key:
            cur.left = removeHelper(cur.left, key)
        else:
            if not cur.left:
                return cur.right
            if not cur.right:
                return cur.left
            else:
                minNode = self.findMin(cur.right)
                cur.key = minNode.key
                cur.val = minNode.val
                cur.right = self.removeHelper(cur.right, minNode.key)
        return cur


    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root, result):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
