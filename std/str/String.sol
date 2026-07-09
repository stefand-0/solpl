empty(text)
    if text == ""
        _return -> 1 ; True
    else
        _return -> 0 ; False
    end
end

contains_char(text, len, char)
    limit -> len - 1
    for i -> 0 to limit
        if text[i] == char
            _return -> 1 ; True! Found it!
        end
    end
    _return -> 0 ; False
end

pad_left(text, current_len, target_len, pad_char)
    needed -> target_len - current_len
    padding -> ""
    
    for i -> 1 to needed
        padding -> padding + pad_char
    end
    
    _return -> padding + text
end

pad_right(text, current_len, target_len, pad_char)
    needed -> target_len - current_len
    padding -> ""
    
    for i -> 1 to needed
        padding -> padding + pad_char
    end
    
    _return -> text + padding
end

wrap(text, open_tags, close_tags)
    _return -> open_tags + text + close_tags
end

reverse(text, len)
    reversed_str -> ""
    limit -> len - 1
    
    ; Loops backwards from the end of the string to 0
    for i -> limit to 0
        reversed_str -> reversed_str + text[i]
    end
    
    _return -> reversed_str
end
