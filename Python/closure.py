# https://stackoverflow.com/questions/21959985/why-cant-python-increment-variable-in-closure
def make_counter(init_value=0):
    sum = [init_value]
    def inc(x=0):
        sum[0] += x
        return sum[0]
    return inc

counter = make_counter(10)
print(counter(1))
print(counter(2))
print(counter(3))
print(counter())
