import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^{-2}
exp_term = mp.exp(-2)

# Compute (1 - e^{-2})
diff = 1 - exp_term

# Multiply by pi and divide by 2: (\pi/2) * (1 - e^{-2})
result = (mp.pi / 2) * diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))