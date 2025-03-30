class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    
    def print(self):
        if self.head is None:
            print("Linked list Empty")
            return
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")
        
    def get_len(self):
        count = 0
        temp = self.head
        while temp:
            count +=1 
            temp = temp.next
            
        return count
            
            

        
    def insertBeg(self,data):
        newNode = Node(data)
        if self.he             is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode
        
    def insertEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        
    def remove(self,index):
        if index<0 or index>=self.get_len():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        curr_temp = self.head
        prev_temp = None
        while count<index:
            prev_temp = curr_temp
            curr_temp = curr_temp.next
            count += 1
            
        prev_temp.next = curr_temp.next
        curr_temp.next = None
        
    def insert_at(self,index,data):
        if index<0 or index>self.get_len():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insertBeg(data)
            return
        
        count = 0
        curr_temp = self.head
        prev_temp = None
        while count<index:
            prev_temp = curr_temp
            curr_temp = curr_temp.next
            count += 1
            
        newNode = Node(data)
        prev_temp.next = newNode
        newNode.next = curr_temp
        
    def insert_values(self,values):
        for value in values:
            self.insertEnd(value)
            
        return self.head
        
    def insert_after_value(self,data_after,data_to_insert):
        temp = self.head
        newNode = Node(data_to_insert)
        while temp:
            if temp.data == data_after: 
                address = temp.next
                temp.next = newNode
                newNode.next = address
                return
                
            temp =temp.next
    def print_reverse(self,temp):
        if temp == None:
            return
        self.print_reverse(temp.next)
        print(temp.data,end="-->")
        return None
                

            
            

        
if __name__ == "__main__":
    # ll = LinkedList()
    # ll.insertBeg(1)
    # ll.insertEnd(7)
    # ll.insertBeg(2)
    # ll.insertBeg(3)
    # ll.insertBeg(4)
    # ll.print()
    # print(ll.get_len())
    # ll.remove(4)
    # ll.print()
    # ll.insert_at(2,25)
    # ll.print()
    # ll.insert_at(0,26)
    # ll.print()
    ll = LinkedList()
    head = ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    # ll.insert_after_value("mango","apple") # insert apple after mango=
    print(ll.print_reverse(head))


        
        
            
            