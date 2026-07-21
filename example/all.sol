// ============================================================
// SOL - Simple demonstration..
// ============================================================

fun main(): nothing
    std.outln("=== SOL Data Types Demo ===")
    std.outln("")
    
    // --- Integer Types ---
    std.outln("--- Integer Types ---")
    imm a: integer -> 42
    std.outln("integer: " + type.toString(a))
    imm b: int16 -> 100
    std.outln("int16: " + type.toString(b))
    imm c: int32 -> 1000
    std.outln("int32: " + type.toString(c))
    imm d: int64 -> 10000
    std.outln("int64: " + type.toString(d))
    std.outln("")
    
    // --- Float Types ---
    std.outln("--- Float Types ---")
    imm pi: float -> 3.14159
    std.outln("float: " + type.toString(pi))
    imm f32: float32 -> 2.5
    std.outln("float32: " + type.toString(f32))
    imm f64: float64 -> 9.8
    std.outln("float64: " + type.toString(f64))
    std.outln("")
    
    // --- Boolean ---
    std.outln("--- Boolean ---")
    imm t: boolean -> true
    imm f: boolean -> false
    std.outln("true: " + type.toString(t))
    std.outln("false: " + type.toString(f))
    std.outln("")
    
    // --- String ---
    std.outln("--- String ---")
    imm greeting: string -> "Hello, SOL!"
    std.outln("string: " + greeting)
    std.outln("upper: " + string.upper(greeting))
    std.outln("lower: " + string.lower(greeting))
    std.outln("length: " + type.toString(string.length(greeting)))
    std.outln("trim: \"" + string.trim("  spaces  ") + "\"")
    std.outln("")
    
    // --- Char ---
    std.outln("--- Char ---")
    imm ch: char -> 'X'
    std.outln("char: " + ch)
    std.outln("")
    
    // --- Number Literals ---
    std.outln("--- Number Literals ---")
    imm hexVal: integer -> 0xFF
    std.outln("hex 0xFF: " + type.toString(hexVal))
    imm octVal: integer -> 0o755
    std.outln("oct 0o755: " + type.toString(octVal))
    imm binVal: integer -> 0b1010
    std.outln("bin 0b1010: " + type.toString(binVal))
    std.outln("")
    
    // --- Type Conversions ---
    std.outln("--- Type Conversions ---")
    imm strFromInt: string -> type.toString(42)
    std.outln("toString(42): " + strFromInt)
    imm intFromStr: integer -> type.strToInteger("123")
    std.outln("strToInteger(\"123\"): " + type.toString(intFromStr))
    imm floatFromInt: float -> type.iToFloat(5)
    std.outln("iToFloat(5): " + type.toString(floatFromInt))
    imm intFromFloat: integer -> type.flToInt(3.14)
    std.outln("flToInt(3.14): " + type.toString(intFromFloat))
    imm hexStr: string -> type.iToHex(255)
    std.outln("iToHex(255): " + hexStr)
    imm octStr: string -> type.iToOct(8)
    std.outln("iToOct(8): " + octStr)
    imm boolFromInt: boolean -> type.intToBool(1)
    std.outln("intToBool(1): " + type.toString(boolFromInt))
    imm intFromBool: integer -> type.boolToInt(true)
    std.outln("boolToInt(true): " + type.toString(intFromBool))
    std.outln("")
    
    // --- List ---
    std.outln("--- List ---")
    imm nums: list -> [1, 2, 3, 4, 5]
    std.outln("list: " + type.toString(nums))
    std.outln("len: " + type.toString(list.len(nums)))
    std.outln("first: " + type.toString(list.first(nums)))
    std.outln("last: " + type.toString(list.last(nums)))
    imm pushed: list -> list.push(nums, 6)
    std.outln("push(6): " + type.toString(pushed))
    imm sorted: list -> list.sort([3, 1, 4, 1, 5])
    std.outln("sort: " + type.toString(sorted))
    imm reversed: list -> list.reverse(nums)
    std.outln("reverse: " + type.toString(reversed))
    std.outln("")
    
    // --- Map ---
    std.outln("--- Map ---")
    imm user: map -> {}
    user -> map.set(user, "name", "Alice")
    user -> map.set(user, "age", 30)
    std.outln("map: " + type.toString(user))
    std.outln("get name: " + map.get(user, "name"))
    std.outln("get age: " + type.toString(map.get(user, "age")))
    std.outln("keys: " + type.toString(map.keys(user)))
    std.outln("len: " + type.toString(map.len(user)))
    std.outln("")
    
    // --- Vector ---
    std.outln("--- Vector ---")
    imm points: vect -> <<1, 2>> <<3, 4>> <<5, 6>>
    std.outln("vect: " + type.toString(points))
    std.outln("")
    
    // --- Result ---
    std.outln("--- Result ---")
    imm okVal: Result<integer, string> -> Ok(42)
    imm errVal: Result<integer, string> -> Err("something went wrong")
    std.outln("Ok(42): " + type.toString(result.isOk(okVal)))
    std.outln("unwrap Ok: " + type.toString(result.unwrap(okVal)))
    std.outln("Err: " + type.toString(result.isErr(errVal)))
    std.outln("unwrapOr Err: " + type.toString(result.unwrapOr(errVal, 0)))
    std.outln("")
    
    // --- Template ---
    std.outln("--- Template ---")
    templ Person
        name: string
        age: integer
    end
    imm alice: Person -> Person("Alice", 30)
    std.outln("Person.name: " + alice.name)
    std.outln("Person.age: " + type.toString(alice.age))
    alice.age -> 31
    std.outln("After birthday: " + type.toString(alice.age))
    std.outln("")
    
    // --- Data (immutable) ---
    std.outln("--- Data ---")
    data Point
        x: float
        y: float
    end
    imm p: Point -> Point(3.0, 4.0)
    std.outln("Point.x: " + type.toString(p.x))
    std.outln("Point.y: " + type.toString(p.y))
    std.outln("")
    
    // --- Nothing ---
    std.outln("--- Nothing ---")
    imm empty: nothing -> nothing
    std.outln("nothing: " + type.toString(empty))
    std.outln("")
    
    // --- Arithmetic & Logic ---
    std.outln("--- Arithmetic & Logic ---")
    std.outln("5 + 3 = " + type.toString(5 + 3))
    std.outln("10 - 4 = " + type.toString(10 - 4))
    std.outln("6 * 7 = " + type.toString(6 * 7))
    std.outln("20 / 4 = " + type.toString(20 / 4))
    std.outln("17 % 5 = " + type.toString(17 % 5))
    std.outln("2 ** 8 = " + type.toString(2 ** 8))
    std.outln("5 == 5: " + type.toString(5 == 5))
    std.outln("5 != 3: " + type.toString(5 != 3))
    std.outln("10 > 5: " + type.toString(10 > 5))
    std.outln("true && false: " + type.toString(true && false))
    std.outln("true || false: " + type.toString(true || false))
    std.outln("!true: " + type.toString(!true))
    std.outln("")
    
    // --- Control Flow ---
    std.outln("--- Control Flow ---")
    imm score: integer -> 85
    if (score >= 90)
        std.outln("Grade: A")
    elseif (score >= 80)
        std.outln("Grade: B")
    elseif (score >= 70)
        std.outln("Grade: C")
    else
        std.outln("Grade: F")
    end
    
    nonimm counter: integer -> 3
    while (counter > 0)
        std.outln("countdown: " + type.toString(counter))
        counter -> counter - 1
    end
    
    for (imm i: integer -> 0; i < 3; i -> i + 1)
        std.outln("for loop i=" + type.toString(i))
    end
    
    imm fruits: list -> ["apple", "banana", "cherry"]
    for (fruit in fruits)
        std.outln("fruit: " + fruit)
    end
    std.outln("")
    
    // --- Match ---
    std.outln("--- Match ---")
    imm dayNum: integer -> 3
    match (dayNum)
        1 -> std.outln("Monday")
        2 -> std.outln("Tuesday")
        3 -> std.outln("Wednesday")
        _ -> std.outln("Other day")
    end
    std.outln("")
    
    // --- Functions ---
    std.outln("--- Functions ---")
    std.outln("add(10, 20) = " + type.toString(add(10, 20)))
    std.outln("greet(\"Bob\") = " + greet("Bob"))
    std.outln("factorial(6) = " + type.toString(factorial(6)))
    std.outln("")
    
    std.outln("=== Demo Complete ===")
end

fun add(a: integer, b: integer): integer
    ret a + b
end

fun greet(name: string): string
    ret "Hello, " + name + "!"
end

fun factorial(n: integer): integer
    if (n <= 1)
        ret 1
    end
    ret n * factorial(n - 1)
end

main()
