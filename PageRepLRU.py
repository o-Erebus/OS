# LRU Page Replacement
def lru_page_replacement(pages, frame_size):
    stack = []
    faults = 0

    print("LRU Page Replacement\n")
    for i, page in enumerate(pages):
        if page not in stack:
            faults += 1
            if len(stack) >= frame_size:
                to_remove = []
                for j in range(i - 1, -1, -1):
                    if pages[j] in stack and pages[j] not in to_remove:
                        to_remove.append(pages[j])
                removed = to_remove[-1]
                stack.remove(removed)
                print(f"Miss {page}\nRemoving {removed}")
            stack.append(page)
        else:
            print(f"Hit {page} || {stack}")

        print(f"Current Frame: {stack} || Faults: {faults}")
    print(f"\nTotal Page Faults (LRU): {faults}\n")


# Example Input
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
frame_size = 4
lru_page_replacement(pages, frame_size)
    