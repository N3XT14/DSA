# Math for Data Structures and Algorithms

Revise the basics of the maths needed for working alongside with DSA.

---
# Logarithms


<!-- $${\color{red}\sum\limits_{\color{lightblue}i=0}^{\color{orange}n} {\color{pink}i}} = \frac{\color{pink}n!}{\color{lightblue}k!(n-k)!}$$ -->

$$
y = bx \\
log{_b}{y}=log{_b}{bx}\\
log{_b}{y}={x}
$$

$$
log{_a}{(xy)}  = log{_a}{x} + log{_a}{y}\\
log{_a}{(x/y)} = log{_a}{x} - log{_a}{y}\\
log{_a}{(x^y)} = ylog{_a}{x}\\
log{_a}{(x)} = \frac{log{_b}{(x)}}{log{_b}{(a)}}\\
x^{log{_b}{(y)}} = y^{log{_b}{(x)}}\\
lg(x) = log{_2}{x}\\
ln(x) = log{_e}{x}\\
log^k(n) = (log(n))^k\\
lglg(n) = lg(lg(n))
$$

---

# Floors & Ceilings

• Floors: 

    [𝑥] is the largest integer not greater than x.
    For 𝑥 ∈ ℝ, 𝑥 − 1 < [𝑥] ≤ 𝑥.

• Ceilings:

    [𝑥] is the smallest integer not less than x.
    For 𝑥 ∈ ℝ, 𝑥 ≤ [𝑥] < 𝑥 + 1.

• Properties:

    𝑥 − 1 < [𝑥] ≤ 𝑥 ≤ [𝑥] ≤ 𝑥 + 1.
    ∀n ∈ Z, [n/2] + [n\2] = n.
    ∀a,b ∈ Z+, [a/b] ≤ (a + (b-1))/b.

• Example:

|x|Floor|Ceiling|
|---|---|---|
|-1.1|-2|-1|
|0|0|0|
|1.01|1|2|
|2.9|2|3|
|3|3|3|

---

# Arithmetic Sequences & Series

`The Arithmetic Sequence is a sequence of numbers such that the difference between successive terms in the sequence is constant.`

    • The first n values of the arithmetic sequence are:
    • 𝑎, 𝑎 + 𝑑, 𝑎 + 2𝑑, 𝑎 + 3𝑑, ... , 𝑎 + (𝑛 − 1)𝑑.
    • 𝑎 – initial value
    • 𝑑 – difference
    • Example: 1, 4, 7, 10, 13, 16, 19, ... (difference of 3).

> The Arithmetic Series is the sum of the terms in the Arithmetic Sequence.

$$
\displaystyle\sum_{i=0}^{n-1} (a+id)=\frac{(2a + (n-1)d)n}{2}
$$

> Let $𝑎{_1} = 𝑎$  𝑎𝑛d $a{_n} = 𝑎 + (𝑛 − 1)𝑑$

$$
\displaystyle\sum_{i=0}^{n-1} (a+id)=\frac{(a{_1} + a{_n})n}{2}
$$

---

# Geometric Sequences & Series

`The Geometric Sequence is a sequence of numbers where each successive term is found by multiplying the previous term by a fixed, non-zero, common ratio.`

    • The first n values of the geometric sequence are:
    • 𝑎, 𝑎𝑟, 𝑎𝑟2, 𝑎𝑟3, ... , 𝑎𝑟𝑛−1
    • 𝑎 – initial value
    • 𝑟 ≠ 0 – fixed multiplier
    • Example: 1, 2, 4, 8, 16, 32, ... (common ratio of 2).

> The Geometric Series is the sum of the terms in the Geometric Sequence.

$$
\displaystyle\sum_{i=0}^{n-1} (ar^i)=\frac{a(1 - r^n)}{1-r}
$$

> When −1 < 𝑟 < 1, the sum of the in infinite geometric progression converges to:

$$
\displaystyle\sum_{i=0}^{∞} (ar^i)=\frac{a}{1-r} 
$$

---

# Harmonic Series

    • The first n values are: 1, 1 2 , 1 3 , ... , 1 𝑛
    • The sum of these values can be represented with:
$$
\displaystyle\\H{_n}=\sum_{i=0}^{n}(\frac{1}{i})
$$
    • The harmonic series does not converge, but satisfies the following property:
    ln(𝑛 + 1) < 𝐻𝑛 ≤ 1 + ln(𝑛)

---

# Limits

`A limit is a way of determining trends for values that may or may not exist`
