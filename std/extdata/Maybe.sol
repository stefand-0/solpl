Maybe{}
  status -> 0
  value -> 0
end

some(val)
  Maybe.status -> 1
  Maybe.value -> val
  _return -> Maybe{}
end

none(val)
  Maybe.status -> 0
  _return -> Maybe{}
end

