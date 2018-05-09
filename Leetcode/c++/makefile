new=$(shell ls -Artd [1-9]*/ | tail -n 1)

all: $(new)/Makefile $(new)/test.cpp

$(new)/Makefile:
	ln -s ../Template/Makefile $@

$(new)/test.cpp:
	cp Template/test.cpp $@
