#!/bin/bash

# Function to perform insertion sort
insertion_sort() {
    local arr=("${!1}")
    local n=${#arr[@]}

    for ((i = 1; i < n; i++)); do
        key=${arr[i]}
        j=$((i - 1))

        while [[ $j -ge 0 && ${arr[j]} -gt $key ]]; do
            arr[j + 1]=${arr[j]}
            ((j--))
        done
        arr[j + 1]=$key
    done

    eval "$1=(\"\${arr[@]}\")"
}

# Main script
echo "Enter numbers to sort (space-separated):"
read -a array

insertion_sort array[@]

echo "Sorted array:"
echo "${array[@]}"
