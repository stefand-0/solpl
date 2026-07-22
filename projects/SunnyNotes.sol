// Notes app: SunnyNotes

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

fun main(): nothing
  std.outln(" === SunnyNotes 1.0 === ")
  std.outln(" - Welcome to SunnyNotes! ")
  std.outln(" - Type "add NAME, DESCRIPTION" to add a note! ")
  std.outln(" - Type "show" to show all notes! ")
  imm input: string -> std.in("> ")
  match (input)
    "add" ->
      imm name: string -> std.in(" - Name? ")
      imm desc: string -> std.in(" - Description? ")
      addNote(name, desc)
    "show" ->
      printNotes(Notes)
     _ -> std.outln(" ! INVALID COMMAND !")
  end
end
