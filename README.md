![find direction](/find-direction.jpg)

## Part 1: Finding your way

Given a map, the programming finds the shortest path between where you are and destination. In the map, # represents your current location, @ represents destination (Luddy Hall), . represents sidewalks, and & represents other buildings, which you are not allowed to enter.

### How To Use
Run `python3 find_luddy.py map.txt`, where map.txt is the map.

### Design

| analysis <img width=250/>| initial solution (given program) <img width=800/>| final solution <img width=800/>|
| --- | --- | --- |
| set of valid states | paths that connect your current location to the destination | paths that connect your current location to the destination |
| successor function | find the sidewalks that can be reached by moving one step north / south / east / west without entering other buildings | find the sidewalks that can be reached by moving one step north / south / east / west without entering other buildings and revisiting the sidewalks that have been visited. A star search is used (please see below). |
| cost function | sum of the length of the path | sum of the length of the path |
| goal state | you arrived at the destination (Luddy Hall) | you arrived at the destination (Luddy Hall) |
| initial state | your current location | your current location |


In order to find the way more efficiently, A star search is used. 
- g(s) = cost of best path found so far to s <br>
Shortest distance between origin and current location
- h(s) = admissible heuristic function <br> 
Euclidean distance between current location and destination

## Part 2: Hide-and-seek
Given a map, the programming arranges your friends such that no two of your friends can see one another but your friend is allowed to see you. Symbols are the same as in Part 1. 

### How To Use
Run `python3 hide.py map.txt K`, where map.txt is the map, K is number of friends you have to arrange to the map.

### Design

| analysis <img width=250/>| initial solution (given program) <img width=800/>| final solution <img width=800/>|
| --- | --- | --- |
| set of valid states | permutation of K locations of sidewalks | permutation of K locations of sidewalks while K friends don't see each other |
| successor function | all the sidewalks | all the sidewalks except those can be seen by your friends who have been arranged in the map. Heuristic search is used (please see below). |
| cost function | number of search steps | number of search steps |
| goal state | K friends have been arranged in the map (there might be several possible arrangements) | K friends have been arranged in the map (there might be several possible arrangements) |
| initial state | the given map which has no friend in the map | the given map which has no friend in the map |


Heuristic search is used to increase efficiency. 
- h(s) = heuristic function <br> 
  - number of surrounding available locations
  - K - number of friends that have been arranged in the map
