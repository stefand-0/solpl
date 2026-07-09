WorkerPool{}
    max_workers -> 4
    active_workers -> 0
    task_count -> 0
end

dispatch(pool_struct, function_name, argument)
    _get("std/extdata/Queue.sol")
    
    if pool_struct.active_workers < pool_struct.max_workers
        ; We have room, so increment active count and run it natively
        pool_struct.active_workers -> pool_struct.active_workers + 1
        function_name(argument) >> _async
    else
        ; The pool is maxed out, so back up the task into the queue
        Queue.push(pool_struct.backlog, function_name)
    end
end
