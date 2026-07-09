main()
  ; _out outputs a value to the console
  _out -> "Hello, World!"
  ; _in() takes input with a prompt
  _in("Name? ") -> name
  _out -> "Hello, " + name + "!"
  ; String concatenation is done with "+"
end
