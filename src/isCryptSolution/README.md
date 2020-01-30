# isCryptSolution

[On CodeSignal](https://app.codesignal.com/interview-practice/task/yM4uWYeQTHzYewW9H)

A cryptarithm is a mathematical puzzle for which the goal is to find
the correspondence between letters and digits, such that the given
arithmetic equation consisting of letters holds true when the letters
are converted to digits.

Write a function, `isCryptSolution(list, solution)` that returns a
boolean determining whether the solution is correct or not.

## Notes

* Convert a List into a String in Python:

```
list1 = ['1', '2', '3']
str1 = ''.join(list1)
```

https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

* There are some gotchas here, where the first number can't be a 0, so
  each string has to be checked for that.
  
* While strings with a first digit 0 may be invalid, when it is just a
  single digit 0, that is okay.
  
* The Python 'join' command to convert an array into a string tripped
  me up a bit at first. The syntax is `join_string.join(array)`, not
  `array.join(join_string)` like it is in Ruby.
