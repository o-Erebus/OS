#!/bin/bash 
# Function to check if a substring exists within a string 
substring_check() { 
    local string="$1" 
    local substring="$2" 
    if [[ "$string" == *"$substring"* ]]; then 
        echo "The substring '$substring' exists within the string '$string'." 
    else 
        echo "The substring '$substring' does not exist within the string '$string'." 
    fi 
} 
# Read input from the user 
read -p "Enter the main string: " main_string 
read -p "Enter the substring to check: " sub_string 
# Call the substring check function 
substring_check "$main_string" "$sub_string"