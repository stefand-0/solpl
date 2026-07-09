# Sol

![LOGO](images/Add%20a%20heading.png)
![python](https://camo.githubusercontent.com/c180a48cde4ae1970836edbdf0025a601034aa67fcb4419457f051a481e88811/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31312d626c75653f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e)
![status](https://camo.githubusercontent.com/f9abd5e3e4958db47256814d395b7923defa3d1fb609e0ce304c50406ce2cd69/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7374617475732d6163746976652d737563636573733f7374796c653d666f722d7468652d6261646765)
![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Sol-FFB000?style=for-the-badge&logo=target)

Sol is an interpreted language with minimal functional paradigms built with Python, originally designed to handle async operations only, but has expanded to a full scripting language.

# Why did I build Sol?

I originaly needed something fast, that handled async natively, and which had very few keywords. Then came my first prototype, which only supported async functions. Sol now supports everything a programming language should need: Functions, variables, I/O, etc.

# What advantages does Sol have over other languages?

- Native async, with no external libraries

- Native networking, also with no external libraries

- With very few keywords, it is the language with the least keywords

- Easy to use standard libraries

- Simple syntax, which goes a long way for automation, web scraping, scripting, math, etc.

# Capabilities:

- Native asynchronous functions

- Native non-blocking IO

- Native networking library

- Support for structs

- Some functional paradigms, bound by the pipe operator ">>", used for channeling async, async into I/O, etc.

- A large collection of standard libraries (including standard web libraries)

# How to install Sol?

```bash
pip install solpl
```

# How to run a Sol script?

```bash
solpl FILENAME.sol
```

# Example:

This demonstrates Sol's capabilities with async:

```lua
countDown(taskName, maxCount)
    for i -> 1 to maxCount
        _out -> taskName
    end
end

main()
    _out -> 111
    countDown(777, 4) >> _async
    countDown(999, 4) >> _async
    _out -> 222
end
```

> [!IMPORTANT]
> Asynchronous functions cannot use the _return method to return a value. Please use _out instead.
> [!TIP]
> Make use of the standard libraries for extra data types, such as Booleans, HashMaps etc.
# License

This repository is licensed with Apache License 2.0, see the LICENSE file for more details

# Link to PyPi package:

https://pypi.org/project/solpl/
