main()
  ; Here, we are going to check if a string is empty.
  _get("std/str/String.sol")
  string -> ""
  isEmpty -> String.empty(string)
  isEmpty = 1 ? _out -> "Empty!"

  ; Now, checking if a String list contains a character.
  list<ls>
  _add(ls, 1, "A")
  _add(ls, 2, "B")
  hasChar -> String.contains_char("A")
  hasChar = 1 ? _out -> "Has A!"

  ; There are many more methods in String.sol
  ; Now, let's make a JSON Key:Value
  myKV -> String.to_json_kv("name", "guy")
  _out -> myKV
end
