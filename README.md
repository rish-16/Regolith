# Regolith
🌗 An elegant Pseudocode-like language for beginners built in Python

## What is it?
Regolith is a dynamically-typed Pseudocode-like programming language mainly meant for beginners learning how to code; it uses a logic-first approach rather than a language-first one. It features a custom compiler written in **Python v3.6**.

This README provides an in-depth review of the language, its nuances, and syntax.

## Why build it?
I built Regolith while learning about compilers and interpreters. It's based off Pseudocode because of its use in teaching beginners how to use logic to solve problems. I use Python for almost every project I take up, be it at work or for side-projects. I decided to use the language to make Regolith owing to its simplicity and structure.

I envision Regolith to be something beginners pick up first (as they do with Pseudocode). It looks very similar to `Q-BASIC` with the uppercase character set.

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
        OUTPUT (i)
        
fizzbuzz(50)
```

## What can you do?
Here's a list of everything you can do with Regolith:

- Basic expressions
- Arithmetic (add, subtract, multiply, divide, modulus, exponentiation)
- Printing

> **Note:** I'll be updating this list as and when a new feature is added

## License
[MIT](https://github.com/rish-16/Regolith/blob/master/LICENSE)
