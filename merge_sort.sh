#!/bin/bash

# Function to merge two sorted subarrays
merge() {
    local arr=("${!1}")
    local left=$2
    local mid=$3
    local right=$4

    local n1=$((mid - left + 1))
    local n2=$((right - mid))

    local L=("${arr[@]:left:n1}")
    local R=("${arr[@]:mid+1:n2}")

    local i=0
    local j=0
    local k=$left

    while [[ $i -lt $n1 && $j -lt $n2 ]]; do
        if [[ ${L[i]} -le ${R[j]} ]]; then
            arr[k]=${L[i]}
            ((i++))
        else
            arr[k]=${R[j]}
            ((j++))
        fi
        ((k++))
    done

    while [[ $i -lt $n1 ]]; do
        arr[k]=${L[i]}
        ((i++))
        ((k++))
    done

    while [[ $j -lt $n2 ]]; do
        arr[k]=${R[j]}
        ((j++))
        ((k++))
    done

    eval "$1=(\"\${arr[@]}\")"
}

# Recursive function to perform merge sort
merge_sort() {
    local arr=("${!1}")
    local left=$2
    local right=$3

    if [[ $left -lt $right ]]; then
        local mid=$(((left + right) / 2))

        merge_sort arr[@] $left $mid
        merge_sort arr[@] $((mid + 1)) $right
        merge arr[@] $left $mid $right
    fi

    eval "$1=(\"\${arr[@]}\")"
}

# Main script
echo "Enter numbers to sort (space-separated):"
read -a array

merge_sort array[@] 0 $((${#array[@]} - 1))

echo "Sorted array:"
echo "${array[@]}"
