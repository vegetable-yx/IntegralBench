import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modified Bessel function of the first kind I_0(1)
bessel_value = mp.besseli(0, 1)

# Calculate sqrt(2)
sqrt_two = mp.sqrt(2)

# Multiply components: sqrt(2) * pi * I_0(1)
result = sqrt_two * mp.pi * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))