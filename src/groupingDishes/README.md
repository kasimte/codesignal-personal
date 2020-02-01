# Notes

I was tripped up because I wasn't sure how to get the keys of a hash
into an array in Python.

It turns out it is this:

> list(d)
> Return a list of all the keys used in the dictionary d.

```
>>> hash = { 1 : 2 }
>>> list(hash)
[1]
```

Then I was tripped up again because I wasn't sure how to sort an
array. It turns out you can call `array.sort()`, which sorts the array
in place.

I guess I'm used to Ruby syntax!
