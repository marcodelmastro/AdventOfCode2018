# Advent Of Code 2018

I did not participate to Advent Of Code in December 2018 (I only discovered the challenge in 2019) but the puzzles are fun and helping me to improve, so I plan to do them when I have time.

https://adventofcode.com/2018

## ChangeLog and Notes

* **Day 1**: January 2020
* **Day 2**: January 2020
* **Day 3**: January 2020

* **Day 4**: 2021-03-05
    * Time interval manipulation. Solved using `datetime`, `defaultdict` and `Counter` to get most common minute.

* **Day 5**: 2021-02-07
    * String slicing and comparing. Probably faster with RegEx is I only knew how to properly use them

* **Day 6**: 2021-02-07
    * Voronoi tessellation with Manhattan distance!

* **Day 7**:
    * Part 1: 2021-02-14. Directed graph analysis using `networkx` library, plus my own implementation of topological sorting.
    * Part 2: 2021-03-08. Using `networkx` `in_degree()` method to flag nodes with no incoming connection, and the graph itself a s queue of nodes to be completed by removing completed nodes from graph with `remove_nodes_from`. It's a somewhat destructive solution, I might have used a `deque()` or similar to implement the queue, but then I should have also kept track independently of something similar to `in_degree` and updated it with each parent node completion.

* **Day 8**:
    * Part 1: 2021-03-11. Recursive call to same function. Popping value from list before and after recursive calls, passing remaining value list and current sum. I don't know why this problem scared be and I only found the gut to attack it after having solved many later days. Part 1 one was ultimately relatively simple if embracing recursion power.
    * Part 2: 2021-03-11. Slight modification of Part 1, more recursion galore!

* **Day 9**: 2021-02-16
    * Double-sided linked list, implemented as a dictionary of size-2 list (left and right neighbors of key marble)
    * Using `defaultdict` to keep track of played marbles for faster access

* **Day 10**: 2021-02-16
    * Fun 2D particle evolution that eventually forms a message. 
    * I decided to use panel size as condition to stop evolution (shrinking and the growing again), but I considered possible others (e.g. several columns in panel to be fully filled, corresponding to letter vertical traits). The advantage of the size condition is that I don't need to fill the grid to visualize the message at each step, only to look for minimum and maximum coordinates.

* **Day 11**: 2021-03-04
    * Summed-area table to speed up Part 2

* **Day 12**: 2021-03-04
    * 1-D Conway game of life. Part 2 requires finding pattern repetition and compute solution, since evolution simulation is impossible (too long)

* **Day 13**: 2021-03-07
    * Part 1: Cart simulation. It took me some time to figure out how to deal with angles and turns, ultimately using complex numbers to represent position and directions.
    * Part 2: The initial logic to find collisions was not adapted to solve Part 2, since carts needed to be removed when collision happened, and not at the end of the tick. Changed loop on carts on loop on cart index, and instead of removing carts I declare them dead with negative coordinate (to be checked). Final code is very patchy but works fine. Next time I'll implement a class to store all cart info (including a flag for a crashed cart)!

* **Day 14**: 2021-03-05
    * Weird sequence generation. For Part 2 it took me some time to understand why my ending condition for the brute force loop was not working for the input, while it did ok for the examples. It obviously had to do with the input format, and how the ending digit can be generated.
    
* **Day 15**: 
    * Part 1: 2021-03-14. This took several sessions (and days!) to get it right. The most complicated part was to get the movements and distance measuring right: after many attempts, BFS (saving only path lenght) was the winning option!
    * Part 2: 2021-03-14. Once Part 1 was done, modifications for Part 2 were simple!

* **Day 16**:
    * Part 1: 2021-03-05. Opcodes! Implementation and then test of what index could represent one or more opcode values
    * Part 2: 2021-03-06. Now I need to solve the opcode/index correspondence matrix, then implement the virtual machine and run the program... :-)

* **Day 17**: 2021-03-30. 
    * I as initially rather scared by this puzzle, but I ended up enjying quite a lot. A few specific cases in the full input reqwuired some debuggin of the water flow and filling logic, but I managed in a reasonable time to undestand how fix them. Given how I decided to store the water information (separating flowing and still water) Part 2 was trivial!

* **Day 18**: 2021-03-06
   * Another Conway's Game of Life clone, this time with 3 states on a 2D grid. Period/recurrence seeking needed to solve Part 2.

* **Day 19**:
   * Part 1: 2021-03-07. Opcodes from Day 16 + dedicated register to select instructions (effectively implementing instruction jumps).
   * Part 2: 2021-03-18. An "infinite loop" to be understood deconstructing the program (both the output and the instructions themselves: what is the program trying to do?) and to be re-implemented in a more efficient way... This is getting old! 

* **Day 20**: 2021-03-16
   * Grid navigation with branching, inputs is similar ot a DFS solution of a maze. Instead of mapping the maze itself, Part 1 is solved by keeping track of minimum distance from origin (where minimum is chosen when two or more possible paths pass for that location). Hoping this won't make solution of Part 2 impossible (e.g. if maze mapping is needed)
   * Part 2 solution took 4 lines, no true mapping needed, dictionary of minimal distances was more then enough!
   
* **Day 21**: 2021-03-19
   * Another pseudo-assembly code. Solution of both Part 1 and Part 2 require understanding what the program is doing, then reimplementing the same calculation in an efficient way. Part 2 adds the need or finding a repetition in the input values halting the program.

* **Day 22**:
   * Part 1: 2021-03-09. Deep recursion to be solved with memoization
   * Part 2: 2021-03-10. Implemented a BFS search with a `PriorityQueue` to follow paths leading to shorter time (is this a Dijkstra's algorithm?). Struggled to get the solution to work on the full input, the problem was the way I was keeping track of the `visited` cells, that was initially only considering the position/equipment pair but not the traveled time. Got an hint about this on reddit (thanks AOC community!). Also implement use of better heuristic in `PriorityQueue` also accounting for position distance and not only traveled time: convergence happens in about half the time!

* **Day 23**:
   * Part 1: 2021-03-09. Quick solution using `numpy` arrays
   * Part 2: **TODO**

* **Day 24**: 2021-03-17
   * Another simulation a bit like Day 15, but luckily without movements! 
   * Part 2 can be solved with brute force search, but one must implement a stopping mechanism to deal with stalling matches. 

* **Day 25**: 2021-03-09
   * Patchy list manipulation, using `numpy` to compute Manhattan distance. Slow and inefficient, but it works.
   
