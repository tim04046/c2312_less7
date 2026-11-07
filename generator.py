def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number**i

res = raise_to_the_degrees(10, 500)
print(res)
for _ in res:
    print(_)