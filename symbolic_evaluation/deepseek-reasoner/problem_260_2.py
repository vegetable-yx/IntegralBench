import mpmath as mp
mp.dps = 15

# Compute cosine of 1
cos_1 = mp.cos(1)

# Calculate the first term: (π/2)(1 - cos(1))
term1 = (mp.pi / 2) * (1 - cos_1)

# Compute the sine integral of 1
si_1 = mp.si(1)

# Combine the terms to get the final result
result = term1 - si_1

print(mp.nstr(result, n=10))