# collatz-divisibility-test

## Overview

This is a divisibility test based on the generalized Collatz $3n + q$ dynamics.

It utilizes two frameworks:

![functions](assets/functions.png)

The function $f_{1}$ is used when $q \equiv 1 \pmod{6}$

And the function $f_{2}$ is used when $q \equiv 5 \pmod{6}$

### Pros

- It uses only addition, shifting, and bitwise AND for checking.
- If $a$ is divisible by $b$, it can provide the answer very quickly as a result of that.

### Cons

- If $a$ is not divisible by $b$, and we use an implementation that relies solely on the operators mentioned above, this test can get stuck in an infinite loop. However, adopting an approach that employs strategies, such as hash tables or bit arrays, to track trajectories efficiently can still be fast but may consume more memory.
