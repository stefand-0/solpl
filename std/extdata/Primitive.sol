to_binary(num)
    _get("std/calc/Math.sol")
    binary_str -> ""
    
    if num == 0
        _return -> "0"
    end
    
    while num > 0 
        remainder -> Math.mod(num, 2)
        
        ; Append the bit to the front of our string
        binary_str -> remainder + binary_str
        
        ; Clean integer division step
        num -> (num - remainder) : 2
    end
    
    _return -> binary_str
end

to_hex(num)
    _get("std/calc/Math.sol")
    hex_str -> ""
    
    if num == 0
        _return -> "0"
    end
    
    while num > 0
        remainder -> Math.mod(num, 16)
        
        ; Map remainders 10-15 to hex characters
        char -> ""
        if remainder == 10 ? char -> "A"
        if remainder == 11 ? char -> "B"
        if remainder == 12 ? char -> "C"
        if remainder == 13 ? char -> "D"
        if remainder == 14 ? char -> "E"
        if remainder == 15 ? char -> "F"
        if remainder < 10  ? char -> remainder
        
        ; Stitch it onto the front
        hex_str -> char + hex_str
        
        ; Clean integer division step
        num -> (num - remainder) : 16
    end
    
    _return -> hex_str
end
