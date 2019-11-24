library(ggplot2)
options(repr.plot.width = 5, repr.plot.height = 3)

sigma <- 0.6
conf.int <- function(data,
                     alpha=0.05) {
    quantile(data, probs=c(alpha/2, 1-alpha/2))
}

gen.test <- function(n, mu.0, mu.1, sigma) {
    x <- rnorm(n, mu.0, sigma)
    y <- rnorm(n, mu.1, sigma)
    t.val <- sqrt(n) * (mean(x) - mean(y)) / (sqrt(2)*sigma)
    t.val
}

set.seed(1)

n = 50
test.stats <- replicate(10000, gen.test(n, 3, 3, 0.6))

qplot(test.stats, binwidth=0.1, main="n = 50") +
    geom_vline(xintercept=-1.96) +
    geom_vline(xintercept=1.96)

p.values <- 2*pnorm(-abs(test.stats))

qplot(p.values, binwidth=0.01, main="n = 50") +
    geom_vline(xintercept=.05)

rejects <- test.stats[p.values < 0.05]
frac.reject <- length(rejects)/length(test.stats)
magnitude <- mean(abs(rejects * sqrt(2) * sigma / sqrt(n)))
sign <- 1-mean(sign(rejects) == 1)

cat("fraction rejected:", frac.reject, "\n")

n <- 1000

test.stats <- replicate(10000, gen.test(n, 3, 3, 0.6))

qplot(test.stats, binwidth=0.1, main="n = 1000") +
    geom_vline(xintercept=-1.96) + geom_vline(xintercept=1.96)

p.values <- 2*pnorm(-abs(test.stats))
qplot(p.values, binwidth=0.01, main="n = 1000") +
    geom_vline(xintercept=.05)

rejects <- test.stats[p.values < 0.05]
frac.reject <- length(rejects)/length(test.stats)
cat("fraction rejected:", frac.reject, "\n")
