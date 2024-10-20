def add_everything_up (a, b):
    try:
        return a+b
    except TypeError:
        return str(a) + str(b)



print(add_everything_up(123.456, "kek"))
print(add_everything_up("гык", 52))
print(add_everything_up(17.45, 98))
print(add_everything_up('отче наш', ' сущий на небесах'))