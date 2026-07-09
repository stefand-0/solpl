Maybe{}
  status -> 0
  value -> 0
end

some(val)
  m -> Maybe{}
  m.status -> 1
  m.value -> val
  _return -> m
end

none(val)
  m -> Maybe{}
  m.status -> 0
  _return -> m
end

