main()
  _get("std/extcond/Cond.sol")
  ; The while loop operates until max uint64
  _out -> Cond.when(1, 0, "Returns... nothing? 1 != 0, and it never will")
end
