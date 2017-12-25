#SOURCES := $(shell find . -name '*.cpp')
RECENT := $(shell ls -t *.cpp | head -n1)
OBJ := $(patsubst %.cpp,%.o,$(RECENT))
EXE := $(patsubst %.cpp,%,$(RECENT))
CPPLIBS := -lstdc++
C11FLAG := -std=c++11
TARGET := target
top: $(TARGET)/$(EXE)
	./$(TARGET)/$(EXE)

$(TARGET)/$(EXE): $(TARGET)/$(OBJ)
	$(CC) $(C11FLAG) $(TARGET)/$(OBJ) -o $@ $(CPPLIBS)

$(TARGET)/%.o: %.cpp
	$(CC) $(C11FLAG) -c $< -o $@
