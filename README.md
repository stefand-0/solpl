
# Create an amazing README with animated SVG badges, feature cards, and the new syntax

readme_content = """<div align="center">

<!-- Animated SOL Banner -->
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200" viewBox="0 0 800 200">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1a1a2e">
        <animate attributeName="stop-color" values="#1a1a2e;#16213e;#1a1a2e" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#0f3460">
        <animate attributeName="stop-color" values="#0f3460;#e94560;#0f3460" dur="8s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="800" height="200" fill="url(#bg)" rx="12"/>
  
  <!-- Animated floating particles -->
  <circle cx="100" cy="50" r="3" fill="#ffb000" opacity="0.6">
    <animate attributeName="cy" values="50;30;50" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0.2;0.6" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="150" r="4" fill="#e94560" opacity="0.5">
    <animate attributeName="cy" values="150;170;150" dur="5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.5;0.1;0.5" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="400" cy="30" r="2" fill="#fff" opacity="0.4">
    <animate attributeName="cy" values="30;20;30" dur="3s" repeatCount="indefinite"/>
  </circle>
  
  <!-- SOL Logo -->
  <text x="400" y="100" text-anchor="middle" font-family="'Courier New', monospace" font-size="72" font-weight="bold" fill="#ffb000" filter="url(#glow)">
    <animate attributeName="opacity" values="0.8;1;0.8" dur="3s" repeatCount="indefinite"/>
    SOL
  </text>
  <text x="400" y="140" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="20" fill="#fff" opacity="0.9">
    <animate attributeName="opacity" values="0.7;1;0.7" dur="4s" repeatCount="indefinite"/>
    ☀️ The Sunny Programming Language
  </text>
  <text x="400" y="170" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="14" fill="#aaa">
    Typed • Expressive • Delightful
  </text>
</svg>

<!-- Animated Status Badges Row -->
<svg xmlns="http://www.w3.org/2000/svg" width="700" height="40" viewBox="0 0 700 40">
  <!-- Version Badge -->
  <g transform="translate(0,0)">
    <rect width="120" height="28" rx="4" fill="#555"/>
    <rect x="60" width="60" height="28" rx="4" fill="#ffb000"/>
    <text x="30" y="19" text-anchor="middle" font-family="Verdana,sans-serif" font-size="11" fill="#fff">VERSION</text>
    <text x="90" y="19" text-anchor="middle" font-family="Verdana,sans-serif" font-size="11" font-weight="bold" fill="#333">0.1.0</text>
    <animateTransform attributeName="transform" type="translate" values="0,0; 0,-2; 0,0" dur="2s" repeatCount="indefinite"/>
  </g>
  
  <!-- Python Badge -->
  <g transform="translate(130,0)">
    <rect width="110" height="28" rx="4" fill="#555"/>
    <rect x="60" width="50" height="28" rx="4" fill="#3776ab"/>
    <text x="30" y="19" text-anchor="middle" font-family="Verdana,sans-serif" font-size="11" fill="#fff">BUILT</text>
    <text x="85" y="19" text-anchor="middle" font-family="Verdana,sans-serif" font-size="11" font-weight="bold" fill="#fff">PY</text>
    <animateTransform attributeName="transform" type="translate" values="130,0; 130,-2; 130,0" dur="2.2s" repeatCount="indefinite"/>
  </g>
  
  <!-- License Badge -->
  <g transform="translate(250,0)">
    <rect width="110" height="28" rx="4" fill="#555"/>
    <rect x="60" width="50" height="28" rx="4" fill="#4c1"/>
    <text x="30" y="19" text-anchor="middle" font-family="Verdana,sans-serif" font-size="11" fill="#fff">LICENSE</text>
    <text x="85" y="19" text-anchor="middle" font-family="Verdana,sans-serif" font-size="11" font-weight="bold" fill="#fff">MIT</text>
    <animateTransform attributeName="transform" type="translate" values="250,0; 250,-2; 250,0" dur="2.4s" repeatCount="indefinite"/>
  </g>
  
  <!-- Status Badge -->
  <g transform="translate(370,0)">
    <rect width="120" height="28" rx="4" fill="#555"/>
    <rect x="60" width="60" height="28" rx="4" fill="#e94560"/>
    <text x="30" y="19" text-anchor="middle" font-family="Verdana,sans-serif" font-size="11" fill="#fff">STATUS</text>
    <text x="90" y="19" text-anchor="middle" font-family="Verdana,sans-serif" font-size="10" font-weight="bold" fill="#fff">BETA</text>
    <animateTransform attributeName="transform" type="translate" values="370,0; 370,-2; 370,0" dur="2.6s" repeatCount="indefinite"/>
  </g>
  
  <!-- Tests Badge -->
  <g transform="translate(500,0)">
    <rect width="110" height="28" rx="4" fill="#555"/>
    <rect x="55" width="55" height="28" rx="4" fill="#9cf"/>
    <text x="27" y="19" text-anchor="middle" font-family="Verdana,sans-serif" font-size="11" fill="#fff">TESTS</text>
    <text x="82" y="19" text-anchor="middle" font-family="Verdana,sans-serif" font-size="11" font-weight="bold" fill="#333">PASS</text>
    <animateTransform attributeName="transform" type="translate" values="500,0; 500,-2; 500,0" dur="2.8s" repeatCount="indefinite"/>
  </g>
</svg>

<br>

<!-- Animated divider -->
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="4" viewBox="0 0 600 4">
  <line x1="0" y1="2" x2="600" y2="2" stroke="#ffb000" stroke-width="2" stroke-linecap="round" stroke-dasharray="20,10">
    <animate attributeName="stroke-dashoffset" values="0;-30" dur="1s" repeatCount="indefinite"/>
  </line>
</svg>

</div>

## 🚀 What is SOL?

**SOL** is a modern, expressive programming language designed for clarity and joy. Named after the Latin word for *sun* ☀️, SOL brings warmth to systems programming with a clean syntax, powerful type system, and delightful standard library.

```sol
// Hello, SOL!
imm greeting: string -> "Hello, World!"
std.outln(greeting)

fun fib(n: integer): integer
    if (n <= 1)
        ret n
    end
    ret fib(n - 1) + fib(n - 2)
end

std.outln(fib(10))  // 55
```

## ✨ Features

<div align="center">

<!-- Feature Cards Grid -->
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="420" viewBox="0 0 720 420">
  <defs>
    <linearGradient id="card1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1a1a2e"/>
      <stop offset="100%" stop-color="#16213e"/>
    </linearGradient>
    <linearGradient id="card2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#16213e"/>
      <stop offset="100%" stop-color="#0f3460"/>
    </linearGradient>
    <linearGradient id="card3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f3460"/>
      <stop offset="100%" stop-color="#1a1a2e"/>
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Card 1: Strong Types -->
  <g transform="translate(10,10)">
    <rect width="220" height="120" rx="12" fill="url(#card1)" filter="url(#shadow)" stroke="#ffb000" stroke-width="1" opacity="0.9">
      <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="3s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="35" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="16" font-weight="bold" fill="#ffb000">🔒 Strong Types</text>
    <text x="110" y="60" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#9cf">imm x: integer -> 42</text>
    <text x="110" y="80" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#9cf">imm name: string -> "sol"</text>
    <text x="110" y="105" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">Runtime type checking with</text>
    <text x="110" y="118" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">contracts on every call</text>
  </g>
  
  <!-- Card 2: Result<T,E> -->
  <g transform="translate(250,10)">
    <rect width="220" height="120" rx="12" fill="url(#card2)" filter="url(#shadow)" stroke="#e94560" stroke-width="1" opacity="0.9">
      <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="3.5s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="35" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="16" font-weight="bold" fill="#e94560">🛡️ Result&lt;T,E&gt;</text>
    <text x="110" y="60" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#fca">imm r: Result -> Ok(42)</text>
    <text x="110" y="80" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#fca">result.unwrapOr(r, 0)</text>
    <text x="110" y="105" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">Explicit error handling</text>
    <text x="110" y="118" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">without exceptions</text>
  </g>
  
  <!-- Card 3: Templates -->
  <g transform="translate(490,10)">
    <rect width="220" height="120" rx="12" fill="url(#card3)" filter="url(#shadow)" stroke="#4c1" stroke-width="1" opacity="0.9">
      <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="4s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="35" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="16" font-weight="bold" fill="#4c1">📐 Templates</text>
    <text x="110" y="60" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#9f9">templ Point</text>
    <text x="110" y="75" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#9f9">  x: integer</text>
    <text x="110" y="90" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#9f9">  y: integer</text>
    <text x="110" y="105" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#9f9">end</text>
    <text x="110" y="118" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">Immutable data structures</text>
  </g>
  
  <!-- Card 4: Pattern Matching -->
  <g transform="translate(10,150)">
    <rect width="220" height="120" rx="12" fill="url(#card2)" filter="url(#shadow)" stroke="#9cf" stroke-width="1" opacity="0.9">
      <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="3.2s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="35" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="16" font-weight="bold" fill="#9cf">🎯 Match</text>
    <text x="110" y="60" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#ccf">match (x)</text>
    <text x="110" y="75" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#ccf">  42 -> "yes"</text>
    <text x="110" y="90" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#ccf">  _ -> "no"</text>
    <text x="110" y="105" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#ccf">end</text>
    <text x="110" y="118" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">Powerful pattern matching</text>
  </g>
  
  <!-- Card 5: Lambdas -->
  <g transform="translate(250,150)">
    <rect width="220" height="120" rx="12" fill="url(#card3)" filter="url(#shadow)" stroke="#f9c" stroke-width="1" opacity="0.9">
      <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="3.7s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="35" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="16" font-weight="bold" fill="#f9c">λ Lambdas</text>
    <text x="110" y="60" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#fcf">ld (n: integer)</text>
    <text x="110" y="75" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#fcf">  ret n * 2</text>
    <text x="110" y="90" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#fcf">end</text>
    <text x="110" y="110" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">First-class anonymous</text>
    <text x="110" y="123" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">functions with closures</text>
  </g>
  
  <!-- Card 6: Safe Access -->
  <g transform="translate(490,150)">
    <rect width="220" height="120" rx="12" fill="url(#card1)" filter="url(#shadow)" stroke="#ffb000" stroke-width="1" opacity="0.9">
      <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="4.2s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="35" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="16" font-weight="bold" fill="#ffb000">🛟 Safe Access</text>
    <text x="110" y="60" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#ff9">obj?.field</text>
    <text x="110" y="80" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#ff9">maybe ?: "default"</text>
    <text x="110" y="105" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">Null-safe navigation and</text>
    <text x="110" y="118" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">Elvis operator for defaults</text>
  </g>
  
  <!-- Card 7: For Loops -->
  <g transform="translate(10,290)">
    <rect width="220" height="120" rx="12" fill="url(#card3)" filter="url(#shadow)" stroke="#4c1" stroke-width="1" opacity="0.9">
      <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="3.3s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="35" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="16" font-weight="bold" fill="#4c1">🔁 For Loops</text>
    <text x="110" y="60" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#9f9">for (i in list)</text>
    <text x="110" y="75" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#9f9">for (i->0; i<10; i->i+1)</text>
    <text x="110" y="95" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#9f9">while (cond)</text>
    <text x="110" y="118" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">For-in, C-style, and while</text>
  </g>
  
  <!-- Card 8: Bitwise -->
  <g transform="translate(250,290)">
    <rect width="220" height="120" rx="12" fill="url(#card1)" filter="url(#shadow)" stroke="#e94560" stroke-width="1" opacity="0.9">
      <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="3.8s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="35" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="16" font-weight="bold" fill="#e94560">⚡ Bitwise</text>
    <text x="110" y="60" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#fcc">& | ^ ~ << >></text>
    <text x="110" y="80" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#fcc">&& || ! == !=</text>
    <text x="110" y="105" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">Full bitwise and logical</text>
    <text x="110" y="118" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">operator support</text>
  </g>
  
  <!-- Card 9: Stdlib -->
  <g transform="translate(490,290)">
    <rect width="220" height="120" rx="12" fill="url(#card2)" filter="url(#shadow)" stroke="#9cf" stroke-width="1" opacity="0.9">
      <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="4.3s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="35" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="16" font-weight="bold" fill="#9cf">📚 Stdlib</text>
    <text x="110" y="60" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#ccf">string.camelcase()</text>
    <text x="110" y="75" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#ccf">list.sort() map.get()</text>
    <text x="110" y="90" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#ccf">std.load() std.save()</text>
    <text x="110" y="110" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">Rich standard library for</text>
    <text x="110" y="123" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="10" fill="#aaa">strings, lists, maps, I/O</text>
  </g>
</svg>

</div>

## 📦 Installation

```bash
git clone https://github.com/stefand-0/sol-lang.git
cd sol-lang
python sol.py your_program.sol
```

## 🎮 Quick Start

### Variables & Types

```sol
// Immediate variables
imm name: string -> "SOL"
imm count: integer -> 42
imm pi: float -> 3.14159
imm active: boolean -> true

// Nullable types
imm maybe: nothing -> nothing
std.outln(maybe ?: "default")  // "default"
```

### Functions

```sol
fun greet(user: string): string
    ret "Hello, " + user + "!"
end

std.outln(greet("World"))  // Hello, World!

// With type contracts enforced at runtime
fun add(a: integer, b: integer): integer
    ret a + b
end

std.outln(add(5, 3))  // 8
```

### Control Flow

```sol
// If/elseif/else
imm score: integer -> 85
if (score >= 90)
    std.outln("A")
elseif (score >= 80)
    std.outln("B")
else
    std.outln("C")
end

// While loop
imm i: integer -> 0
while (i < 5)
    std.outln(i)
    i -> i + 1
end

// For-in loop
imm nums: list -> [1, 2, 3, 4, 5]
for (n in nums)
    std.outln(n * n)
end

// C-style for
for (imm j: integer -> 0; j < 10; j -> j + 1)
    std.outln(j)
end
```

### Pattern Matching

```sol
imm status: integer -> 200

match (status)
    200 -> std.outln("OK")
    404 -> std.outln("Not Found")
    500 -> std.outln("Server Error")
    _   -> std.outln("Unknown")
end
```

### Templates & Data

```sol
// Mutable template
templ Point
    x: integer
    y: integer
end

imm p: Point -> Point(10, 20)
std.outln(p.x)  // 10

// Immutable data type
data Color
    r: integer
    g: integer
    b: integer
end

imm c: Color -> Color(255, 128, 0)
std.outln(c.r)  // 255
```

### Result<T, E>

```sol
fun divide(a: integer, b: integer): Result
    if (b == 0)
        ret Err("Division by zero")
    end
    ret Ok(a / b)
end

imm result: Result -> divide(10, 2)
if (result.isOk(result))
    std.outln(result.unwrap(result))  // 5
end
```

### Lambdas

```sol
imm square: any -> ld (n: integer)
    ret n * n
end

std.outln(square(7))  // 49

// Higher-order functions
fun apply(f: any, x: integer): integer
    ret f(x)
end

std.outln(apply(square, 5))  // 25
```

## 📖 Language Reference

### Keywords

| Keyword | Description |
|---------|-------------|
| `imm` | Immediate variable declaration |
| `nonimm` | Non-immediate variable declaration |
| `fun` | Function declaration |
| `ld` | Lambda declaration |
| `ret` | Return statement |
| `if` / `elseif` / `else` / `end` | Conditional blocks |
| `while` / `for` / `break` / `continue` | Loop control |
| `match` / `when` | Pattern matching |
| `templ` | Template (mutable struct) |
| `data` | Data (immutable struct) |
| `interface` | Interface definition |
| `ext` | Extension method |
| `import` / `module` / `as` | Module system |
| `nothing` / `null` / `undefined` | Null values |
| `Ok` / `Err` / `Result` | Result type |

### Operators

| Operator | Description |
|----------|-------------|
| `->` | Assignment |
| `+` `-` `*` `/` `%` `**` | Arithmetic |
| `==` `!=` `<` `>` `<=` `>=` | Comparison |
| `&&` `\|\|` `!` | Logical |
| `&` `\|` `^` `~` `<<` `>>` | Bitwise |
| `?:` | Elvis (null-coalescing) |
| `?.` | Safe navigation |
| `!` | Force unwrap |
| `?` | Nullable type marker |

## 🧪 Running Tests

```bash
python sol.py test.sol
python sol.py test_comprehensive.sol
```

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" width="400" height="30" viewBox="0 0 400 30">
  <text x="200" y="20" text-anchor="middle" font-family="'Segoe UI',sans-serif" font-size="12" fill="#666">
    Made with ☀️ by 
    <tspan fill="#ffb000" font-weight="bold">stefand-0</tspan>
    <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" repeatCount="indefinite"/>
  </text>
</svg>

</div>