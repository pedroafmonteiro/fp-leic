def deriv(y):
    def dy(x):
        derivative = (y(x + 0.001) - y(x)) / 0.001
        return round(derivative,3)
    return dy