class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListException(Exception):
    #Custom exception class for linked list operations
    pass


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        
        # If list is empty, make new node the head
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        
        # Add new node at the end
        current.next = new_node
    
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("List: " + " -> ".join(elements))
    
    def delete_nth_node(self, n):
        if not self.head:
            raise LinkedListException("Cannot delete from an empty list")
        
        if n < 1:
            raise LinkedListException("Index must be greater than 0")
        
        # Delete first node
        if n == 1:
            self.head = self.head.next
            return
        
        # Find the node before the one to delete
        current = self.head
        for i in range(1, n - 1):
            if not current.next:
                raise LinkedListException(f"Index {n} is out of range")
            current = current.next
        
        # Check if the node to delete exists
        if not current.next:
            raise LinkedListException(f"Index {n} is out of range")
        
        # Delete the node
        current.next = current.next.next
    
    def get_size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None


def display_menu():
    print("\n" + "="*40)
    print("     SINGLY LINKED LIST OPERATIONS")
    print("="*40)
    print("1. Add node to list")
    print("2. Print list")
    print("3. Delete nth node")
    print("4. Get list size")
    print("5. Check if list is empty")
    print("6. Run sample test")
    print("7. Exit")
    print("="*40)


def run_sample_test():
    """Run a sample test of the linked list"""
    print("\n" + "="*30)
    print("    RUNNING SAMPLE TEST")
    print("="*30)
    
    # Create a new linked list
    test_list = LinkedList()
    
    # Test adding nodes
    print("Adding nodes: 10, 20, 30, 40, 50")
    for value in [10, 20, 30, 40, 50]:
        test_list.add_node(value)
    
    # Print the list
    test_list.print_list()
    print(f"List size: {test_list.get_size()}")
    
    # Test deleting nodes
    try:
        print("\nDeleting node at position 3 (value 30)")
        test_list.delete_nth_node(3)
        test_list.print_list()
        
        print("\nDeleting node at position 1 (value 10)")
        test_list.delete_nth_node(1)
        test_list.print_list()
        
        print(f"List size after deletions: {test_list.get_size()}")
        
    except LinkedListException as e:
        print(f"Error: {e}")
    
    # Test edge cases
    print("\nTesting edge cases:")
    try:
        print("Attempting to delete node at position 10 (out of range)")
        test_list.delete_nth_node(10)
    except LinkedListException as e:
        print(f"Caught expected error: {e}")
    
    print("Sample test completed!")


def main():
    linked_list = LinkedList()
    
    print("Welcome to the Singly Linked List Program!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                try:
                    data = input("Enter data to add: ")
                    try:
                        data = int(data)
                    except ValueError:
                        pass  # Keep as string if not a number
                    
                    linked_list.add_node(data)
                    print(f"Added '{data}' to the list")
                    
                except Exception as e:
                    print(f"Error adding node: {e}")
            
            elif choice == '2':
                linked_list.print_list()
            
            elif choice == '3':
                try:
                    n = int(input("Enter position to delete (1-based): "))
                    linked_list.delete_nth_node(n)
                    print(f"Deleted node at position {n}")
                    
                except ValueError:
                    print("Please enter a valid integer")
                except LinkedListException as e:
                    print(f"Error: {e}")
            
            elif choice == '4':
                size = linked_list.get_size()
                print(f"List size: {size}")
            
            elif choice == '5':
                if linked_list.is_empty():
                    print("List is empty")
                else:
                    print("List is not empty")
            
            elif choice == '6':
                run_sample_test()
            
            elif choice == '7':
                print("Thank you for using the Linked List!")
                break
            
            else:
                print("Invalid choice! Please enter a number between 1-7")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()