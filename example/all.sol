// ============================================================
// SOL Programming Language - Example Syntax File
// ============================================================

// --------------------------------------------------
// 1. Variable Declarations
// --------------------------------------------------

imm name: string -> "Alice"
imm age: integer -> 30
imm pi: float -> 3.14159
imm isActive: boolean -> true
imm empty: string
imm scores: list

nonimm counter: integer -> 0
nonimm message: string -> "Hello, SOL!"

// --------------------------------------------------
// 2. Type Literals
// --------------------------------------------------

imm hexVal: integer -> 0xFF
imm octVal: integer -> 0o755
imm binVal: integer -> 0b1010
imm charVal: char -> 'A'

// --------------------------------------------------
// 3. Functions
// --------------------------------------------------

fun greet(name: string): string
    ret "Hello, " + name + "!"
end

fun add(a: integer, b: integer): integer
    ret a + b
end

fun factorial(n: integer): integer
    if (n <= 1)
        ret 1
    end
    ret n * factorial(n - 1)
end

fun safeDivide(a: float, b: float): Result<float, string>
    if (b == 0)
        ret Err("Division by zero!")
    end
    ret Ok(a / b)
end

// Generic function
fun identity<T>(val: T): T
    ret val
end

// --------------------------------------------------
// 4. Templates (Mutable Structs)
// --------------------------------------------------

templ Person
    name: string
    age: integer
    email: string
end

// Create a Person instance
imm person: Person -> Person("Bob", 25, "bob@example.com")

// --------------------------------------------------
// 5. Data (Immutable Structs)
// --------------------------------------------------

data Point
    x: float
    y: float
end

data Color
    r: integer
    g: integer
    b: integer
end

// --------------------------------------------------
// 6. Interfaces
// --------------------------------------------------

interface Drawable
    fun draw(): string
end

interface Movable
    fun move(dx: float, dy: float): void
end

// --------------------------------------------------
// 7. Extensions
// --------------------------------------------------

ext integer.isEven(): boolean
    ret (this % 2) == 0
end

ext string.isPalindrome(): boolean
    imm reversed: string -> string.reverse(this)
    ret this == reversed
end

ext list.sum(): integer
    imm total: integer -> 0
    for (item in this)
        total -> total + item
    end
    ret total
end

// --------------------------------------------------
// 8. Control Flow
// --------------------------------------------------

// If-ElseIf-Else
fun grade(score: integer): string
    if (score >= 90)
        ret "A"
    elseif (score >= 80)
        ret "B"
    elseif (score >= 70)
        ret "C"
    elseif (score >= 60)
        ret "D"
    else
        ret "F"
    end
end

// While loop
fun countdown(start: integer): void
    nonimm i: integer -> start
    while (i > 0)
        std.outln(i)
        i -> i - 1
    end
end

// For loop (C-style)
fun sumTo(n: integer): integer
    imm total: integer -> 0
    for (imm i: integer -> 0; i <= n; i -> i + 1)
        total -> total + i
    end
    ret total
end

// For-in loop
fun printNames(names: list): void
    for (name in names)
        std.outln(name)
    end
end

// --------------------------------------------------
// 9. Match Expressions
// --------------------------------------------------

fun describe(value: integer): string
    match (value)
        0 -> ret "zero"
        1 -> ret "one"
        _ -> ret "something else"
    end
end

fun classifyPoint(p: Point): string
    match (p)
        Point(0, 0) -> ret "origin"
        Point(x, 0) -> ret "on x-axis"
        Point(0, y) -> ret "on y-axis"
        _ -> ret "somewhere in space"
    end
end

// --------------------------------------------------
// 10. Lambda Expressions
// --------------------------------------------------

imm double: ld(x: integer): integer
    ret x * 2
end

imm apply: ld(fn: ld, val: integer): integer
    ret fn(val)
end

// --------------------------------------------------
// 11. Result Type
// --------------------------------------------------

fun parseInt(s: string): Result<integer, string>
    if (string.isnumeric(s))
        ret Ok(type.strToInteger(s))
    end
    ret Err("Not a valid integer: " + s)
end

fun useResult(): void
    imm r: Result<integer, string> -> parseInt("42")
    if (result.isOk(r))
        std.outln("Parsed: " + type.toString(result.unwrap(r)))
    else
        std.outln("Error: " + result.unwrapOrElse(r, ld() ret "default" end))
    end
end

// --------------------------------------------------
// 12. Lists and Maps
// --------------------------------------------------

imm numbers: list -> [1, 2, 3, 4, 5]
imm doubled: list -> list.map(numbers, ld(x) ret x * 2 end)
imm filtered: list -> list.filter(numbers, ld(x) ret x > 2 end)

imm user: map -> {}
user -> map.set(user, "name", "Alice")
user -> map.set(user, "age", 30)
imm userName: string -> map.get(user, "name")

// --------------------------------------------------
// 13. Vectors (2D points)
// --------------------------------------------------

imm points: vect -> <<1, 2>> <<3, 4>> <<5, 6>>

// --------------------------------------------------
// 14. String Operations
// --------------------------------------------------

imm text: string -> "  hello world  "
imm trimmed: string -> string.trim(text)
imm upper: string -> string.upper(text)
imm lower: string -> string.lower(text)
imm title: string -> string.titlecase(text)
imm camel: string -> string.camelcase("hello_world")
imm snake: string -> string.snakecase("hello world")
imm kebab: string -> string.kebabcase("hello world")

// --------------------------------------------------
// 15. Type Conversions
// --------------------------------------------------

imm strNum: string -> type.toString(42)
imm intFromStr: integer -> type.strToInteger("123")
imm floatFromInt: float -> type.iToFloat(5)
imm intFromFloat: integer -> type.flToInt(3.14)
imm hexStr: string -> type.iToHex(255)
imm octStr: string -> type.iToOct(8)
imm boolVal: boolean -> type.intToBool(1)
imm intBool: integer -> type.boolToInt(true)

// --------------------------------------------------
// 16. Operators
// --------------------------------------------------

fun demonstrateOperators(): void
    imm a: integer -> 10
    imm b: integer -> 3
    
    // Arithmetic
    std.outln(a + b)   // 13
    std.outln(a - b)   // 7
    std.outln(a * b)   // 30
    std.outln(a / b)   // 3.333...
    std.outln(a % b)   // 1
    std.outln(a ** b)  // 1000
    
    // Comparison
    std.outln(a == b)  // false
    std.outln(a != b)  // true
    std.outln(a < b)   // false
    std.outln(a > b)   // true
    std.outln(a <= b)  // false
    std.outln(a >= b)  // true
    
    // Logical
    std.outln(true && false)  // false
    std.outln(true || false)  // true
    std.outln(!true)          // false
    
    // Bitwise
    std.outln(a & b)   // 2
    std.outln(a | b)   // 11
    std.outln(a ^ b)   // 9
    std.outln(~a)      // -11
    std.outln(a << 1)  // 20
    std.outln(a >> 1)  // 5
    
    // Elvis operator
    imm maybeNull: string -> nothing
    imm fallback: string -> maybeNull ?: "fallback"
    std.outln(fallback)  // "fallback"
    
    // Safe access
    imm maybeUser: Person -> nothing
    std.outln(maybeUser?.name)  // null (safe)
end

// --------------------------------------------------
// 17. Ternary Operator
// --------------------------------------------------

fun max(a: integer, b: integer): integer
    ret (a > b) ? a : b
end

// --------------------------------------------------
// 18. Modules and Imports
// --------------------------------------------------

// import "math.sol"
// import "utils.sol" as utils
// module myModule = load("module.sol")

// --------------------------------------------------
// 19. Break and Continue
// --------------------------------------------------

fun findFirstEven(numbers: list): integer
    for (n in numbers)
        if (n % 2 == 0)
            ret n
        end
    end
    ret -1
end

fun skipOdds(numbers: list): void
    for (n in numbers)
        if (n % 2 != 0)
            continue
        end
        std.outln(n)
    end
end

// --------------------------------------------------
// 20. Complex Example: A Mini Program
// --------------------------------------------------

fun main(): void
    // Greeting
    std.outln(greet("World"))
    
    // Math
    std.outln("5 + 3 = " + type.toString(add(5, 3)))
    std.outln("5! = " + type.toString(factorial(5)))
    
    // Result handling
    imm divResult: Result<float, string> -> safeDivide(10, 2)
    std.outln("10 / 2 = " + type.toString(result.unwrapOr(divResult, 0.0)))
    
    imm badDiv: Result<float, string> -> safeDivide(10, 0)
    std.outln("Error: " + result.unwrapOrElse(badDiv, ld() ret "Cannot divide" end))
    
    // List operations
    imm nums: list -> [3, 1, 4, 1, 5, 9, 2, 6]
    std.outln("Original: " + type.toString(nums))
    std.outln("Sorted: " + type.toString(list.sort(nums)))
    std.outln("Reversed: " + type.toString(list.reverse(nums)))
    std.outln("Length: " + type.toString(list.len(nums)))
    
    // String operations
    std.outln(string.upper("sol language"))
    std.outln(string.camelcase("hello_world_example"))
    
    // Control flow
    std.outln("Grade for 85: " + grade(85))
    
    // Match
    std.outln("Describe 0: " + describe(0))
    std.outln("Describe 7: " + describe(7))
    
    // Point
    imm p: Point -> Point(3.0, 4.0)
    std.outln("Point classification: " + classifyPoint(p))
    
    // Countdown
    std.outln("Countdown:")
    countdown(5)
    
    // Type conversions
    std.outln("Hex of 255: " + type.iToHex(255))
    std.outln("Oct of 8: " + type.iToOct(8))
end

// Run main
main()
