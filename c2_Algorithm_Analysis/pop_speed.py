pop_zero = Timer("x.pop(0)",
	"from __main__ import x")

pop_end = Timer("x.pop()",
	"from __main__ import x")

x = list(range(2000000))
print(f"POP START: {pop_zero.timeit(number=1000):.9f}")

print(f"POP END: {pop_end.timeit(number=1000):.9f}")
