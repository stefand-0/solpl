Promise{}
    status -> "PENDING"
    result -> 0
end

; Called by the main thread to check if data is ready
is_ready(promise_struct) ; promise_struct = Promise{}
    if promise_struct.status == "FULFILLED"
        _return -> 1
    else
        _return -> 0
    end
end
