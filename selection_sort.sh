#!/bin/bash

# Function to perform selection sort
selection_sort() {
    local arr=("${!1}")
    local n=${#arr[@]}  # Get the number of elements in the array

    for ((i = 0; i < n - 1; i++)); do
        min_index=$i  # Assume the current index is the smallest
        for ((j = i + 1; j < n; j++)); do
            if [[ ${arr[j]} -lt ${arr[min_index]} ]]; then
                min_index=$j  # Update the index of the smallest element
            fi
        done

        # Swap the smallest element with the element at index i
        temp=${arr[i]}
        arr[i]=${arr[min_index]}
        arr[min_index]=$temp
    done

    eval "$1=(\"\${arr[@]}\")"  # Update the original array with the sorted values
}

# Main script
echo "Enter numbers to sort (space-separated):"
read -a array  # Read the input as an array

selection_sort array[@]  # Call the selection_sort function

echo "Sorted array:"
echo "${array[@]}"  # Display the sorted array
