enqueue(list, current_tail_idx, value)
    _add(list, current_tail_idx, value)
end

dequeue(list, current_front_idx, current_tail_idx)
    if current_front_idx == current_tail_idx
        _return -> "QUEUE_EMPTY"
    else
        ; Return the front item, developer will increment front_idx by 1!
        _return -> list[current_front_idx]
    end
end
