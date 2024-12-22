# 1. Stack
stack = [3, 4, 5]
stack.append(6) #[3, 4, 5, 6]
stack.pop() #[3, 4, 5]

print(stack)

# 2. Queue
# deque -> doble end queue
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()

print(queue)
