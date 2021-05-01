def zero(x=False): return x(0) if x else 0
def one(x=False): return x(1) if x else 1
def two(x=False): return x(2) if x else 2
def three(x=False): return x(3) if x else 3
def four(x=False): return x(4) if x else 4
def five(x=False): return x(5) if x else 5
def six(x=False): return x(6) if x else 6
def seven(x=False): return x(7) if x else 7
def eight(x=False): return x(8) if x else 8
def nine(x=False): return x(9) if x else 9


def plus(x): return lambda n: n + x
def minus(x): return lambda n: n - x
def times(x): return lambda n: n * x
def divided_by(x): return lambda n: n // x
