find(list, size, element)
    limit -> size - 1
    for i -> 0 to limit
        if list[i] = element
            _return -> i
        end
    end
    _return -> -1
end

contains(list, size, element)
    idx -> find(list, size, element)
    if idx = -1
        _return -> 0
    else
        _return -> 1
    end
end

swap(list, idx1, idx2)
    temp -> list[idx1]
    _add(list, idx1, list[idx2])
    _add(list, idx2, temp)
end

fill(list, size, value)
    limit -> size - 1
    for i -> 0 to limit
        _add(list, i, value)
    end
end

count(list, size, element)
    total -> 0
    limit -> size - 1
    for i -> 0 to limit
        if list[i] = element
            total -> total + 1
        end
    end
    _return -> total
end

maxval(list, size)
    max_val -> list[0]
    limit -> size - 1
    for i -> 1 to limit
        if list[i] > max_val
            max_val -> list[i]
        end
    end
    _return -> max_val
end


reverse(list, size)
    left -> 0
    right -> size - 1
    while right > left
        ; Swap the values inline
        temp -> list[left]
        _add(list, left, list[right])
        _add(list, right, temp)
        
        ; Move pointers closer together
        left -> left + 1
        right -> right - 1
    end
end

copy(src_list, dest_list, size)
    limit -> size - 1
    for i -> 0 to limit
        _add(dest_list, i, src_list[i])
    end
end

selection_sort(list, size)
    if size < 2
        _return -> 0
    end
    
    limit -> size - 2
    for i -> 0 to limit
        min_idx -> i
        
        ; Scan the rest of the list to find the minimum
        start_j -> i + 1
        end_j -> size - 1
        for j -> start_j to end_j
            if list[j] < list[min_idx]
                min_idx -> j
            end
        end
        
        ; Swap the lowest item into its final spot
        if min_idx > i
            temp -> list[i]
            _add(list, i, list[min_idx])
            _add(list, min_idx, temp)
        end
    end
end

insertion_sort(list, size)
    if size < 2
        _return -> 0
    end
    
    limit -> size - 1
    for i -> 1 to limit
        key -> list[i]
        j -> i - 1
        
        ; Loop to shift elements right
        keep_going -> 1
        while keep_going == 1
            if j < 0
                keep_going -> 0
            else
                if list[j] > key
                    next_j -> j + 1
                    _add(list, next_j, list[j])
                    j -> j - 1
                else
                    keep_going -> 0
                end
            end
        end
        
        ; Insert the key into its correct spot
        insert_idx -> j + 1
        _add(list, insert_idx, key)
    end
end

bubble_sort(list, size)
    ; If the list has 1 or 0 elements, it's already sorted!
    if size < 2
        _return -> 0
    end

    limit -> size - 1
    ; Outer loop: Controls how many passes we make through the list
    for i -> 1 to limit
        
        inner_limit -> size - 2
        ; Inner loop: Goes through the list and bubbles up the highest number
        for j -> 0 to inner_limit
            next_idx -> j + 1
            
            ; If the current item is bigger than the next item, swap them!
            if list[j] > list[next_idx]
                temp -> list[j]
                _add(list, j, list[next_idx])
                _add(list, next_idx, temp)
            end
        end
    end
end
