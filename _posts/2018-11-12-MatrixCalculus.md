---
layout: post
title: Conventions for Matrix Calculus
tags: optimization calculus
---


## Notes 

In optimization, you need to take derivatives. To do that in $\mathbb{R}^n$, you
need matrix calculus. The objective of this note is to summarize the important
definitions and conventions, explain them whenever possible, and show a few
examples.


#### Frechet and Gateaux derivatives

Let's define a function $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$.  That
function is 
[Frechet differentiable](https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative) 
at $x$ if
there exists a bounded (necessarily the case for an operator between finite dimensional
spaces) linear operator  
$Df(x): \mathbb{R}^n \rightarrow \mathbb{R}^m$ 
such that
\\[ \frac{\| f(x+h) - f(x) - Df(x)h \|}{\| h \|} \rightarrow 0 \\] 
as $\|h\| \rightarrow 0$.

A somehow weaker definition of differentiability is the [Gateaux
differentiability](https://en.wikipedia.org/wiki/G%C3%A2teaux_derivative).  A
function $f$ is Gateaux differentiable at $x$ if, for any $v
\in \mathbb{R}^n$ the following limit exists
\\[ lim_{\varepsilon \rightarrow 0} \frac{f(x + \varepsilon v) - f(x)} \varepsilon . \\]
If that limit exists, we can calculate it as
\\[ lim_{\varepsilon \rightarrow 0} \frac{f(x + \varepsilon v) -
f(x)}\varepsilon = \frac{d}{d\varepsilon} f(x + \varepsilon v)
|_{\varepsilon=0} . \\]

If $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ 
is Frechet differentiable, it is necessarily Gateaux differentiable, and
$$ \frac{d}{d \varepsilon} f(x + \varepsilon v) |_{\varepsilon=0} = Df(x) v
$$.

#### Gradient of a functional

Let's call $H = \mathbb{R}^n$, which is a Hilbert space with inner product
$\langle \cdotp, \cdotp \rangle$.  For a functional $f: \mathbb{R}^n \rightarrow
\mathbb{R}$, the derivative $Df(x)$ is, by definition, an element of the dual
space $H^*$.
Applying [Riesz representation
theorem](https://en.wikipedia.org/wiki/Riesz_representation_theorem), we know
there is an element $g_x \in H$ such that for any $v \in H$,
$$ DF(x) v = \langle g_x, v \rangle $$. That element $g_x$ is the gradient of
the functional $f$. This clearly defines the gradient of a functional, 
without having to agree on notations or conventions. 

#### General case

What can we do for a function $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$?
First, we can't apply Riesz representation theorem. Also, it is not clear how we
optimize that function $f$. We'd need to define a [total
order](https://en.wikipedia.org/wiki/Total_order#Orders_on_the_Cartesian_product_of_totally_ordered_sets)
on $\mathbb{R}^m$ that would coincide with the objective of optimization.  For
that reason, I see the definition of a gradient in that case as more of a
convention.  There are really two conventions, which are a transpose of each
other (see [layout
conventions](https://en.wikipedia.org/wiki/Matrix_calculus#Layout_conventions)),
and I adopt the convention used in Nocedal & Wright's Numerical Optimization
textbook (section A.2 Derivatives).
Linear maps between two finite-dimensional spaces can
all be described by the action of a matrix.
Nocedal & Wright call the Jacobian the matrix 
$J(x) \in \mathbb{R}^{m \times n}$ 
that verifies, for any $v \in \mathbb{R}^n$, $Df(x)v = J(x) \cdotp v$.
The gradient is defined to be the transpose,

$$ \begin{align} 
J(x) & = \left[ \frac{\partial f_i}{\partial x_j} \right]_{ij} 
\in \mathbb{R}^{m \times n} \\
\nabla f(x) & = \left[ \frac{\partial f_j}{\partial x_i} \right]_{ij} = J(x)^T
= \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \dots & \frac{\partial f_m}{\partial x_1} \\
\vdots & & \vdots \\
\frac{\partial f_1}{\partial x_n} & \dots & \frac{\partial f_m}{\partial x_n} 
\end{bmatrix}
\in \mathbb{R}^{n \times m} 
\end{align} $$


One thing to be careful about with that notation, 
the chain-rule, as we know it, applies to the Jacobian, i.e., if $h(x) =
f(g(x))$, then

$$ J_h(x) = J_f(g(x)) \cdotp J_g(x) $$

and therefore in terms of the gradient, we get the transpose,

$$ \nabla h(x) = \nabla g(x) \cdotp \nabla f(g(x)) $$

For instance, let's assume $f: \mathbb{R}^m \rightarrow \mathbb{R}$ and $g: \mathbb{R}^n
\rightarrow \mathbb{R}^m$. Then, with $y_k = (g(x))_k$, for any $i=1,\dots,n$,

$$ \frac{\partial h}{\partial x_i} = \sum_{k=1}^m \frac{\partial f}{\partial
y_k} \frac{\partial y_k}{\partial x_i} 
= \left [\frac{\partial (g(x))_i}{\partial x_i} \right]_i^T \cdotp \nabla f(g(x))
$$

Then putting all indices $i$ together (in rows), we get the expression above for the
gradient.


#### Derivative with respect to a matrix

In that case also, this is just a convenient notation. For a function $f :
\mathbb{R}^{m \times n} \rightarrow \mathbb{R}$, we define
 
$$ \frac{\partial f(M)}{\partial M} = \left[
\frac{\partial f(M)}{\partial m_{ij}} \right]_{ij} $$


## Examples

#### If $f(x) = Ax + b$

We then have $f : \mathbb{R}^n \rightarrow \mathbb{R}^m$.
We can apply the definition of the Gateaux derivative,

$$f(x + \varepsilon v) = f(x) + \varepsilon A v $$

We can conlude directly that

$$ \nabla f(x) = A^T $$

#### If $f(x) = \frac12 x^T Q x $

We then have $f : \mathbb{R}^n \rightarrow \mathbb{R}$.
We can apply the definition of the Gateaux derivative,

$$f(x + \varepsilon v) = f(x) + \frac12 \varepsilon 
\left( x^T Q v + v^T Q x \right) + 
\frac12 \varepsilon^2 v^T Q v $$

We conlude that

$$ \nabla f(x) = \frac12 ( Q + Q^T) x $$

In the special case that $Q=Q^T$ (symmetric), we have

$$ \nabla f(x) =  Q x $$


#### If $f(x) = \frac12 \| Ax+b\|^2$

We then have $f : \mathbb{R}^n \rightarrow \mathbb{R}$.
Following the same approach, we get

$$f(x + \varepsilon v) = f(x) + 
\frac12 \varepsilon \left( (Ax+b)^T A v + (Av)^T(Ax+b) \right) + 
\frac12 \varepsilon^2 \|Av\|^2 $$

We can conlude that

$$ \nabla f(x) = A^T \cdotp (Ax+b) $$

Alternatively, we can use the chain-rule with $g(y) = \frac12 \| y \|^2$ and
$f(x) = g(Ax + b)$. 
Since $\nabla (Ax+b) = A^T$ and $\nabla g(y) = y$, we have

$$ \nabla f(x) = A^T \cdotp (Ax+b) $$


#### If $f(A) = Ax+b$

In that case, I'm not sure it helps to talk about a gradient. However we can
still calculate the derivative (e.g., using the formula for the Gateaux
derivative), and we get

$$ Df(A) M = M \cdotp x $$


#### If $f(A) = \frac12 \| Ax+b\|^2$

Here we have $f: \mathbb{R}^{m \times n} \rightarrow \mathbb{R}$.
It's tempting to use the chain-rule, but I couldn't agree with myself on a
logical convention. And I think sadly this is the main conclusion of that small
post: it's safer to always rely on the entry-wise derivative. In this case,
with $y = Ax + b \in \mathbb{R}^m$, we have

$$ \begin{align*}
\frac{\partial f(A)}{\partial a_{ij}} & = 
\sum_k \frac{\partial g(Ax + b)}{\partial y_k} \frac{\partial y_k}{\partial
a_{ij}} \\
& = \left[ \frac{\partial y_1}{\partial a_{ij}}, \dots, \frac{\partial y_m}{\partial
a_{ij}} \right] \cdotp (Ax + b)
\end{align*} $$

Let's look at the partial derivatives for $y$, using the notation $\delta_{ik} =
1$ if $i=k$ and $0$ otherwise,

$$ \frac{\partial y_k}{\partial a_{ij}} = x_j \delta_{ik} $$

Such that

$$ \frac{\partial f(A)}{\partial a_{ij}}  = (Ax+b)_i x_j $$

And putting all indices back together,

$$ \frac{\partial f(A)}{\partial A}  = (Ax+b) \cdotp x^T $$

