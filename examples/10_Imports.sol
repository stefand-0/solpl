; Make sure to clone the `solstd` repo.
main()
  ; Always import in the main function
  ; For example, using the Math library
  _get("solstd/std/calc/Math.sol")
  ; The name of the lib file is the namespace
  square -> Math.sq(6)
  _out -> square
end
