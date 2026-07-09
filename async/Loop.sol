afor(f, out)
  for i -> 0 to f
    _out -> out
  end
end
; Loop.afor(1, "Hello") >> _async()

awhile(arg, out)
  while arg == arg
    _out -> out
  end
end
; Loop.awhile(1, "Hello") >> _async()
; Keep in mind that asynchronous functions cannot return values with _return.

awhen(a, b, out)
  _get("std/extcond/Cond.sol")
  _out -> Cond.while(1, 2, out)
; Loop.awhen(1,1,"Hello")
end