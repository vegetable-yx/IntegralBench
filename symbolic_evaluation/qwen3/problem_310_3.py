import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate π/2 using mpmath constant for pi divided by 2
result = mp.pi / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))