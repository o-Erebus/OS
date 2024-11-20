def fifo_page_replacement(page,frame_size):
    stack=[]
    faults=0
    
    
    print("FIFO Page Replacement\n")
    for page in pages:
        if page not in stack:
            faults+=1
            print(f"Miss {page} || {stack} || No of Faults = {faults}")
            if len(stack)>=frame_size:
                removed=stack.pop(0)
                print(f"{removed} Removed")
            stack.append(page)
        else:
            print(f"Hit {page} || {stack}")
        
        
        print(f"Current Frame:{stack}")
    print(f"\nTotal Page Faults (FIFO): {faults}\n")
    
pages=[7,0,1,2,0,3,0,4,2,3,0,3,2,3]
frame_size=4
fifo_page_replacement(pages,frame_size)
        
     