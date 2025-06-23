import mpmath as mp
mp.dps = 15

# Calculate the hyperbolic sine integral of 2
shi_value = mp.shi(2)

# Divide by 2 to get the final result
result = shi_value / 2

print(mp.nstr(result, n=10))