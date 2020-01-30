# checkPalindrome

This checks if the input string is a palindrome. The approach checks
if the `inputString` and its reverse are equal.

## Notes

From
this [post](https://stackoverflow.com/questions/931092/ddg#931095), I
learned how to reverse a string in Python.

Example:

```
>>> 'hello world'[::-1]
'dlrow olleh'
```

> This is extended slice syntax. It works by doing [begin:end:step] -
> by leaving begin and end off and specifying a step of -1, it
> reverses a string.

Since `begin` and `end` are not specified, the whole string is used,
and `-1` steps through the string backwards.

Update: It actually, looks like `reverse` was added to strings in
Python:

```
irb(main):047:0> "hello".reverse
=> "olleh"
```
