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

The definition of a limit follows such that if $0< |x-c| < \delta$ then $|f(x) - 1| < \varepsilon$

$$
\lim\limits_{x \to c}f(x) = l\\
$$

### Rules:

$$
\lim\limits_{x \to c}b = b\\
\lim\limits_{x \to c}x = c\\
\lim\limits_{x \to c}x^n = c^n
$$

Constants can be pulled out of limits when a ∈ ℝ and $\lim\limits_{x \to c}f(x) = l$

$$
\lim\limits_{x \to c}(a)(f(x)) = (a)(l)
$$  

The limit of a sum is the sum of the limits

$$
\lim\limits_{x \to c}(f(x) + g(x)) = limits_{x \to c}f(x) + limits_{x \to c}g(x)
$$  

The limit of a product is the product of the limits

$$
\lim\limits_{x \to c}(f(x) \times g(x)) = limits_{x \to c}f(x) \times limits_{x \to c}g(x)
$$ 

The limit of a quotient is the quotient of the limits, when divisor is not 0 such that $\lim\limits_{x \to c}g(x) ≠ 0$.

$$
\lim\limits_{x \to c}(f(x) \div g(x)) = limits_{x \to c}f(x) \div limits_{x \to c}g(x)
$$ 

---

# Derivatives

`Derivatives are a measure of how a function changes with respect to its input.`

    For a real-valued function of a single real variable, the derivative at a point is the slope of the tangent line to the graph of the function at that point.

### Rules:

• When $p(x) = x^n$ and  n ≠ 0, $p^`(x) =  (n)(x^{n-1})$

• ${f(x)g(x)}` = ((f(x))(g`(x))) + ((f`(x))(g(x)))$

• $(\frac{f}{g})$\` $(x)$ = $\frac{((g(x))(f\`(x)) - (g\`(x))(f(x)))}{(g(x)^2)}$

• $(\frac{d}{dx})(f(g(x)))$ = $f\`(g(x)g\`(x))$

• $(\frac{d}{dx})(ln(x))$ = $\frac{1}{x}$

• $(\frac{d}{dx})(e^{x})$ = $e^{x}$

• $(\frac{d}{dx})(e^{f(x)})$ = $(e^{f(x)})(f\`(x))$

• $(\frac{d}{dx})p^{x}$ = $p^{x}(ln(p))$

• $(\frac{d}{dx})(p^{g(x)})$ = $(p^{g(x)})(g\`(x))(ln(p))$

• $(\frac{d}{dx})(\log{_p}{(g(x))})$ = $\frac{g\`(x)}{(g(x))ln(p)}$

---

# L'Hopital's Rule

`Assume 𝑓(𝑥) and 𝑔 𝑥 are both differentiable, with derivatives 𝑓′(𝑥) and 𝑔′(𝑥) respectively. Further, assume that 𝑐 ∈ ℝ.`

$$
\lim\limits_{x \to c}\frac{f(x)}{g(x)} = \frac{0}{0}\ or \ \lim\limits_{x \to c}\frac{f(x)}{g(x)} = \frac{±\infty}{±\infty} \ and \ \lim\limits_{x \to c}\frac{f\`(x)}{g\`(x)} \ exists, \\
then \ \lim\limits_{x \to c}\frac{f(x)}{g(x)} = \lim\limits_{x \to c}\frac{f\`(x)}{g\`(x)}
$$ 

---