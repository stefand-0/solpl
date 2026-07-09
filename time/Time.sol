epoch()
    ; Using a plain text API endpoint that returns just the number string
    raw_response -> _fetch("http://worldtimeapi.org/api/timezone/Etc/UTC.txt")
    
    ; If the server sends a clean plain text number, we return it directly
    _return -> raw_response
end

; WARNING, EXTENDED USE MAY TEMPORARILY BAN YOUR IP FROM THE WORLDTIMEAPI SERVER

delay(seconds)
    start_time -> fetch_live_epoch()
    target_time -> start_time + seconds
    
    current_time -> start_time
    
    ; Keep loop spinning until the network says time is up!
    while current_time < target_time
        current_time -> epoch()
    end
end

; (Pass is_negative as 1 to subtract hours, 0 to add)
apply_offset(epoch, hours, is_negative)
    seconds_to_shift -> hours * 3600
    
    if is_negative == 1
        _return -> epoch - seconds_to_shift
    else
        _return -> epoch + seconds_to_shift
    end
end
