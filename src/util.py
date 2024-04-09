from math import *
import globals


def cute_round(x, k):
    if x % 1 == 0:
        return int(x)
    return round(x, k)


def cute_float(x, delta):
    """Transforms float to scientific form"""

    e = int(log(delta, 10))
    if e >= 3:
        e = int(log(delta, 10**3))
        return str(cute_round(x / 10 ** (e * 3), 1)) + "e" + str(e * 3)
    elif 3 > e and e >= 1:
        return str(cute_round(x, 1))
    elif e >= 0:
        return str(round(x, 2))
    return str(cute_round(x / 10**e, 2)) + "e" + str(e)

def process(string):
    """Edits function string"""
    string = string.replace("^", "**")
    symbols = " ()+-*/^"

    prev = 0
    varnames = set()
    while prev < len(string):
        while string[prev] in symbols:
            prev += 1
            if prev == len(string):
                return string, varnames
        now = prev + 1
        while now < len(string) and string[now] not in symbols:
            now += 1
        varname = string[prev:now]
        if varname != "x":
            try:
                eval(varname)
            except:
                varnames |= {varname}
                l = len("globals.global_kwargs['']")
                string = (
                    string[:prev]
                    + f"globals.global_kwargs['{varname}']"
                    + string[now:]
                )
                now += l
        prev = now
    return string, varnames

def evaltest_function(func, varnames):
    """Checks if the function is correct"""
    added = set()
    try:
        for i in varnames:
            if i not in globals.global_kwargs:
                added |= {i}
                globals.global_kwargs[i] = 0

        func(0, globals.global_kwargs)

    except SyntaxError as e:
        for i in added:
            globals.global_kwargs.pop(i)
        return False
    except BaseException:
        pass
    for i in added:
        globals.global_kwargs.pop(i)
    return True