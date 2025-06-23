import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the Bessel function of the first kind of order 1 at z=1
j1_value = mp.besselj(1, 1)

# Compute the Struve function of order 1 at z=1
h1_value = mp.struveh(1, 1)

# Sum the Bessel and Struve function values
sum_j1_h1 = j1_value + h1_value

# Multiply by pi to get the final result
result = mp.pi * sum_j1_h1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))