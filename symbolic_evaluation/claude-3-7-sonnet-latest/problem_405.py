import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate each exponential term individually
exp1 = mp.exp(1)  # e^1
exp2 = mp.exp(2)  # e^2
exp3 = mp.exp(3)  # e^3
exp4 = mp.exp(4)  # e^4

# Combine terms according to the expression: 2e^4 + e^3 + e^2 + e - 1
result = 2 * exp4 + exp3 + exp2 + exp1 - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))