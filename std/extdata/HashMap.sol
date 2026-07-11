clear(map_list, current_pair_count)
    total_slots -> current_pair_count * 2
    limit -> total_slots - 1
    
    for i -> 0 to limit
        _add(map_list, i, "")
    end
end

put(map_list, current_pair_count, key, value)
    found -> 0
    total_slots -> current_pair_count * 2
    
    ; Look for an existing key
    i -> 0
    while i < total_slots
        if map_list[i] = key
            val_idx -> i + 1
            _add(map_list, val_idx, value) ; Overwrites the old value!
            found -> 1
            i -> total_slots ; Break loop
        else
            i -> i + 2
        end
    end
    
    ; If it's a brand new key, append it to the end
    if found = 0
        _add(map_list, total_slots, key)
        
        val_idx -> total_slots + 1
        _add(map_list, val_idx, value)
    end
end

; Retrieves a value by its key from the single map list
get(map_list, current_pair_count, key)
    total_slots -> current_pair_count * 2
    
    i -> 0
    while i < total_slots
        if map_list[i] = key
            val_idx -> i + 1
            _return -> map_list[val_idx]
        end
        i -> i + 2
    end
    
    _return -> "NOT_FOUND"
end

