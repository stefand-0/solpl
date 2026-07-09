; Structs are defined with "{}",
; there is no seperate keyword for them

Player{}
  name -> "Sam"
  level -> 1
end

main()
  ; Accessing properties:
  _out -> Player.name
  ; Changing properties:
  Player.name -> "Bob"
end
