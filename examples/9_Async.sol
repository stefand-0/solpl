myAsync()
  ; Super heavy calculations
  ; It would be better if they ran in the background!
  var -> 1
  _out -> var
end

main()
  _out -> "Async starting."
  ; Pipe the function into the global _async method
  myAsync() >> _async
  ; Printing the initial state:
  _out -> var
end
