import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the argument for the Bessel function
arg = 1 / mp.sqrt(2)

# Compute modified Bessel function of the first kind I_{3/2}(1/sqrt(2))
bessel_value = mp.besseli(1.5, arg)

# Multiply by 1/6 to get the final result
result = (1/6) * bessel_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))