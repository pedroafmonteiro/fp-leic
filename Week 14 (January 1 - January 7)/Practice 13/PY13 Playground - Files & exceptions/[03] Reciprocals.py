def reciprocals(alist):
    result = []
    for n in alist:
        try:
            result.append(1/n)
        except ZeroDivisionError:
            pass
        except TypeError:
            pass
        except ValueError:
            pass
    return result
