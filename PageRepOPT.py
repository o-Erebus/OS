def optimal_page_replacement(pages,frame_size):
    fault=0
    stack=[]
    
    for i,page in enumerate(pages):
        if page not in stack:
            fault+=1
            if len(stack)>=frame_size:
                to_remove=[]
                for j in range(i+1,len(pages)):
                    if pages[j] in stack and pages[j] not in to_remove:
                        to_remove.append(pages[j])
                    
                for s in stack:
                    if s not in pages[i+1:]:
                        to_remove.append(s)
                        break
                    
                removed = to_remove[-1]
                stack.remove(removed)
                print(f"\nMiss {page}\nRemoving {removed}")
            stack.append(page)
        else:
            print(f"\nHit {page} || {stack}")
            
        print(f"Current Frame: {stack} || Faults: {fault}")
    print(f"\nTotal Page Faults (Optimal): {fault}\n")


# Example Input
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
frame_size = 4
optimal_page_replacement(pages, frame_size)            
                    
    
    