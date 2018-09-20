# 1. touchp 13/roman-to-integer.hpp
# 2. make with this makefile

# Gets the newest directory
new=$(shell ls -Artd [1-9]*/ | tail -n 1 | sed 's/\/$$//')

# Finds the title of the problem via the *.hpp file
title=$(shell ls -Artd $(new)/*.hpp | tail -n 1 | xargs -I {} basename {} .hpp)
# Change dashes to underscores
title_=$(shell echo $(title) | sed s/-/_/g)

all: $(new)/Makefile $(new)/test.cpp

$(new)/Makefile:
	ln -s ../Template/Makefile $@

$(new)/test.cpp:
	echo $(title) $(title_)
	cp Template/test.cpp $@
	: # Replace the templates
	sed -i 's/%title%/$(title)/;s/%title_%/$(title_)_$(new)/' $@
