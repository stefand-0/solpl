find_user(id)
  id == 1 ? _return -> Maybe.some("Guy")
  _return -> Maybe.none()
end
; Optional structs have 2 parameters: value, status
main()
  _get("solstd/std/extdata/Maybe.sol")
  ; For example, checking for an ID.
  result -> find_user(1)
  result.status = 0 ? _out -> "User not found!"
  result.status = 1 ? _out -> "User found: " + result.value 
end
