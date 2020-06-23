inputs = list()
"""
current = input("write something: ")
while current != "quit":
    inputs.append(current)
    current = input("Write something: ")
"""

while (current := input("Write something: ")) != "quit":
    inputs.append(current)
