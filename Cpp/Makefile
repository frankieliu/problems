# This makefile looks at the most recently changed cpp file

# SOURCES := $(shell find . -name '*.cpp')
RECENT := $(shell ls -t *.cpp *.c | head -n1)
CEXT := $(suffix $(RECENT))
OEXT := .o

OBJ := $(patsubst %$(CEXT),%$(OEXT),$(RECENT))
EXE := $(patsubst %$(CEXT),%,$(RECENT))

ifeq ($CEXT,.cpp)
	CPPLIBS := -lstdc++
	C11FLAG := -std=c++11
else
	CPPLIBS :=
	C11GLAG :=
endif

# target directory
TARGET := target

top: $(TARGET)/$(EXE)
	./$(TARGET)/$(EXE)

$(TARGET)/$(EXE): $(TARGET)/$(OBJ)
	$(CC) $(C11FLAG) $(TARGET)/$(OBJ) -o $@ $(CPPLIBS)

$(TARGET)/%.o: %$(CEXT)
	$(CC) $(C11FLAG) -c $< -o $@
