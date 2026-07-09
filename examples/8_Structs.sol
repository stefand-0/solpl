; Structs are defined with "{}",
; there is no seperate keyword for them

Player{}
  name -> "Sam"
  level -> 1
end

main()
  ; Initialising a copy of Person{}
  Guy -> Person{}
  ; Accessing properties:
  _out -> Guy.name
  ; Changing properties:
  Player.name -> "Bob"
end
