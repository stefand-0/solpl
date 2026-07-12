; RaySync is an async library, designed to make spawning threads easier, and less heavy on the CPU.
; Make sure you have the SolSTD repo cloned onto your home directory.
main()
    _get("solstd/raysync/ray.sol")

    worker(fut, msg)
        _sleep(500)
        ray_promise(fut, "done: " + msg)
    end

    f1 -> ray_alloc()
    f2 -> ray_alloc()

    worker(f1, "alpha") >> _async
    worker(f2, "beta") >> _async

    ray_join2(f1, f2)

    ray_get(f1) >> _out
    ray_get(f2) >> _out
end
