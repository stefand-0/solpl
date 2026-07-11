; _call() example: first-class functions in Sol
; _call("function_name", arg1, arg2, ...) calls a function by name

; === Higher-order functions ===

; Apply a function to a value
apply(func, val)
  result -> _call(func, val)
  _return -> result
end

; Apply a function to each element of a list
map(func, list)
  result<r>
  i -> 0
  while i < 3
    _add(r, i, _call(func, list[i]))
    i -> i + 1
  end
  _return -> r
end

; Filter a list using a predicate
filter(func, list)
  result<r>
  i -> 0
  while i < 3
    keep -> _call(func, list[i])
    keep = 1 ? _add(r, 0, list[i])
    i -> i + 1
  end
  _return -> r
end

; === Functions to pass around ===

double(x)
  _return -> x * 2
end

triple(x)
  _return -> x * 3
end

is_even(x)
  x : 2 = 0 ? _return -> 1
  _return -> 0
end

is_positive(x)
  x > 0 ? _return -> 1
  _return -> 0
end

; === Struct for more complex example ===

Person{}\n  name -> \"\"\n  age -> 0\nend

; Function that takes a struct and returns a modified copy
birthday(person)
  person.age -> person.age + 1
  _return -> person
end

; === Main program ===

main()
  ; === Basic _call() ===
  _out -> \"=== Basic _call() ===\"\n  doubled -> _call(\"double\", 5)
n  _out -> doubled
  
  tripled -> _call(\"triple\", 4)
  _out -> tripled
  
  ; === Higher-order: apply() ===
  _out -> \"=== apply() ===\"\n  a -> apply(\"double\", 10)
  _out -> a
  
  b -> apply(\"triple\", 7)
  _out -> b
  
  ; === Passing functions as arguments ===
  _out -> \"=== Passing functions ===\"\n  my_func -> \"double\"\n  result -> _call(my_func, 15)
  _out -> result
  
  ; === map() ===
  _out -> \"=== map() ===\"\n  nums<numbers>
  _add(numbers, 0, 1)
  _add(numbers, 1, 2)
  _add(numbers, 2, 3)
  
  mapped -> map(\"double\", numbers)
  _out -> mapped[0]
  _out -> mapped[1]
  _out -> mapped[2]
  
  ; === filter() ===
  _out -> \"=== filter() ===\"\n  evens -> filter(\"is_even\", numbers)
  _out -> evens[0]
  
  ; === Passing structs to functions ===
  _out -> \"=== Structs ===\"\n  p -> Person{}
  p.name -> \"Alice\"\n  p.age -> 30
  _out -> p.name + \" is \" + p.age
  
  p2 -> birthday(p)
  _out -> p2.name + \" is now \" + p2.age
  
  ; === Dynamic list creation inside function ===
  _out -> \"=== Dynamic lists ===\"\n  make_list()
    temp<templist>
    _add(templist, 0, \"apple\")\n    _add(templist, 1, \"banana\")\n    _return -> templist
  end
  
  fruits -> make_list()
  _out -> fruits[0]
  _out -> fruits[1]
  
  ; === Nested struct properties ===
  _out -> \"=== Nested structs ===\"\n  Item{}\n    name -> \"Sword\"\n    damage -> 10
  end
  
  p2.weapon -> Item{}
  _out -> p2.weapon.name
  p2.weapon.damage -> 25
  _out -> p2.weapon.damage
end
