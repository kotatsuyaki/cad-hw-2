# 1. Calculate slack for each block
The tables below tabluates the process of finding slack for each of block.
Slack is given in the rows marked as $S(X)$.

||A|B|C|D|F|G|H|I|
|---|---|---|---|---|---|---|---|---|
|$D(X)$|0|0|0|0|1|4|2|1|
|$A(Y)$ of predecessors|0|0|0|0|0|0;0|1|4|
|$R(X)-D(X)$ of successors|1;9|-1;12|-1;11|1;12|2;5|3;7|4;7|4;5|
|$A(X)$|0|0|0|0|1|4|3|5|
|$R(X)$|1|-1|-1|1|2|3|4|4|
|$R(X)-D(X)$|1|-1|-1|1|1|-1|2|3|
|$S(X)$|1|-1|-1|1|1|-1|1|-1|

||J|K|L|M|N|O|P|
|---|---|---|---|---|---|---|---|
|$D(X)$|5|2|3|2|3|5|4|
|$A(Y)$ of predecessors|3;5|1;5|4;3|0;10|0;0|7;7|0;12|
|$R(X)-D(X)$ of successors|9|10|10|11|15|15|15|
|$A(X)$|10|7|7|12|3|12|16|
|$R(X)$|9|10|10|11|15|15|15|
|$R(X)-D(X)$|4|5|7|9|12|10|11|
|$S(X)$|-1|3|3|-1|12|3|-1|

# 2. Find longest and shortest delay paths and their delays

First, perform a topological sort on the graph in increasing order.

$$(S), A, F, B, G, K, C, H, L, D, I, N, J, M, E$$

We find the longest and shortest path delays ($A(X)$'s and $a(X)$'s) in the sorted order.
The node names after the path delays inside parentheses are the chosen predecessor.

|   | $A(X)$                  | $a(X)$               |
|---|-------------------------|----------------------|
|$A$|$\max(0) = 0$ (S)        |$\min(0) = 0$ (S)     |
|$F$|$\max(0) = 0$ (S)        |$\min(0) = 0$ (S)     |
|$B$|$\max(2,3) = 3$ (F)      |$\min(2,3) = 2$ (A)   |
|$G$|$\max(3) = 3$ (F)        |$\min(3) = 3$ (F)     |
|$K$|$\max(2,0) = 2$ (A)      |$\min(2,0) = 0$ (S)   |
|$C$|$\max(4) = 4$ (B)        |$\min(3) = 3$ (B)     |
|$H$|$\max(4,4) = 4$ (B)      |$\min(3,4) = 3$ (B)   |
|$L$|$\max(4,3) = 4$ (G)      |$\min(4,1) = 1$ (K)   |
|$D$|$\max(8) = 8$ (C)        |$\min(7) = 7$ (C)     |
|$I$|$\max(8,3) = 8$ (H)      |$\min(7,1) = 1$ (K)   |
|$N$|$\max(10) = 10$ (D)      |$\min(9) = 9$ (D)     |
|$J$|$\max(8,11) = 11$ (I)    |$\min(7,4) = 4$ (I)   |
|$M$|$\max(10,6) = 10$ (D)    |$\min(9,3) = 3$ (L)   |
|$E$|$\max(13,14,15) = 15$ (M)|$\min(12,7,8) = 7$ (J)|

Finally we identify the longest and shortest paths.

- Longest path: $S\to F\to B\to C\to D\to M\to E$, path delay $15$.
- Shortest path: $S\to K\to I\to J\to E$, path delay $7$.

# 3. Normalized Polish expression for the floorplan

Construct the normalized slicing tree.
Here the tree is presented in an S-expression-like format.
Left children nodes come before right children nodes.

```txt
(V (1)
   (H (H (V (5)
            (H (H
               (8)
               (7))
            (6)))
         (4))
      (V (2)
         (3))))
```

Convert the slicing tree to Polish expression.

```txt
1587H6HV4H23VHV
```

# 4 (a). Area optimization by hard block rotation

The calculation is shown in the figure below.
Sizes are written as pairs of $(\text{width}, \text{height})$.
Sizes for the optimized area case are shown in **bold font**.
Internal nodes are numbered in an arbitrary order.

![The optimization process](./resources/4a-tree.pdf)

The area of the optimized floorplan is $6\times 7 = 42$.
The floorplan is illustrated below.

![The floorplan](./resources/4a-floorplan.pdf)

# 4 (b). Draw a slicing floorplan that has smaller area than (a)

The area of the following floorplan is $6\times 6 = 36 < 42$.

![The floorplan](./resources/4b-floorplan.pdf)


<!-- vim: set ft=markdown.pandoc colorcolumn=100: -->
