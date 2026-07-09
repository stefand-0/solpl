when(a, b, action)
  _get("std/extdata/Infinity.sol")
  j -> Infinity.new()
  for i -> 0 to j
    if a == b
      _return -> action
    end
  end
end
