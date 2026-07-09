main()
  ; Always import in the main function
  ; For example, using the Math library
  _get("std/calc/Math.sol")
  ; The name of the lib file is the namespace
  square -> Math.sq(6)
  _out -> answer
end
