# Task 3 – Choose Variables and Name the Constants

## 1. Variables and named constants

The program uses meaningful names such as `BASE_RATE`, `STANDARD_FAT`, `STANDARD_SNF`, `FAT_STEP_VALUE` and `SNF_STEP_VALUE`.

Constants use uppercase letters with underscores between words. Variables such as `fat`, `snf`, `fat_steps` and `rate` use lowercase letters.

Named constants make the program easier to read and maintain. If the standard rate changes, I can update `BASE_RATE` in one place instead of searching for repeated values throughout the code.

## 2. Why Python constants are not enforced

Python does not have a built-in keyword that makes a variable permanently constant. Uppercase names are a programming convention that tells other programmers the value should not normally be changed.

For example, `BASE_RATE = 30.00` is intended to remain unchanged while the program runs.

## 3. Dynamic typing

Python determines the type of a value at runtime. A variable can refer to different types of values at different times.

In this program, `sample` first stores the integer `10`, so its type is `int`. Later it stores the string `"ten"`, so its type becomes `str`.

## 4. Multiple assignment and swapping

The statement `a, b = 10, 20` assigns two values at once.

The statement `a, b = b, a` swaps the values without requiring a temporary variable. The output is `20 10`.

## 5. Alternative: magic numbers

If values such as `30.00`, `0.40` and `0.30` were typed directly into calculation expressions, they would be magic numbers. If the same rate appeared in k places, a rate revision could require up to k edits. Missing one edit could make the program inconsistent.

With named constants, each value is defined once, so a revision normally requires one edit.

## 6. Alternative: dictionary rate card

A dictionary such as `RATE_CARD = {"base": 30.00, "fat": 0.40, "snf": 0.30}` groups related values under descriptive keys. This can be useful when a rate card has several related values or needs to be selected or loaded as a group.

Named constants are straightforward for a small fixed rate card. A dictionary is useful when the program needs to access rate values by key or manage multiple rate cards.

## 7. Time and space complexity

Looking up a named constant takes O(1) time. Storing a fixed number of constants uses O(1) space. A dictionary lookup is also O(1) on average, and a fixed-size dictionary uses O(1) space for this rate card.

The main benefit of named constants is maintainability and consistency; they do not meaningfully change the time complexity of this small calculation.
