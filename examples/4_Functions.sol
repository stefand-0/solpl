; Functions are defined with "()"
; The _return method only works for synchronous functions.
myFunction(input)
  _return -> input
end

; main() is the starting point for every program
main()
  result -> myFunction()
  _out -> result
end
