// Calculator in Sol:
/*
Features:
- Robust error handling with the Result<T, E> type
- No if-else boilerplate, match statements are used here
- Dynamic input with std.in()
- Type safe function declarations with explicit return types
- Immediate and Non-Immediate variable bindings!
*/
fun add(a: float, b: float): float
  ret a + b
end

fun subtract(a: float, b: float): float
  ret a - b
end

fun multiply(a: float, b: float): float
  ret a * b
end

fun divide(a: float, b: float): Result<float, string>
  if (b == 0.0)
    ret Err("Cannot divide by 0!")
  end
  ret Ok(a / b)
end

fun power(a: float, b: float): float
  ret a ** b
end

fun modulus(a: float, b: float): Result<float, string>
  if (b == 0.0)
    ret Err("Cannot modulo by zero!")
  end
  ret Ok(a % b)
end

fun showMenu(): nothing
  std.outln("")
  std.outln("=== Sol Calculator ===")
  std.outln("1. Add")
  std.outln("2. Subtract")
  std.outln("3. Multiply")
  std.outln("4. Divide")
  std.outln("5. Power")
  std.outln("6. Modulus")
  std.outln("7. QUIT")
  std.outln("")
end

fun getNumber(prompt: string): float
  std.outln(prompt)
  imm input: string -> std.in("")
  ret type.iToFloat(type.strToInteger(input))
end

fun doMath(choice: string): boolean
  match (choice)
    "1" ->
        imm a: float -> getNumber("Enter first number")
        imm b: float -> getNumber("Enter second number")
        std.outln("Result: " + type.toString(add(a, b)))
        ret true
    "2" ->
        imm a: float -> getNumber("Enter first number")
        imm b: float -> getNumber("Enter second number")
        std.outln("Result: " + type.toString(subtract(a, b)))
        ret true
    "3" ->
        imm a: float -> getNumber("Enter first number")
        imm b: float -> getNumber("Enter second number")
        std.outln("Result: " + type.toString(multiply(a, b)))
        ret true
    "4" ->
        imm a: float -> getNumber("Enter first number")
        imm b: float -> getNumber("Enter second number")
        imm result: Result<float, string> -> divide(a, b)
        if (result.isOk(result))
          std.outln("Result: " + type.toString(result))
        else
          std.outln("Error: " + result.unwrapOrElse(result, ld() ret "Unknown Error" end))
        end
        ret true 
    "5" ->
        imm a: float -> getNumber("Enter first number")
        imm b: float -> getNumber("Enter second number")
        std.outln("Result: " + type.toString(power(a, b)))
        ret true
    "6" ->
        imm a: float -> getNumber("Enter first number")
        imm b: float -> getNumber("Enter second number")
        imm result: Result<float, string> -> modulus(a, b)
        if (result.isOk(result))
          std.outln("Result: " + type.toString(result))
        else
          std.outln("Error: " + result.unwrapOrElse(result, ld() ret "Unknown Error" end))
        end
        ret true
    "7" -> 
        std.outln("Goodbye!")
        ret false
    _ ->
        std.outln("Invalid choice. Please try again, selecting one of the valid inputs.")
        ret true
  end
end

fun main(): nothing
  imm running: boolean -> true
  while (running)
    showMenu()
    std.outln("Choose an option ( 1 - 7 )")
    imm choice: string -> std.in("")
    running -> doMath(choice)
  end
end

main()
