class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    find_recursive_path(root, sum, [], allPaths)
    return allPaths

def find_recursive_path(root, sum, currentpath, allPaths):
    if root is None:
        return False
    currentpath.append(root.val)
    if root.val == sum and root.left is None and root.right is None:
        allPaths.append(list(currentpath))
    else:
        find_recursive_path (root.right, sum - root.val, currentpath,allPaths)
        find_recursive_path (root.left, sum - root.val, currentpath,allPaths)
    del currentpath[-1]

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))

main()