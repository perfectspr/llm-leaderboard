***
### Coding 1
Generate a bash script to create 10 files, with the names A1.txt through A10.txt
### Answer
```bash
for i in {1..10}
do
  touch A$i.txt
done
```
***
### Coding 2
Write a Oracle SQL query to find the nth number in the Fibonacci Sequence.
### Answer
```sql
WITH fibonacci (n, a, b) AS (
  SELECT 1, 0, 1 FROM dual
  UNION ALL
  SELECT n+1, b, a+b FROM fibonacci WHERE n < :n
)
SELECT a AS fibonacci_number FROM fibonacci WHERE n = :n;
```
***
### Coding 3
How can I install the Pandas package in Python?
### Answer
`python -m pip install pandas` or `pip install pandas`
***
### Coding 4
Edit the following code to print out all even numbers from 1 to 10.
```python
for i in range(1,11):
    print(i)
```
### Answer
```python
for i in range(1,11):
    if i % 2 == 0:
        print(i)
```

***
### Coding 5
Create a function to calculate the area of a given circle.
### Answer
```python
def area_circle(radius):
    return 3.14 * (radius**2)
```
***
### Coding 6
Write a Python program that prints the value of every tree node value of a binary tree.
### Answer
To print the value of every node in a binary tree, we first need to define the structure of a binary tree. A binary tree is a data structure where each node has at most two children, referred to as the left child and the right child.

Here's a simple Python program that defines a binary tree node, populates the tree, and prints the values of all nodes using an in-order traversal (which visits left subtree, root, and then right subtree):

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree_in_order(node):
    if node is not None:
        print_tree_in_order(node.left)
        print(node.value)
        print_tree_in_order(node.right)

# Example usage:
# Constructing the following binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print_tree_in_order(root)
```

When you run this program, it will output:

```
4
2
5
1
3
```

This program uses a recursive function `print_tree_in_order` to traverse the tree in an in-order fashion. If you would like to print the values using a different traversal method, such as pre-order or post-order, you can modify the function as follows:

For pre-order traversal (root, left subtree, right subtree):

```python
def print_tree_pre_order(node):
    if node is not None:
        print(node.value)
        print_tree_pre_order(node.left)
        print_tree_pre_order(node.right)
```

For post-order traversal (left subtree, right subtree, root):

```python
def print_tree_post_order(node):
    if node is not None:
        print_tree_post_order(node.left)
        print_tree_post_order(node.right)
        print(node.value)
```
***
### Coding 7
What is the difference between multiprocessing and multithreading in Python?
### Answer
Multiprocessing and multithreading are both approaches to achieve parallelism and concurrency in Python, allowing a program to perform multiple operations at once. However, they work in different ways and are suitable for different types of tasks. Here's a brief overview of the differences:

**Multithreading:**
- Threads are lighter-weight than processes. They share the same memory space and efficiently read and write to the same variables.
- In Python, the Global Interpreter Lock (GIL) prevents multiple native threads from executing Python bytecodes at once. This means that threads are not truly running in parallel in a standard CPython implementation when it comes to CPU-bound tasks. They are better suited for I/O-bound tasks where the performance improvement comes from the program being able to handle I/O operations concurrently.
- Multithreading is useful when the program is I/O-bound and you want to make better use of idle time, such as waiting for files or network services.
- Multithreading can lead to issues like race conditions and deadlocks if not managed correctly, due to shared access to mutable data.

**Multiprocessing:**
- Each process in multiprocessing has its own Python interpreter and memory space, so the GIL does not prevent multiple processes from running in parallel on multiple CPU cores. This makes it suitable for CPU-bound tasks.
- Multiprocessing often results in a higher memory overhead because each process has a separate memory space.
- It is useful for CPU-intensive operations where tasks can be performed in parallel without needing to share data, or where data sharing is done minimally and carefully (using IPC mechanisms like queues or pipes).
- Multiprocessing in Python can be implemented using the `multiprocessing` module, which provides an API similar to `threading`.

In summary, multithreading is best for tasks that spend a lot of time waiting for external events (I/O-bound), while multiprocessing is best for tasks that need to perform a lot of computations and can take advantage of multiple cores (CPU-bound). Each method comes with its own set of challenges and trade-offs, such as managing concurrency issues in multithreading or dealing with the overhead of inter-process communication in multiprocessing.
Multiprocessing and multithreading are both approaches to achieve parallelism and concurrency in Python, allowing a program to perform multiple operations at once. However, they work in different ways and are suitable for different types of tasks. Here's a brief overview of the differences:

**Multithreading:**
- Threads are lighter-weight than processes. They share the same memory space and efficiently read and write to the same variables.
- In Python, the Global Interpreter Lock (GIL) prevents multiple native threads from executing Python bytecodes at once. This means that threads are not truly running in parallel in a standard CPython implementation when it comes to CPU-bound tasks. They are better suited for I/O-bound tasks where the performance improvement comes from the program being able to handle I/O operations concurrently.
- Multithreading is useful when the program is I/O-bound and you want to make better use of idle time, such as waiting for files or network services.
- Multithreading can lead to issues like race conditions and deadlocks if not managed correctly, due to shared access to mutable data.

**Multiprocessing:**
- Each process in multiprocessing has its own Python interpreter and memory space, so the GIL does not prevent multiple processes from running in parallel on multiple CPU cores. This makes it suitable for CPU-bound tasks.
- Multiprocessing often results in a higher memory overhead because each process has a separate memory space.
- It is useful for CPU-intensive operations where tasks can be performed in parallel without needing to share data, or where data sharing is done minimally and carefully (using IPC mechanisms like queues or pipes).
- Multiprocessing in Python can be implemented using the `multiprocessing` module, which provides an API similar to `threading`.

In summary, multithreading is best for tasks that spend a lot of time waiting for external events (I/O-bound), while multiprocessing is best for tasks that need to perform a lot of computations and can take advantage of multiple cores (CPU-bound). Each method comes with its own set of challenges and trade-offs, such as managing concurrency issues in multithreading or dealing with the overhead of inter-process communication in multiprocessing.
***
### Coding 8
Translate the following python dictionary from JSON to an HTML table with column headers and title: 
```json
{ "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}
```
### Answer
```html
<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>Restaurant Employees</h2>

<table>
  <tr>
    <th>Name</th>
    <th>Email</th>
  </tr>
  <tr>
    <td>Shyam</td>
    <td>shyamjaiswal@gmail.com</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>bob32@gmail.com</td>
  </tr>
  <tr>
    <td>Jai</td>
    <td>jai87@gmail.com</td>
  </tr>
</table>

</body>
</html>
```
