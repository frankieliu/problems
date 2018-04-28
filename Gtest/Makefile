# Find the latest hpp file
file_hpp=$(shell ls -Art test.cpp | tail -n 1)

run:
	echo $(file)
test: test.cpp
	g++ test.cpp -L /usr/lib -lgtest -lgtest_main -lpthread
