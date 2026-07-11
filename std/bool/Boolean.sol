true()
   n -> 1
   _return -> n
end

false()
  n -> 0
  _return -> 0
end

not(n)
  if n = 1
    _return -> 0
  else
    _return -> 1
  end
end

and(a, b)
  if a = 1
    if b = 1
      _return -> 1
    end
  end
  _return -> 0
end

or(a, b)
  if a = 1
    _return -> 1
  elseif b = 1
    _return -> 1
  else
    _return -> 0
  end
end

xor(a, b)
    if a = b
        _return -> 0
    else
        _return -> 1
    end
end

nand(a, b)
    if a = 1
        if b = 1
            _return -> 0
        end
    end
    _return -> 1
end

nor(a, b)
    if a = 1
        _return -> 0
    elseif b = 1
        _return -> 0
    else
        _return -> 1
    end
end

implies(a, b)
    if a = 1
        if b = 0
            _return -> 0
        end
    end
    _return -> 1
end

to_str(val)
    if val = 1
        _return -> "true"
    else
        _return -> "false"
    end
end
