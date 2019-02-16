import sys
import io
import json

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self.left is None:
            sl = "-"
        else:
            sl = str(self.left)

        if self.right is None:
            sr = "-"
        else:
            sr = str(self.right)

        if self.next is not None:
            n = "->" + str(self.next.val)
        else:
            n = ""

        return ("{" + str(self.val) + n + "," +
                sl + "," +
                sr + "}")

    def new(x):
        if x:
            return TreeNode(x)
        else:
            return None

    def make(a):
        t = [TreeNode.new(x) for x in a]
        return TreeNode.make_sub(t, level=0)

    def make_sub(a, level=0):
        if a[level]:
            print("Check", level)
            tn = a[level]
            if 2*level+1 < len(a):
                tn.left = a[2*level+1]
                TreeNode.make_sub(a, 2*level+1)
            if 2*level+2 < len(a):
                tn.right = a[2*level+2]
                TreeNode.make_sub(a, 2*level+2)
        return a[level]


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None
    inputValues = [s.strip() for s in input.split(',')]
    return intArrToTreeNode(inputValues)


def arrayToTreeNode(inputValues):
    if len(inputValues) == 0:
        return None
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item is not None:
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item is not None:
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);

            ret = Solution().inorderTraversal(root)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == "__main__":
    tn = arrayToTreeNode([1, None, 2, 3])
    print(tn)
