class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        """ Insert a new node with key and data into the BST. """
        self.root = self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if node is None:
            return Node(key, data)
        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        return node

    def search(self, key):
        """ Search for a node by key. """
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        """ Delete a node by key. """
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.data = temp.data
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        """ Find the node with the minimum key value in the BST. """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order(self):
        """ Traverse the tree in-order and return a list of nodes (sorted by key). """
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append((node.key, node.data))
            self._in_order(node.right, result)


class Order:
    def __init__(self, order_id, customer_name, food_item):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Food Item: {self.food_item}"


class FoodDeliveryApp:
    def __init__(self):
        self.bst = BinarySearchTree()

    def add_order(self):
        """ Add a new order to the system. """
        try:
            order_id = int(input("Enter order ID: "))
            customer_name = input("Enter customer name: ")
            food_item = input("Enter food item: ")
            order = Order(order_id, customer_name, food_item)
            self.bst.insert(order_id, order)
            print("Order added successfully!")
        except ValueError:
            print("Invalid input! Order ID must be an integer.")

    def find_order(self):
        """ Find an order by order ID. """
        try:
            order_id = int(input("Enter order ID to search: "))
            result = self.bst.search(order_id)
            if result:
                print(result.data)
            else:
                print("Order not found.")
        except ValueError:
            print("Invalid input! Order ID must be an integer.")

    def delete_order(self):
        """ Delete an order by order ID. """
        try:
            order_id = int(input("Enter order ID to delete: "))
            self.bst.delete(order_id)
            print("Order deleted successfully!")
        except ValueError:
            print("Invalid input! Order ID must be an integer.")

    def list_orders(self):
        """ List all orders sorted by order ID. """
        orders = self.bst.in_order()
        if not orders:
            print("No orders found.")
        else:
            for key, order in orders:
                print(order)

    def update_order(self):
        try:
            order_id = int(input("Enter order ID to update: "))
            result = self.bst.search(order_id)
            if result:
                print("Current order details:")
                print(result.data)
                print("Enter new details:")
                customer_name = input("Enter new customer name: ")
                food_item = input("Enter new food item: ")
                result.data.customer_name = customer_name
                result.data.food_item = food_item
                print("Order updated successfully!")
            else:
                print("Order not found.")
        except ValueError:
            print("Invalid input! Order ID must be an integer.")



    def main_menu(self):
        while True:
            print("\nFood Delivery Management System")
            print("1. Add Order")
            print("2. Find Order")
            print("3. Cancel Order")
            print("4. Update Order")
            print("5. View All Orders")
            print("6. Exit")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice! Please enter a number.")
                continue

            if choice == 1:
                self.add_order()
            elif choice == 2:
                self.find_order()
            elif choice == 3:
                self.delete_order()
            elif choice == 4:
                self.update_order()
            elif choice == 5:
                self.list_orders()
            elif choice == 6:
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = FoodDeliveryApp()
    app.main_menu()
