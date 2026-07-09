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
  for i -> 0 to exp
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
