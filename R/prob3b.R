library(ggplot2)

options(repr.plot.width=4, repr.plot.height=3)

lincoln.peterson <- function(n, K, k) {
    K * n / k
}

chapman <- function(n, K, k) {
    (K+1) * (n+1) / (k+1) - 1
}

n = 200
K = 200
k = 21

cat("Estimate of population (LP):",
    lincoln.peterson(n, K, k), "\n")

cat("Estimate of population (C): ",
    chapman(n, K, k))
set.seed(1)

alpha <- 0.05
nboot <- 1000
boot.samples <- sort(
    sapply(rbinom(nboot, K, k/K),
           function(kboot) {chapman(n, K, kboot)}))

boot.mean <- mean(boot.samples)
boot.SE <- sd(boot.samples)
cat("Bootstrap qCI: ",
    boot.samples[round(nboot * alpha/2)],
    boot.samples[round(nboot * (1-alpha/2))], "\n")
cat("Bootstrap seCI:",
    boot.mean - 1.96*boot.SE,
    boot.mean + 1.96 * boot.SE)
qplot(boot.samples, bins=50)
