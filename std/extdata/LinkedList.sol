init(list)
    ; Index 0 is the Head Pointer. -1 means the list is empty.
    _add(list, 0, -1)
end

append(list, current_node_count, value)
    ; Calculate where this new node will physically sit in the flat list
    ; (Account for the 1 slot used by the Head Pointer at Index 0)
    new_node_idx -> 1 + (current_node_count * 2)
    
    ; Drop in the data and set its "Next" pointer to -1 (the end)
    _add(list, new_node_idx, value)
    
    next_ptr_idx -> new_node_idx + 1
    _add(list, next_ptr_idx, -1)
    
    ; If the list was completely empty, make Head point to this new node
    if list[0] == -1
        list[0] -> new_node_idx
    else
        ; Otherwise, walk the pointers to find the current tail node
        current -> list[0]
        
        while list[current + 1] != -1
            current -> list[current + 1]
        end
        
        ; Link the old tail's Next pointer to the new node's physical index
        tail_next_ptr_idx -> current + 1
        list[tail_next_ptr_idx] -> new_node_idx
    end
end

print(list)
    ; Start at the Head pointer
    current -> list[0]
    
    ; Follow the pointer chain until we hit -1
    while current != -1
        _out -> "Node Value: " + list[current]
        
        ; Move 'current' to the index stored in the Next pointer slot
        next_ptr_idx -> current + 1
        current -> list[next_ptr_idx]
    end
end

