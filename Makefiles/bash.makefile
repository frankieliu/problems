# https://stackoverflow.com/questions/32548993/advanced-pattern-matching-in-makefile

# If I understood your question correctly, you have a bunch of
# *.source files, and want a rule that turns each into a *.target
# file, while picking two sub-strings from whatever the * expands to.

# Why not pick the stem in $* apart at the underscore? Here's a
# solution. If you have these files

# $ ls *.source
# 1_1.source
# 1_2.source
# 1_3.source
# a_b.source
# foo_bar.source
# then running this GNUmakefile's default target

# all should depend on all targets for which a source exists.
# all: $(shell echo *.source | sed 's/source/target/g')

# %.target: %.source
#    @z="$*" y="$*"; \
#    z=$${z%%_*} y=$${y##*_}; \
#    echo z=$$z y=$$y
# will give you

# $ gmake
# z=1 y=1
# z=1 y=2
# z=1 y=3
# z=a y=b
# z=foo y=bar
