+++
title = "Non-parametric"
description = ""
weight = 1
+++

[hugo-setup](https://henrybear327.github.io/CodingNotes/tools/hugo/hugo-setup/)
[backslashes-hugo-markdown](https://github.com/gcushen/hugo-academic/issues/291)
[academic](https://academic-demo.netlify.com/)

<!--more-->

## Confidence interval

Say you are trying to estimate $\theta$.  It is a known fixed real
number and let $X_1$ and $X_2$ be iid,
\\[
Pr(X_i = 1) = Pr(X_i = -1) = \frac{1}{2}.
\\]
You measure $Y_1$ and $Y_2$, there $Y_i = \theta + X_i$.  Suppose you
only have these two samples.

Define the confidence interval (one point):

$$
C =\begin{cases}
Y_i - 1 &\text{if } Y_1 = Y_2 \\\\\\
\frac{Y_1 + Y_2}{2} &\text{otherwise}
\end{cases}
$$

So indendent of $\theta$, $Pr(\theta \in C)=\frac{3}{4}$, i.e.  this
is a 75 percent confidence interval.

Note this confidence interval doesn't say anything about the
probability of $\theta$, since $\theta$ is a fixed number.  For
example, if $Y_1 = 15$ and $Y_2 = 17$, $Pr(\theta = 16) = 0.75$.  Just
says that 75% of the intervals calculated in this way will contain the
parameter.

From L.Wasserman:

> A confidence interval is not a probability statement about $\theta$
> since $\theta$ if a fixed quantity, not a random variable.  Some
> ... interpret confidence intervals as ...: if I repeat the
> experiment over and over, the interval will contain the paramater
> 95% of the time.  This is correct but uselss since we rarely repeat
> the same experiment over and over.  A better interpretation is: for
> each day you collect data, construct a 95% confidence interval for
> some $\theta$.  95% of your intervals will trap the true parameter
> value.





