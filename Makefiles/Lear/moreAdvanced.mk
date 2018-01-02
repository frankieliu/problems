# set the binaries that have to be built
SRCS := $(wildcard tools/*.cpp)
TARGETS := $(TARGETS) $(SRCS:.cpp=)

# set the build configuration set
BUILD := release
#BUILD := debug

BIT := 64
#BIT := 32

# set bin and build dirs
BUILDDIR := .build_$(BUILD)$(BIT)
BINDIR := $(BUILD)$(BIT)

# include directories
INCLUDEDIRS := \
	common_code \
	$(HOME)/more_common_code

# library directories
LIBDIRS :=

# set which libraries are used by which executable
# $* matches the prefix of a pattern rule such as foo in %.xyz given foo.xyz
LDLIBS = $(addprefix -l, $(LIBS) $(LIBS_$(notdir $*)))
LIBS = cv boost_program_options-mt-d boost_serialization-mt-d boost_regex-mt-d
LIBS_mySimpleTool :=
LIBS_myComplicatedTool := highgui avformat avcodec avutil

# set some flags and compiler/linker specific commands
CXXFLAGS = -fopenmp -m$(BIT) -pipe -D STD=std -Wall $(CXXFLAGS_$(BUILD)) $(addprefix -I, $(INCLUDEDIRS))
CXXFLAGS_debug := -ggdb
CXXFLAGS_release := -ggdb -O3 -DNDEBUG

LDFLAGS = -m$(BIT) -pipe -Wall $(LDFLAGS_$(BUILD)) $(addprefix -L, $(LIBDIRS))
LDFLAGS_debug := -ggdb
LDFLAGS_release := -ggdb -O3

# we set specific compilers for specific tools
CXX = $(if $(CXX_$(notdir $*)), $(CXX_$(notdir $*)), g++)
CXX_myComplicatedTool := mpiCC

include /path_to_generic_makefile/generic.mk
