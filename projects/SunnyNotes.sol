// Notes app: SunnyNotes
// Version 2
/*
Added a `deleteNote()` function
*/

templ Note
  name: string
  desc: string
end

imm Notes: map -> {}

fun addNote(name: string, desc: string): map
  imm n: Note -> Note(name, desc)
  Notes -> map.set(Notes, n.name, n.desc)
  ret Notes
end

fun printNotes(n: map): nothing
  std.outln(" === Notes === ")
  for (notes in n)
    std.outln(n.name)
    std.outln(n.desc)
    std.outln(" ========= ")
  end
end

fun deleteNote(n: map, name: string): map
  imm New: Map -> map.set(n, name, "")
  ret New
end

fun main(): nothing
  std.outln(" | === SunnyNotes 1.0 === |")
  std.outln(" | Welcome to SunnyNotes! |")
  std.outln(" | Type `add` to add a Note! |")
  std.outln(" | Type `show` to show all Notes! |")
  std.outln(" | ====================== |")
  imm input: string -> std.in("> ")
  match (input)
    "add" ->
      imm name: string -> std.in(" - Name? ")
      imm desc: string -> std.in(" - Description? ")
      Notes -> addNote(name, desc)
    "show" ->
      printNotes(Notes)
    "delete" -> 
      imm in: string -> std.in(" - Note to Delete? (name) ")
      deleteNote(Notes, in)
     _ -> std.outln(" ! INVALID COMMAND !")
  end
end

fun forever(): nothing
  for (imm i: integer -> -1; i < 0; i -> i - 1)
    main()
  end
end

forever()
