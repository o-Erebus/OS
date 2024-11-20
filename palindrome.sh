#!/bin/bash 
# Function to check if a string is a palindrome 
is_palindrome() { 
    local input="$1" 
    local length=${#input}
    local reversed_input=""
    
    # Reverse the string manually
    for (( i=length-1; i>=0; i-- )); do
        reversed_input="$reversed_input${input:$i:1}"
    done
    
    # Check if the input string is the same as the reversed string
    if [[ "$input" == "$reversed_input" ]]; then 
        echo "The string '$input' is a palindrome." 
    else 
        echo "The string '$input' is not a palindrome." 
    fi 
} 

# Read input from the user 
read -p "Enter a string: " user_input 

# Call the palindrome check function 
is_palindrome "$user_input"
