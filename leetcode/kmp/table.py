import logging

"""
This is the length of the longest proper prefix that is a suffix
Example:
abcabc

suffixes:
c      : not a prefix
bc     : not a prefix
abc    : prefix (length 3)    3
cabc   : not a prefix
bcabc  : not a prefix
abcabc : not a proper prefix

abcabc
000123 <- so table should look like this

       <- it seems that you keep track of the
          longest prefix so far, and if the
          char that you are looking at also
          matches the next char in the prefix
          you add a 1 to the t(n-1), i.e.
          t(n) = t(n-1) + 1, or
          t(n) = k (the location of the current match)
"""

def table(w):
    T = [0] * len(w)  # for the first character there is no proper prefix
    pos = 1           # current position the next char
    cnd = 0           # index in matching candidate

    while pos < len(w):
        logging.info("comparing {} to {}".format(w[pos], w[cnd]))
        if w[pos] == w[cnd]:
            # print(pos)
            T[pos] = cnd + 1
            cnd = cnd + 1
        else:
            if cnd == 0:
                logging.info("cnd at 0 already")
                T[pos] = 0
            else:
                cnd = 0
                if w[pos] == w[cnd]:
                    T[pos] = cnd + 1
                    cnd = cnd + 1
                else:
                    logging.info("rewound cnd and no match")
                    T[pos] = 0
        pos = pos + 1

    return T

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    print(table("abcabc"))
    print(table("abababca"))
    print(table("abcdabd"))
