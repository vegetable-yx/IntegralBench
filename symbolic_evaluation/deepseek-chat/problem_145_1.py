import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate I_0(2) - modified Bessel function of the first kind of order 0 at 2
bessel_value = mp.besseli(0, 2)

# Subtract 1 from the Bessel function value
adjusted_value = bessel_value - 1

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * adjusted_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))