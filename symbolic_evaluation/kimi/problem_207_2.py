import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute e^{-1} (reciprocal of Euler's number)
exp_minus_one = mp.exp(-1)

# Multiply by π and then divide by 2
result = (mp.pi * exp_minus_one) / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))