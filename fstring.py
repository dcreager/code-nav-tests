x = 123
y = f"does this work {x}"

def passthrough(z):
    return z

result = f"and how about this {passthrough(x)}"
other = passthrough(x)
