import timeit
print(timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = [i for i in input_list if div_by_two(i)]''', number=50000))

#list comprehension is faster but uses more mem and vice versa is the case of generators