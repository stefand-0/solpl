init(tree_list, max_capacity)
    limit -> max_capacity - 1
    for i -> 0 to limit
        _add(tree_list, i, -1)
    end
end

insert(tree_list, value)
    current_idx -> 0
    placed -> 0
    
    while placed == 0
        slot_value -> tree_list[current_idx]
        
        ; 1. Found an empty slot! Place the value here.
        if slot_value == -1
            tree_list[current_idx] -> value
            placed -> 1
        else
            ; 2. If the value is smaller, climb down to the Left Child slot
            if value < slot_value
                current_idx -> (2 * current_idx) + 1
            else
                ; 3. If the value is larger or equal, climb down to the Right Child slot
                current_idx -> (2 * current_idx) + 2
            end
        end
    end
end
