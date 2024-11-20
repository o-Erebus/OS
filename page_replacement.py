page = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
print(page)
frame = 4
print(frame)
stack =[]
fault = 0
#Fifo
for i in range(len(page)):
    if page[i] not in stack:
        fault+=1
        print(f"Miss {page[i]} || {stack} || No of Faults = {fault}")
        if len(stack) >= frame:
            print(stack.pop(0) ," Removed")
            stack.append(page[i])
        else:
            stack.append(page[i])
        print(f"{stack}")
    else:
        print(f"Hit {page[i]} || {stack}")


print(f"FIFO Page fault {fault}")



page = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
frame = 4
stack =[]
fault = 0
#LRU
print("\n\n\n\n")
for i in range(len(page)):
    if page[i] not in stack:
        fault+=1

        if len(stack) >= frame:
            toremove = []
            for j in range (i-1,-1,-1):
                if page[j] in stack and page[j] not in toremove:
                    toremove.append(page[j])

            stack.remove(toremove[-1])
            stack.append(page[i])
            print(f"Miss {page[i]}\nRemoving {toremove[-1]} || {stack} || {fault}")
        else:

            stack.append(page[i])
            print(f"Miss {page[i]}\n || {stack} || {fault}")
    else:
        print(f"Hit {page[i]} || {stack}")

print(f"LRU Page {fault}")

page = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
frame = 4
stack =[]
fault = 0
toremove = []
print("\n\n\n\n")
for i in range(len(page)):
    if page[i] not in stack:
        fault+=1
        if len(stack) >= frame:
            print(f"Miss {page[i]}\nRemoving {toremove[0]} ",end="")
            stack.remove(toremove.pop(0))

            stack.append(page[i])
            print(f"|| {stack} || {fault}")
            toremove.append(page[i])

        else:

            stack.append(page[i])
            toremove.append(page[i])
            print(f"Miss {page[i]}\n|| {stack} || {fault}")
        print(f"{stack}")
    else:
        print(f"Hit {page[i]} || {stack}")
        toremove.remove(page[i])
        toremove.append(page[i])

print(f"LRU Page {fault}")


page = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
frame = 4
stack =[]
fault = 0
toremove = []
#LRU
print("\n\n\n\n")
for i in range(len(page)):
    if page[i] not in stack:
        fault+=1
        if len(stack) >= frame:
            toremove = []
            for j in range (i+1,len(page)):
                if page[j] in stack and page[j] not in toremove:
                    toremove.append(page[j])
            for s in stack:
                if s not in page[i+1:]:
                    toremove= [s]
                    break
            stack.remove(toremove[-1])
            stack.append(page[i])
            print(f"\nMiss {page[i]}\nRemoving {toremove[-1]} || {stack} || {fault}")
        else:

            stack.append(page[i])
            print(f"\nMiss {page[i]}\n || {stack} || {fault}")
    else:
        print(f"\nHit {page[i]} || {stack}")

print(f"Optimal Page {fault}")

