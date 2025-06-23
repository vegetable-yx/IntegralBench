import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Si(3) using the relationship: Si(x) = si(x) + π/2
# where si(x) is the alternate sine integral (mp.si)
si_3 = mp.si(3)
Si_3 = si_3 + mp.pi/2

# Compute the final expression: (π/2) * Si(3)
result = (mp.pi / 2) * Si_3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))