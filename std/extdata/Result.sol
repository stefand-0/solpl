Result{}
  status -> 0 ; 1 for Ok, 0 for Err
  data -> 0
  error -> ""
end

ok(val)
  r -> Result{}
  r.status -> 1
  r.data -> val
  _return -> r
end

err(msg)
  r -> Result{}
  r.status -> 0
  r.error -> msg
  _return -> r
end
