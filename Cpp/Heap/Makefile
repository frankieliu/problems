# set the binaries that have to be built
TARGETS := heap_test

# set which libraries are used by which executable
LIBS = stdc++
LDLIBS = $(addprefix -l, $(LIBS) $(LIBS_$(notdir $*)))

C11FLAG := -std=c++11

# set some flags and compiler/linker specific commands
CXXFLAGS = -g -Wmultichar $(C11FLAG) $(addprefix -I, $(INCLUDEDIRS))

LDFLAGS = -g $(addprefix -L, $(LIBDIRS))

# we set specific compilers for specific tools
CXX = $(if $(CXX_$(notdir $*)), $(CXX_$(notdir $*)), g++)

include ../../Makefiles/generic.mk
