# Advent Of Code 2018

I did not participate to Advent Of Code in December 2018 (I only discovered the challenge in 2019) but the puzzles are fun and helping me to improve, so I plan to do them when I have time.

https://adventofcode.com/2018

## ChangeLog

* Day 1: January 2020
* Day 2: January 2020
* Day 3: January 2020
* Day 4: 
* Day 5: 2021-02-07
    * String slicing and comparing. Probably faster with RegEx is I only knew how to properly use them
* Day 6: 2021-02-07
    * Voronoi tassellation with Manhattan distance!
* Day 7:
    * Part 1: 2021-02-14. Directed graph analysis using `networkx` library, plus my own implementation of topological sorting.
* Day 8:
* Day 9: 2021-02-16
    * Double-sided linked list, implemented as a dictionary of size-2 list (left and right neighbours of key marble)
    * Using `defaultdict` to keep track of played marbles for faster access
* Day 10: 2021-02-16
    * Fun 2D particle evolution that eventually forms a message. 
    * I decied to use panel size as condition to stop evolution (shrinking and the growing again), but I considered possible others (e.g. several columns in panel to be fully filled, corresponding to letter vertical traits). The advantage of the size condition is that I don't need to fill the grid to visualize the message at each step, only to look for minimum and maximum coordinates.
* Day 11: 2021-03-04
    * Summed-area table to speed up Part 2
* Day 12: 2021-03-04
    * 1-D Conway game of lifes. Part 2 requires finding pattern repetition and compute solution, since evolution simulation is impossible (too long)
* Day 13:
* Day 14:
  * Part 1: 2021-03-05. Weird sequence generation
