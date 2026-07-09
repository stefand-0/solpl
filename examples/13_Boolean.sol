main()
  _get("std/bool/Boolean.sol")
  n -> Boolean.true()
  boolAsString -> Boolean.to_str(n)
  ; That was a Boolean
  ; Now, onto logical operators
  _out -> Boolean.not(1)
  _out -> Boolean.and(1,0)
  _out -> Boolean.or(1,0)
  _out -> Boolean.xor(1,1)
  _out -> Boolean.nand(1,0)
  _out -> Boolean.nor(1,1)
  _out -> Boolean.implies(1,0)
end
