#!/bin/bash 
# Function to perform Bubble Sort 
bubble_sort() { 
local array=("$@") 
local n=${#array[@]} 
local temp 
# Loop through the entire array 
for ((i = 0; i < n; i++)); do 
# Flag to check if any swap was made 
swapped=false 
# Compare adjacent elements 
for ((j = 0; j < n-i-1; j++)); do 
      if ((array[j] > array[j+1])); then 
        # Swap the elements 
        temp=${array[j]} 
        array[j]=${array[j+1]} 
        array[j+1]=$temp 
        swapped=true 
      fi 
    done 
 
    # If no elements were swapped, the array is sorted 
    if [ "$swapped" = false ]; then 
      break 
    fi 
  done 
 
  echo "${array[@]}" 
} 
 
# Read input from the user 
read -p "Enter numbers separated by spaces: " -a numbers 
 
# Call the Bubble Sort function 
sorted_numbers=($(bubble_sort "${numbers[@]}")) 
 
# Print the sorted array 
echo "Sorted numbers: ${sorted_numbers[@]}"