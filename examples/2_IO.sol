main()
  ; _out outputs a value to the console
  _out -> "Hello, World!"
  ; _in takes input with a prompt
  ; pipes the output into name
  ; io is non-blocking
  "Name? " >> _in >> name
  _out -> "Hello, " + name + "!"
  ; String concatenation is done with "+"
end
