; Data types that originate from Result{} are used for error handling
; A function that could fail
divide(a, b)
  b = 0 ? _return -> Result.err("Cannot divide by zero!")
  _return -> Result.ok(a : b)
end
main()
  _get("solstd/std/extdata/Result.sol")
  // Usage:
  res -> divide(10, 0)
  res.status = 0 ? _out -> "Error: " + res.error
  res.status = 1 ? _out -> "Success: " + res.data
end
