---
layout: post
title: Gaussian measures in high dimension
tags: gaussian dimensionality statistics chi distributions
---

High dimensional spaces can be counter-intuitive. [For instance](https://www.johndcook.com/blog/2011/09/01/multivariate-normal-shell/), 
most of the mass
of a sphere in high dimension is concentrated in the outside region of the sphere.
To see this, remember that the volume of a
[n-sphere](https://en.wikipedia.org/wiki/N-sphere#Volume_and_surface_area) is
given by
\\[ V_n(r) = \frac{\pi^{n/2}}{\Gamma(n/2+1)} r^n. \\]
With this formula, we find that the percentage of mass of a unit n-sphere found
in-between two spheres of radii 0.99 and 1.00 (i.e., a shell of thickness 0.01)
is equal to $10\%$ in $\mathcal{R}^{10}$, $39\%$ in $\mathcal{R}^{50}$, and $63\%$
in $\mathcal{R}^{100}$.

This example also helps explain why samples from a [multivariate Gaussian](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)
in $\mathcal{R}^n$ tend to accumulate on a sphere of radius $\sqrt{n}$ when $n$
grows large.
The pdf of a Gaussian decreases exponentially fast as distance from the mean
grows, but the mass of the space becomes more and more concentrate. The result
is that the mode of a multivariate standard normal is at a distance
$\sqrt{n-1}$.

For a multivariate standard normal ($\mu=0$, $\Sigma=I$) in $\mathcal{R}^n$, the $l_2-$norm of the
samples has a [chi distribution](https://en.wikipedia.org/wiki/Chi_distribution)
with parameter $n$, $\chi_n$; it has mode $\sqrt{n-1}$, and a mean that is
approximately equal to $\sqrt{n}$ as $n$ grows. This means the variance, given
by $n$ minus the square of the mean, is approximately equal to zero. 
Empirically, with 1,000 samples, I found the standard deviation of the samples
to remain around 0.7 for dimensions $n=$1 to 100,000. A more rigorous
explanation that almost all samples remain in a band of constant thickness
can be found
[here](https://www.cs.cmu.edu/~venkatg/teaching/CStheory-infoage/chap1-high-dim-space.pdf).

### Side note
As a 'fun' little exercise, we can re-derive the distribution of the $l_2-$norm
of a multivariate standard normal. Assume $X \sim \mathcal{N}(0,I)$, then
\\[ \mathcal{P}(|X| \leq \alpha) = \iint_{|x| \leq \alpha^2} (2\pi)^{-n/2}
\exp(-\|x\|^2/2) dx \\]
We turn to spherical coordinates,
\\[ x_1  = r \cos \theta_1 \\]
\\[ x_2  = r \sin \theta_1 \cos \theta_2 \\]
\\[ \vdots \\]
\\[ x_i = r \sin \theta_1 \ldots \sin \theta_{i-1} \cos \theta_i \\]
\\[ \vdots \\]
\\[ x_n = r \sin \theta_1 \ldots \ldots \sin \theta_{n-2} \sin \theta_n \\]
And the Jacobian of the transformation is given 
[by](https://en.wikipedia.org/wiki/N-sphere#Spherical_coordinates)
\\[ \left| \frac{\partial x}{\partial \theta} \right| = r^{n-1} \sin^{n-2}
\theta_1 \ldots \sin \theta_{n-2} \\]
However the exact form of the Jacobian does not matter. Since the pdf of the
multivariate standard normal only depends on the radius, $\mathcal{P}(|X|\leq
\alpha)$ will be given by
\\[ \mathcal{P}(|X|\leq \alpha) = S_n (2\pi)^{-n/2} \int_0^{\alpha} r^{n-1}
e^{-r^2/2} dr , \\]
where $S_n$ is the part of the volume of unit n-sphere that does not depend on
the radius, i.e., all the integrals for the $\theta_i$'s. Again, we use the
formula for the volume of a unit n-sphere to get
\\[ \frac{\pi^{n/2}}{\Gamma(n/2+1)} = S_n \int_0^1 r^{n-1} dr \\]
Using the definition of the 
[gamma function](https://en.wikipedia.org/wiki/Gamma_function)
we re-write $S_n$ as
\\[ S_n = \frac{n \pi^{n/2}}{n/2 \, \Gamma(n/2)} \\]
and finally get
\\[ \mathcal{P}(|X|\leq \alpha) = 
\frac{1}{2^{n/2-1} \Gamma(n/2)} \int_0^{\alpha} r^{n-1}
e^{-r^2/2} dr , \\]
which corresponds to a chi distribution.
