# Report

## Choices of data structures

I used python `heapq` for the frontier data structure, which I call `to_visit`. This essentially turns a `list` into a `min heap` ordered by the $totalCost + heuristicCost$  of each node. This makes sense because we want to explore each node in order of how likely they are to take us to the solution according to our heuristic.

I used a simple `set` as the data structure for the `explored` set. Because order does not matter in this set, and we only use it to check if the node has been visited already, the constant time lookup time of the set made perfect sense.

## Effectiveness of heuristic

#### Maze 1: *Death Trail*

##### Optimal: 15 Steps

```
["XXXXXXXXXXXX",
"XG.......XGX",
"X...XXX..X.X",
"X...XGX..X.X",
"X...XXX..X.X",
"X.......XX.X",
"X..........X",
"X......XXXXX",
"X.........*X",
"XXXXXXXXXXXX"]
```

##### Results

| Breadth-first Tree Search | A* Graph Search |
| ------------------------- | --------------- |
| 1026155                   | 128             |



#### Maze 2: *Space Invaders*

##### Optimal: 8 Steps

```
["XXXXXXXXXXXXX",
"X..G.G.G.G..X",
"X.G.G.G.G.G.X",
"X..G.G.G.G..X",
"X...........X",
"X...........X",
"X...........X",
"X.XX.XXX.XX.X",
"X.....*.....X",
"XXXXXXXXXXXXX"]
```

##### Results

| Breadth-first Tree Search | A* Graph Search |
| ------------------------- | --------------- |
| 1387                      | 63              |



#### Maze 3: *The Maze Runner*

##### Optimal: 22 Steps

```
["XXXXXXXXXXXXXXXXX",
"X...............X",
"X.XXXXX...XXXXX.X",
"X.X...........X.X",
"X.X....*......X.X",
"X.X...........X.X",
"X.XXXXXXXXXXXXX.X",
"X.......G.......X",
"XXXXXXXXXXXXXXXXX"]
```

##### Results

| Breadth-first Tree Search | A* Graph Search |
| ------------------------- | --------------- |
|                           | 183             |

