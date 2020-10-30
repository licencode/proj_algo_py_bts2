def ma_table(j):
    for i in range(1, 11):
        print(i, 'x', j, '=', i * j)
    return gestion_error


def gestion_error(ma_table):
    try:
        if ma_table < 0:
            raise ValueError("This is not a positive number!!")
    except ValueError as e:
        print(e)
    else:
        return ma_table()



z = int(input("number: "))

gestion_error(z)
