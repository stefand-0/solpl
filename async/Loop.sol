afor(f, out)
  for i -> 0 to f
    _out -> out
  end
end
; afor(1, "Hello") >> _async()

awhile(arg, out)
  while arg == arg
    _out -> out
  end
end
; awhile(1, "Hello") >> _async()
