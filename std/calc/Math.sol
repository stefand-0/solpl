sq(n)
  _return -> n * n
end

cube(n)
  _return -> n * n * n
end

quad(n)
  _return -> n * n * n * n
end

abs(v)
  if v < 0
    _return -> v * -1
  else
    _return -> v
  end
end

pow(b, e)
  res -> 1
  for i -> 0 to e
    res -> res * b
  end
  _return -> res
end

mod(n, d)
  while n > d
    n -> n - d
  end
  if n == d
    _return -> 0
  else
    _return -> n
  end
end

max(a, b)
  if a > b
    _return -> a
  else
    _return -> b
  end
end

min(a, b)
  if a < b
    _return -> a
  else
    _return -> b
  end
end

clamp(v, l, h)
  if v < l
    _return -> l 
  elseif v > h
    _return -> h
  else
    _return -> v
  end
end

percent(part, total)
    ; Multiplies first to avoid float issues, then divides
    _return -> (part * 100) : total
end
