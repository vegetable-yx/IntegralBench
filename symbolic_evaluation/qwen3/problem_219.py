import mpmath as mp
mp.dps = 15

# Compute the sine integral of 1
si_1 = mp.si(1)

# Compute the cosine integral of 1
ci_1 = mp.ci(1)

# Sum the integral results
sum_integrals = si_1 + ci_1

# Multiply by square root of 2
result = mp.sqrt(2) * sum_integrals

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))