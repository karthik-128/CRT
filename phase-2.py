class node:
    def __init__(self,data):
        self.data=data
        self.next=None
obj1 = node(71)
obj2 = node(72)
obj3 = node(73)
obj4 = node(74)
obj5 = node(75)
obj6 = node(76)
obj7 = node(77)
obj8 = node(78)
obj9 = node(79)
obj10 = node(80)

obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
obj9.next=obj10
currentNode = obj1 
while currentNode != None:
    print(currentNode.data, end = " --> ")
    currentNode = currentNode.next





#searching
    class Node:
        def __init__(self, data):
            self.data = data 
            self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
    printLinkedList(head)
print("Final linked list is:")
printLinkedList(head)




#oidfun98
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head
 
# Task - 1
def insertAtHead(head, ele):
    temp = Node(ele)
    temp.next = head 
    return temp
 
# Task - 2
def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtHead(head, ele)
 
    temp = Node(ele)
    index = 0 
    currentNode = head 
 
    while index != position - 1:
        currentNode = currentNode.next 
        index += 1 
 
    nextNode = currentNode.next 
    temp.next = nextNode 
    currentNode.next = temp 
    return head
 
 
 
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
print("Final linked list is:")
printLinkedList(head)
 
head =insertAtSpecificPosition(head, 3, 101)
printLinkedList(head)




 #delete tail node
def deleteTailNode(head):
    if head == None or head.next == None:
        return None
    previous = None
    currentNode = head
    while currentNode.next != None:
        previous = currentNode
        currentNode = currentNode.next
    previous.next = None
    return head
#task1
def deleteHeadNode(head):
    if head == Node:
        return head
    secondNode = head.next
    head.next = None
    return secondNode


#day2
# Stack implementation 
 
def push(stack, ele):
    stack.append(ele)
    print(ele, "inserted into stack successfully")
 
def pop(stack):
    if len(stack) == 0:
        print("Stack is empty")
        return 
    print(stack[-1], "deleted successfully")
    stack.pop()
 
stack = [] 
push(stack, 10)
push(stack, 20)
# [10, 20]
push(stack, 30)
push(stack, 40)
# [10, 20, 30, 40]
 
pop(stack)
# [10, 20, 30]
pop(stack)
# [10, 20]
pop(stack)
# [10]
pop(stack)
# []
pop(stack)
# []
#own trail
def push(stack,ele):
    stack.append(ele)
    print(ele,"inserted into stack successfully")

def pop(stack):
    if len(stack) == 0:
        print("stack is empty")
        return
    print(stack[-1],"deleted successfully")
    stack.pop()

stack = []
push(stack, 10)
push(stack, 20)
push(stack, 30)
push(stack, 40)


#QUEUES
def enQueue(Q, ele):
    Q.append(ele)
    print(ele,"inserted into Queue")
    
def deQueue(Q):
    if len(Q) == 0:
        print("Queue is empty")
        return
    print(Q[0],"is getting deleted")
    Q.pop(0)
#jvwoij
def enQueue(Q, ele):
    Q.append(ele)
    print(ele, "inserted into Queue")
 
def deQueue(Q):
    if len(Q) == 0:
        print("Queue is empty")
        return 
    print(Q[0], "is getting deleted")
    Q.pop(0)
 
# Queue implementation 
 
Q = []
enQueue(Q, 10)
enQueue(Q, 20)
enQueue(Q, 30)
enQueue(Q, 40)
enQueue(Q, 50)
 
print(Q)
 
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
#comment
def isBalanced(word):
    stack = []
    for ele in word:
        if ele == '(':
            stack.append(ele)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    return False
word = "()("
result = isBalanced(word)
print(result)
#iusdhvueofh
nums = [12,10,6,23,123]
target = 23
num = sorted(nums)

left = 0 
right = len(nums) - 1
flag = -1

while left <= right:
    mid = (left + right)//2
    if num[mid] == target:
        flag = mid
        break
    elif num[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
if flag == -1:
    print("target not found")
else:
    print("target found at index ",flag)


#SORTING
def performBubblesort(nums):
    n = len(nums)
    fixThisindex = n - 1
    while fixThisindex > 0:
        for index in range(fixThisindex):
            if nums[index] > nums[index + 1]:
                temp = nums[index]
                nums[index] = nums[index + 1]
                nums[index + 1] = temp
        print(nums)
        fixThisindex = 1
nums = [10,8,2,14,12,7]
print("Before sorting:",nums)

performBubblesort(nums)

print("After sorting:",nums)
#second
def performSelectionSort(num):
    n = len(nums)
    fixThisindex = n - 1
    while fixThisindex > 0:
        maxeleindex = fixThisindex

        for index in range(fixThisindex):
            if num[index] > num[maxeleindex]:
                maxeleindex = index
            if maxeleindex != fixThisindex:
                temp = nums[maxeleindex]
                nums[maxeleindex] = nums[fixThisindex]
                nums[fixThisindex] = temp
            print(nums)
            fixThisindex = 1
#third
def mergetwosubarrays(nums,left,mid,right):
    temp = []
    index1 = left
    index2 = mid + 1
    while index1 <= mid and index2 <= right:
        if nums[index1] < nums[index2]:
            temp.append(nums[index1])
            index1 += 1
        else:
            temp.append(nums[index2])
            index2 += 1
    while index1 <= mid:
        temp.append(nums[index2])
        index2 += 1
    position = left 
    for ele in temp:
        nums[position] = ele 
        position += 1 
 
    position = left 
    for ele in temp:
        nums[position] = ele 
        position += 1 

#day 4
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =None

obj1 = Node(100)
obj2 = Node(21)
obj3 = Node(-151)
obj4 = Node(87)
obj5 = Node(12)
obj6 = Node(52)
obj7 = Node(8)
obj8 = Node(27)
obj9 = Node(28)
obj10 = Node(7)


obj1.left = obj2
obj1.right = obj3
obj2.left = obj4
obj2.right = obj5
obj3.left = obj6
obj3.right = obj7
obj4.right = obj8
obj5.right = obj9
obj7.left = obj10
 
 #second
class Solution(object):
    def preorderhelper(self,root, result):
        if root == None:
            return
        result.append(root.val)
        self.preorderhelper(root.left, result)
        self.preorderhelper(root.right, result)
    def preorderTraversal(self,root):
        result = []
        self.preorderHelper(root,result)
        return result

#day 5
#TREES  
class TreeNode:
    def __init__(self, data):
        self.val = data 
        self.left = None 
        self.right = None
 
def printInorder(root):
    if root == None:
        return 
    # 1 
    printInorder(root.left)
    # 2 
    print(root.val, end = ", ")
    # 3
    printInorder(root.right)
 
 
def insertIntoBST(root, val):
    if root == None:
        return TreeNode(val)
    elif root.val > val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
 
nums = [10, 8, 12, 5, 23, 20]
root = None
for ele in nums:
    root = insertIntoBST(root, ele)
printInorder(root)


#deletion node
def deleteNodeFromBST(root, val):
    if root == None:
        return None 
    elif root.val > val:
        # If root value is greater than node to be deleted
        root.left = deleteNodeFromBST(root.left, val)
    elif root.val < val:
        # If root value is lesser than node to be deleted
        root.right = deleteNodeFromBST(root.right, val)
    else:
        # If root value is equal to node to be deleted
 
        # category-1 (Node with 0 children)
        if root.left == None and root.right == None:
            return None
 
        # category-2 (Node with 1 children) 
        if root.left == None:
            return root.right 
        elif root.right == None:
            return root.left
 
        # category-3 (Node with 2 children)
        # Finding inorder successor 
        curr = root.right 
        while curr.left != None:
            curr = curr.left 
 
        # Once inorder successor is found, we need to replace the value 
        root.val = curr.val 
        root.right = deleteNodeFromBST(root.right, curr.val)
    return root
#Adjacency Matrix
n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = [0] * n 
    [0, 0, 0, 0, 0]
    matrix.append(row)
 
    print(matrix)  
for i in range(m):
   u, v = map(int, input().split())
   matrix[u][v] = 1 
   matrix[v][u] = 1  
 
print(matrix)
 
 
# Adjacency List Construction 
n, m = map(int, input().split())
adj = [] 
for i in range(n):
    adj.append([])
 
print(adj)
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
print(adj)
 #dfge
nums = [10, 8, 12, 5, 23, 20, 43, 23, 11, 7]
root = None
for ele in nums:
    root = insertIntoBST(root, ele)
printInorder(root)
root = deleteNodeFromBST(root, 20)
printInorder(root)

#Graphs
def initiateBFSTraversal(node, visited, adj, result):
    Q = [node]
    visited[node] = True 
 
    while len(Q) > 0:
        curr = Q.pop(0)
        result.append(curr)
        for neighbour in adj[curr]:
            if visited[neighbour] == False:
                visited[neighbour] = True 
                Q.append(neighbour)
 
 
def printBFSTraversal(adj, n):
    visited = [False] * n 
    result = []
    for node in range(n):
        if visited[node] == False:
            initiateBFSTraversal(node, visited, adj, result)
 
    print("BFS traversal is: ", result)
#HGVYU
def initiateDFSTraversal(node, visited, adj, result):
    result.append(node)
    visited[node] = True 
 
    for neighbour in adj[node]:
        if visited[neighbour] == False:
            initiateDFSTraversal(neighbour, visited, adj, result)
 
def printDFSTraversal(adj, n):
    visited = [False] * n 
    result = []
    for node in range(n):
        if visited[node] == False:
            initiateDFSTraversal(node, visited, adj, result)
 
    print("DFS traversal is: ", result)
 
 
# Adjacency List Construction 
n, m = map(int, input().split())
adj = [] 
for i in range(n):
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
# printBFSTraversal(adj, n)
printDFSTraversal(adj, n)

 
 
 
 





 
 
 

