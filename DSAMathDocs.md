# Math for Data Structures and

Revise the basics of the maths needed for working alongside with DSA.

---
# Logarithms

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

`The Arithmetic Sequence is a sequence of numbers
such that the difference between successive terms
in the sequence is constant.`

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