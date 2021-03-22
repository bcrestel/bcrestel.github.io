---
layout: post
title: Intro to causal inference by Ferenc
tags: causality statistics
---

[Ferenc Huszar](https://www.inference.vc/) put together a series of 3 blog post to introduce different concepts of causal inference:
* [ML beyond Curve Fitting: An Intro to Causal Inference and do-Calculus](https://www.inference.vc/untitled/)
* [Illustrating Interventions via a Toy Example](https://www.inference.vc/causal-inference-2-illustrating-interventions-in-a-toy-example/)
* [Counterfactuals](https://www.inference.vc/causal-inference-3-counterfactuals/).

He mentions a fourth part dealing with "Causal Diagrams, Markov Factorization, Structural Equation Models", but I haven't seen anything related to it.

# ML beyond Curve Fitting: An Intro to Causal Inference and do-Calculus

In this first post, he mainly introduces the `do` operator and what it means. 
An important point is to understand the distinction between $p(y|x)$ and $p(y| do(x))$.
* $p(y|x)$: it's the typical conditional distribution we are used to calculate. 
It comes from an underlying joint distribution (say $p(x,y,z)$ for the sake of argument) and we have the relation $p(y|x) = p(x,y)/p(x)$ where the pdf in the ratio are marginal of the original joint distribution. 
But that joint distribution $p(x,y,z)$ corresponds to the data we observed. That is the fundamental difference with the other one.
* $p(y|do(x))$ is also a standard conditional distribution, albeit calculated from a joint distribution that does not correspond to the data we observed.
It is calculated from the joint distribution $p_{do(X=x)}(x,y,z)$ where we force the random variable $X$ to take the value $x$ by intervention (eg, A/B testing, randomized controlled trial,...).
In that case, we have $p(y|do(x)) = p_{do(X=x)}(x,y) / p_{do(X=x)}(x)$ (Note: it would seem to me that we should have $p_{do(X=x)}(x) = 1$; but I'll double check)

In other words, $p(y|x)$ answers the question "how $y$ changes given $x$" based on observational data, while
$p(y|do(x))$ answers that same question from an interventional point of view.
The main point of causal inference is to try and estimate this $p_{do(X=x)}(x,y,z)$ even without a randomized controlled trial.
And this is what the do-calculus is here for. Ferenc doesn't deep dive into do-calculus, but instead points to a reference [paper](https://arxiv.org/pdf/1305.5506.pdf).

In order to estimate this interventional pdf, one needs a causal model, that is
a model that explains how the different features are related to each other (not
just relations, but what causes what). Once you have such a model, you can
start altering the observed pdf.  But, "The mapping from causal diagrams to
joint distributions is many-to-one: several causal diagrams are compatible with
the same joint distribution. 
Thus, it is generally impossible to conclusively
choose between different causal explanations by looking at observed data only."

You can test the validity of a causal model against the data you have.
And you can extend that idea to do causal discovery. That is, test multiple causal models to find the one that best match the data.
However, you are still blocked by the fact that 
the relationship between causal model and data is many-to-one. 
So a causal model is more of a modeling choice.

# Illustrating Interventions via a Toy Example

In his second post, Ferenc shows an illustrative example of why the joint distribution doesn't tell the whole story.
He generates a 2d multivariate Gaussian distribution in 3 different ways.
They all have the same joint, but the ways they are constructed are different.
Therefore, they all have the same conditional distributions, for instance $p(y|X=3)$.

Then he simulates an intervention; basically, he conditions on $X=3$.
But because of the way each example is constructed, they do not lead to the same distribution for $p(y|do(X=3))$.
The first conclusion is that you cannot predict the results of an intervention from the joint distribution alone, 
as all 3 examples had the same joint.

The way to make a correct prediction for this intervention is to use the causal
diagram for each example.  "Graphically, to simulate the effect of an
intervention, you **mutilate the graph by removing all edges that point into the
variable on which the intervention is applied**, in this case x." 
After doing this, you see that some causal diagrams are un-modified (therefore the interventional distribution is the same as the 
original conditional distribution). Whereas in other examples, both variables become independent (and therefore 
the interventional distribution become the original marginal).
"This is called causal infernce from observational data."

# Counterfactuals

This post discussed counterfactuals, and mainly how they differ from intervention conditionals, like $p(y|do(X=\hat{x}))$, that was introduced in previous posts.
The main difference is that intervention conditionals deal with the whole population (they are averages of conditional probabilities), whereas counterfactuals deal with a single individual.
Ferenc uses the example of "does having a beard had anything to do with having a PhD?" So would I get a PhD if I didn't have a beard.
In that case, the intervention conditionals look at the distribution of all PhDs if we had shaved everyone who had a beard in the universe. Since both (having a beard and having a PhD) are actually  not causaly related, we would end up with the marginal of PhD holders in the world.
On the other hand, if we care about Ferenc in particular, this is not the average we want. 
We want to know how shaving that one specific inidividual would have affected their chances of gaining a PhD.
To illustrate that, he introduced Structural Equation Models (SEM), which will allow us to write things more rigorously.

SEMs are a set of equations that represent and quantify the causal dependencies of the variables in the problem.
That is, it defines the causal relations (like a causal graph), but also quantifies these relations (ie, it defines the equation to calculate one quantity from the others).
So from a SEM, you can deduce the causal graph, but the SEM also tells you how all the variables are related to each other (not just what variables are related to each other).
Since you have some uncertainty, you also have random variables $\varepsilon_i$ that enters the SEM. 
For instance, assuming $u$ is a deterministic input, you could have variables $x$ and $y$ defined as 
$$x = f_1(u, \varepsilon_1), y = f_2(x, u, \varepsilon_2), \dots$$

When you simulate intervention in a causal graph, you remove all edges pointing **toward** the variable you intervene on.
In the case of SEMs, this means you remove the single equation defining that variable and instead you set that variable to a constant deterministic value. 
The rest of the graph/equations remain unchanged. 
This also means that the realizations of the noise $\varepsilon_i$ (not just the random variable, but the actual realization of the noise for each equation) remain unchanged.
However, the variables obtained from the mutilated graph are not exactly the same as the one from the original graph. 
Ferenc defines them as some sort of *parallel twin* living in a *parallel universe*. 
The reason he is saying that is because we mix components of the "real world" (all other equations but the one corresponding to the intervention; realizations of the noise;...) with components that did not happen (ie, intervention).
He defines these variables with an asterisk, eg $$y^*$$.
One key sentence in the article is that "*counterfactuals are
making a prediction about features of the unobserved twin datapoint based on features of the observed datapoint.*"

Now that this is out of the way, we can write down clear equations for that a counterfactual is.
In the blog post example of the PhD (y) and the beard (x), the counterfactual can be written as
$$ p(y^*=1 | do(x=0), y=1, x=1)$$. 
In the blog post, he actually writes this as $$p(y^*=1 | x^*=0, y=1, x=1)$$. 
What's important to understand is that we have 2 joint distributions:
* $p(x,y)$ from the data, and
* $$p(x^*, y^*)$$ from the intervention.
Actually, this goes even further. 
Because both distributions rely on the same realization of the noise, both distributions actually come from the same joint distribution $$p(x,y,x^*,y^*)$$.
This is the reason why we can make counterfactuals in the first place!

Now that we have this large joint distribution, we can make the connection between intervention conditionals and counterfactuals:
$$p(y|do(X=\hat{x})) = p(y^*|x^*)= \int_{x,y} p(y^* | x^*, x, y) p(x,y) dxdy$$
Such that the intervention conditional is the expectation of all counterfactuals taken over the observed data.
