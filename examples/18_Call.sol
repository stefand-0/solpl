double(x)
  _return -> x * 2
end

main()
  ; Call a function by its name as a string
  result -> _call("double", 5)
  _out -> result
end