### Initially, we only have the exact coordinates of the start location. 
### Then all other points are given to us as a chain from this point. 

# Now your task is to find the exact coordinates of each location.

## Input
### The first line contains the start coordinates. The values ​​of x and y, which are integers, are given at the beginning.

### In the following lines, a new location is introduced in each line. First, the name of the new location is given, then the phrase from, and then the name of the location to which x and y are given. In these lines, the values ​​of x and y are always given with a + or - sign.

### For example, in the first example, hospital, its x value is one unit less than the x belonging to start, and its y value is two units more than the y belonging to start.

## Output
### For each location in the input except start, the exact coordinates of the same location should be printed in the output, observing the order in which they appeared in the input.

# Example:
---
## Sample Input 1
```
start x=1 y=1
hospital from start x=-1 y=+2
```
‍‍‍‍‍---

## Sample Output 1
```
hospital x=0 y=3
```

## Sample Input 2
```
start x=1 y=1
office from hospital x=+4 y=-1
hospital from start x=-1 y=+2
```
‍‍‍‍‍‍‍‍‍
## Sample Output 2
```
office x=4 y=2
hospital x=0 y=3
```

## More Tips
The order of display of locations in the output must be exactly the same as the order of the input (except start, which does not need to be displayed).
A solution is guaranteed to exist.
Each location name is guaranteed to be unique and consist of lowercase English letters and numbers, and a new location is described after the first line.
The total number of locations is guaranteed to be as follows.
