cpp=gg
obj=hh
sample=adfds.gg
result=$(patsubst %.$(cpp),%.$(obj),$(sample))

all:
	echo $(result)
