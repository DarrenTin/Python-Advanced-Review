stack = []

for i in [200, 250, 1080]:
    stack.append(i)

print(stack)
print(stack.pop()) # 1080
print(stack[-1]) # peek
print(len(stack) == 0) # check empty