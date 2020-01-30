# rotateImage

https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB

Rotate an image, represented as a square matrix, clockwise.

Input:

```
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
```

Output:

```
rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
```

## Notes

* I used a naive approach, where an entirely new output array is
  created and then elements are added to it, but based on skimming
  online there are obviously more performant approaches.
  
* I am still getting used to Python syntax. To insert something into
  an existing array, the format is `array.insert(index, element)`.
