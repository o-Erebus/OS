awk '{ 
    if ($3 < 40 || $4 < 40 || $5 < 40) { 
        result = "Fail"; 
        percentage = "-"; 
        printf "%s (Roll No: %s) - Total Marks: N/A, Percentage: %s, Result: %s\n", $1, $2, percentage, result;
    } else {
        total = $3 + $4 + $5; 
        percentage = total / 3; 
        
        if (percentage >= 65) { 
            result = "Distinction"; 
        } else if (percentage >= 60 && percentage < 65) { 
            result = "First Class"; 
        } else if (percentage >= 40) { 
            result = "Pass"; 
        } else { 
            result = "Fail"; 
        }
        
        printf "%s (Roll No: %s) - Total Marks: %d, Percentage: %.2f, Result: %s\n", $1, $2, total, percentage, result;
    }
}' A3.txt
