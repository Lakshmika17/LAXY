class Node:  
    def __init__(self,data):   
        self.data = data  
        self.left = None  
        self.right = None  

class BinaryTree:  
    def __init__(self):  
        self.root = None
    def insertNode(self, data):    
        newNode = Node(data)
        if(self.root == None):  
            self.root = newNode  
            return  
        else: 
            queue = []  
            queue.append(self.root)                
            while(True):  
                node = queue.pop(0)  
                if(node.left != None and node.right != None):  
                    queue.append(node.left) 
                    queue.append(node.right) 
                else:  
                    if(node.left == None):  
                        node.left = newNode  
                        queue.append(node.left)
                    else:  
                        node.right = newNode;  
                        queue.append(node.right)  
                    break;  
                       
    
    def preorderTraversal(self, node):            
        if(self.root == None):  
            print("Tree is empty") 
            return 
        else:
            print(node.data)
            if(node.left != None):  
                self.preorderTraversal(node.left)    
            if(node.right!= None):  
                self.preorderTraversal(node.right)

    
bt = BinaryTree();  
bt.insertNode(5);    
bt.insertNode(6);  
bt.insertNode(7);
bt.insertNode(8);  
bt.insertNode(9);


print("Binary tree in preorder traversal after insertion");   
bt.preorderTraversal(bt.root);

