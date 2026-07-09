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

fact(n)
  r -> 1
  if n == 0
    _return -> 1
  end
  for i -> 1 to n
    r -> r * i
  end
  _return -> r
end

gcd(a, b)
  while b > 0
    t -> b
    b -> mod(a, b)
    a -> t
  end
  _return -> a
end

fib(n)
  if n == 0
        _return -> 0
    elseif n == 1
        _return -> 1
    end
    
    a -> 0
    b -> 1
    for i -> 2 to n
        next_val -> a + b
        a -> b
        b -> next_val
    end
    _return -> b
end

percent(part, total)
    ; Multiplies first to avoid float issues, then divides
    _return -> (part * 100) : total
end
