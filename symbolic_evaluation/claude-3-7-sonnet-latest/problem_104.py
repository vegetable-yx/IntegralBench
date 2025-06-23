import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Define the input value for arcsin
x = mp.mpf(1)/4  # Represent 1/4 as an exact mpmath float

# Compute arcsin(1/4) using mpmath's asin function
result = mp.asin(x)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))