#!/usr/bin/awk -f

{
    # Store each number in an array
    numbers[NR] = $1
    count = NR
}

END {
    # Simple selection sort algorithm
    for (i = 1; i <= count; i++) {
        min_idx = i
        for (j = i + 1; j <= count; j++) {
            if (numbers[j] < numbers[min_idx]) {
                min_idx = j
            }
        }
        # Swap the found minimum element with the first element of the unsorted segment
        temp = numbers[i]
        numbers[i] = numbers[min_idx]
        numbers[min_idx] = temp
    }

    # Print the sorted numbers
    for (i = 1; i <= count; i++) {
        print numbers[i]
    }
}