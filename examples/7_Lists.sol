main()
  ; NAME<REFERENCE_NAME>
  list1<inventory>

  ; Methods:

  ; _add(LIST, INDEX, VALUE)
  ; _remove(LIST, INDEX)
  ; Lists start at index 0
  _add(inventory, 0, 2)
  _add(inventory, 1, 2)
  _out -> inventory[1] 
end
