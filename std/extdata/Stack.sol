push(list, current_size, value)
    _add(list, current_size, value)
end

top(list, current_size)
    if current_size = 0
        _return -> "STACK_EMPTY"
    else
        top_idx -> current_size - 1
        _return -> list[top_idx]
    end
end

; Developer decrements size tracker by 1.
pop(list, current_size)
    if current_size = 0
        _return -> "STACK_EMPTY"
    else
        top_idx -> current_size - 1
        _return -> list[top_idx]
    end
end
