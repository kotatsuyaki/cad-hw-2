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

<!-- vim: set ft=markdown.pandoc colorcolumn=100: -->
