from table import table

def kmp(s, w):

    wl = len(w)
    wi = 0
    si = 0
    t = table(w)

    while si < len(s):
        if w[wi] == s[si]:
            wi = wi + 1
            si = si + 1
            if wi == wl:
                return si - wl
        else:
            if wi == 0:
                si = si + 1
            else:
                wi = t[wi - 1]

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.WARNING)
    print(
        kmp(s="ABC ABCDAB ABCDABCDABDE",
            w="ABCDABD")
    )
