import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components separately
sqrt2 = mp.sqrt(2)  # Compute square root of 2
pi = mp.pi          # Get π constant
j1 = mp.besselj(1, 1)  # Compute Bessel function J₁(1)

# Combine components for final result
result = sqrt2 * pi * j1

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))