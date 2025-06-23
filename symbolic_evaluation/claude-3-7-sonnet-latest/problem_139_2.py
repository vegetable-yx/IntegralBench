import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at 2
I0 = mp.besseli(0, 2)

# Subtract 1 from the Bessel function value
temp = I0 - 1

# Multiply by 4 to get the final result
result = 4 * temp

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))