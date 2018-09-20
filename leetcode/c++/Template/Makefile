# Find the latest hpp file
file_hpp=$(shell ls -Art *.hpp | tail -n 1)

run: test
	./test

test: test.cpp $(file_hpp)
	g++ -o test test.cpp -L /usr/lib -lgtest -lgtest_main -lpthread
