
library(boot)
meanfun <- function (data, i){
    d <- data[i]
    return (mean (d))
}

c <- c(1,1,1,1,1,1,1,0,0,0)
bo<-boot (c, statistic=meanfun, R=1000)
plot(bo)
# boot.ci (bo, conf=0.95, type="bca")  #obviously `bo` was not made
