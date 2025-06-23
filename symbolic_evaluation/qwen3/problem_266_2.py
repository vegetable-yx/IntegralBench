import mpmath as mp

mp.dps = 15

# Compute the cosine term (cos(2) - 1)/2
cos_2 = mp.cos(2)
cos_term = (cos_2 - 1) / 2

# Compute the sine integral term Si(2)
si_term = mp.si(2)

# Sum the terms to get the result
result = cos_term + si_term

print(mp.nstr(result, n=10))