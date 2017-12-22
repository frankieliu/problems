#SOURCES := $(shell find . -name '*.cpp')
RECENT := $(shell ls -t *.cpp | head -n1)
OBJ := $(patsubst %.cpp,%.o,$(RECENT))
EXE := $(patsubst %.cpp,%,$(RECENT))
CPPLIBS := -lstdc++
C11FLAG := -std=c++11
top: $(EXE)
	./$(EXE)

$(EXE): $(OBJ)
	$(CC) $(C11FLAG) $(OBJ) -o $@ $(CPPLIBS)

%.o: %.cpp
	$(CC) $(C11FLAG) -c $< -o $@
