---
layout: post
title: Delta method and convergence of random variables
tags: statistics 
---

#### Delta method
The Delta method can be used to approximate the variance of a function of a random
variable that converges to a normal random variable. 
Assuming $$\sqrt{n} (Y_n - \theta) \rightarrow
\mathcal{N}(0,\sigma^2)$$ (distribution) with $\theta \in
\mathbb{R}$, then for a given function $g$ (with $g'(\theta) \neq 0$), we have
\\[ \sqrt{n} (g(Y_n) - g(\theta)) \rightarrow \mathcal{N}(0, \sigma^2
[g'(\theta)]^2) \text{ (distribution)} \\]


#### Convergence in distribution and convergence in probability
In the proof of the Delta method, we use the result that 
\\[ \sqrt{n} (Y_n - \theta) \rightarrow
\mathcal{N}(0,\sigma^2) \text{ (distribution)} \Rightarrow
Y_n \rightarrow \theta \text{ (probability),} \\]
 i.e., for any $\varepsilon > 0$,
$\mathbb{P}[|Y_n-\theta| \geq \varepsilon] \rightarrow 0$  as $n$ grows.
Now, let us introduce $X_n = \sqrt{n}(Y_n - \theta)$. Then
\\[ Y_n - \theta = \frac{1}{\sqrt{n}} X_n \\]
$X_n$ converges to $\mathcal{N}(0,\sigma^2)$ in distribution and $1/\sqrt{n}$
converges to zero. 
Slutsky's theorem tells us that
\\[ X_n \rightarrow X \text{ (distr) and } Y_n \rightarrow a \in \mathbb{R}
\text{ (prob)} 
\Rightarrow X_n Y_n \rightarrow aX \text{ (distr)} \\]
Therefore $Y_n - \theta \rightarrow 0$ (distr).

Moreover, 
\\[ X_n \rightarrow a \in \mathbb{R} \text{ (distr)}
\Rightarrow X_n \rightarrow a \text{ (prob)} \\]
Indeed, $\mathbb{P}[|X_n-a| \geq \varepsilon] = 1-F_n(a+\varepsilon) +
F_n(a-\varepsilon)$. Convergence to a constant in distribution means $F_n(x)$
converges to the Heaviside function $H(x-a)$. Therefore $F_n(a+\varepsilon)
\rightarrow 1$ and $F_n(a-\varepsilon) \rightarrow 0$.

Going back to our original proof, we have $Y_n - \theta \rightarrow 0$ (prob),
or equivalently $Y_n \rightarrow \theta$ (prob).
