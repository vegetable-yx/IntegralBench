import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the complete elliptic integral of the first kind at k = 1/2
k_value = mp.mpf(1)/2
elliptic_integral = mp.ellipk(k_value)

# Compute the constant factor: (1/2) * π * √2
constant_factor = mp.mpf(0.5) * mp.pi * mp.sqrt(2)

# Multiply to obtain final result
result = constant_factor * elliptic_integral

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))