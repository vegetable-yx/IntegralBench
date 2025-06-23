import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of parameter a (example value, adjust as needed)
a = 1.0

# Compute exponential term: e^(a/2)
exp_term = mp.exp(a / 2)

# Compute hyperbolic cosine term: cosh(a)
cosh_a = mp.cosh(a)

# Compute the second part: (1 + cosh(a)) / 2
second_term = (1 + cosh_a) / 2

# Final result: e^(a/2) - (1 + cosh(a))/2
result = exp_term - second_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))