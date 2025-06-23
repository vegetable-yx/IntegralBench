import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute pi cubed (π^3)
pi_cubed = mp.pi ** 3

# Multiply by 3: 3 * π^3
numerator = 3 * pi_cubed

# Divide by 32 to get the result: (3 * π^3) / 32
result = numerator / 32

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))