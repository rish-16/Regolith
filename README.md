# 🌗 Regolith
An elegant Pseudocode-like language for beginners built in Python

## What is it?
Regolith is a dynamically-typed Pseudocode-like programming language mainly meant for beginners learning how to code; it uses a logic-first approach rather than a language-first one. It features a custom compiler written in **Python v3.6**. All Regolith files have a `.rego` extension.

This README provides an in-depth review of the language, its nuances, and syntax.

### The Name
Regolith is the blanket of loose rock deposits on the surface of space rocks, planets, and moons. It represents the flexibility and surface-level nature of the language. Crazy connection, I know. For more information about the name, check out its [Wikipedia page](https://en.wikipedia.org/wiki/Regolith).

## Why build it?
I built Regolith while learning about compilers and interpreters. It's based off Pseudocode because of its use in teaching beginners how to use logic to solve problems. I use Python for almost every project I take up, be it at work or for side-projects; I decided to use the language to make Regolith owing to its simplicity and structure.

I hope Regolith is as easy to pick up as Pseudocode and its variants. I've tried to follow common Pseudocode practices taught at schools around the world. This way, there's a bit of familiarity when someone interacts with it for the first time.

## Samples
Here's the `Fizzbuzz` program written in Regolith:

```
PROCEDURE fizzbuzz(n : INT)
    FOR (i <- 0 TO n)
        IF (i MOD 3 = 0 AND i MOD 5 = 0) THEN
            OUTPUT ("FizzBuzz")
        ELSE IF (i MOD 3 = 0) THEN
            OUTPUT ("Fizz")
        ELSE IF (i MOD 5 = 0) THEN
            OUTPUT ("Buzz")
        ELSE    
            OUTPUT (i)
        ENDIF
    ENDFOR
ENDPROCEDURE

fizzbuzz(50)
```

## What can you do?
Here's a list of everything you can do with Regolith:

- Basic expressions
- Arithmetic (add, subtract, multiply, divide, modulus, exponentiation)
- Printing

> **Note:** I'll be updating this list as and when new features are added. Check out [TODO.md](https://github.com/rish-16/Regolith/blob/master/TODO.md) for a potential timeline.

## Usage

To run the barebones version of Regolith, fire up a terminal window and clone this repo:

```bash
$ git clone https://github.com/rish-16/Regolith.git
```

Next head to the `regolith` directory and run the `main.py` file providing the Regolith filename as an argument using the `--file` or `-f` flag:
```bash
$ cd regolith
$ python main.py --file test.rego
```

## License
[MIT](https://github.com/rish-16/Regolith/blob/master/LICENSE)
