# Regolith
🌗 An elegant Pseudocode compiler for beginners built in Python

Here's a sample `Fizzbuzz` program written in Regolith:

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