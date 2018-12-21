---
layout: post
title: Market-cap weighted portfolios are self-rebalancing
tags: finance
---

This is a very simple note about a proof that I regularly forget. It is often
said that a great advantage of market-cap weighted portfolios is that they are
self rebalancing. That is, when you choose the weights of each security in a
portfolio according to the proportion of their market-cap, the weights remain
consistent with the original definition (under some rather mild assumptions).

#### Return of a portfolio
First, an even simpler result that we need in the rest of that note: The return
of a portfolio is simply the weighted average of the returns of the securities
in the portfolio. Let's introduce some notation: let's call $X_t$ the
\\$-value of
the portfolio at time $t$, and $X_t = \sum_i X_{i,t}$ where $X_{i,t} = w_{i,t}
X_t$ is the \\$-value of the $i^\text{th}$ security in the portfolio at time
$t$. 
The sum is taken over all securities in the portfolio, and we assume the weights
sum to 1.
Next the return of the portfolio (similarly for any security $i$) is defined by $r_t =
X_t/X_{t-1}-1$.
Then,
$$ \begin{align} 
X_t & = \sum_i X_{i,t} = \sum_i (1+r_{i,t}) X_{i,t-1} = \sum_i (1+r_{i,t})
w_{i,t-1} X_{t-1} \notag \\ 
& = X_{t-1} \left( 1 + \sum_i w_{i,t-1} r_{i,t} \right),
\end{align} $$
since by definition $\sum_i w_{i,t} = 1$ at any time $t$.
Note that the same conclusion applies to all type of returns, including
continuously compounded returns
$$\bar{r}_{i,t}$$, since $1+r_{i,t} = e^{\bar{r}_{i,t}}$.

#### Self-rebalancing
Let's define $M_{i,t}$ as the market-cap of security $i$, and let $M_t =
\sum_i M_{i,t}$.
Now let's assume that in the period $t-1$, the weights are calculated as a
proportion of their relative market-cap, i.e., $w_{i,t-1} = M_{i,t-1} /
M_{t-1}$. And let's assume that from period $t-1$ to $t$, the market-cap of all
securities $i$ only vary through its price (number of shares remain constant, no
M$\&$A,...).
Then, the ratios of market-cap will vary from $t-1$ to $t$
as
\\[ \frac{M_{i,t}/M_t}{M_{i,t-1}/M_{t-1}} =  \frac{M_{i,t}}{M_{i,t-1}} \frac{M_{t-1}}{M_t}
 = \frac{1+r_{i,t}}{1+r_t} . \\]
On the other hand, the weights of the portfolios will vary as
\\[ \frac{w_{i,t}}{w_{i,t-1}} = \frac{X_{i,t}/X_t}{X_{i,t-1}/X_{t-1}} 
= \frac{X_{i,t}}{X_{i,t-1}} \frac{X_{t-1}}{X_t}
 = \frac{1+r_{i,t}}{1+r_t} . \\]

