# set the target executables that need to be built
TARGETS := my_program

# set some flags and compiler/linker specific commands
CXXFLAGS = -ggdb -O2 -DNDEBUG
LDFLAGS = -Wall -ggdb

include /path_to_generic_makefile/generic.mk
