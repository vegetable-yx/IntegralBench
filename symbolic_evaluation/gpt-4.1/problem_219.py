import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for the Bessel function: sqrt(2)/2
arg = mp.sqrt(2) / 2

# Compute the Bessel function of the first kind of order 1 at the given argument
bessel_val = mp.besselj(1, arg)

# Multiply by sqrt(2) and pi to get the final result
result = mp.sqrt(2) * mp.pi * bessel_val

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))