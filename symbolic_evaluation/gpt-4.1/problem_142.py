import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the parameter 'a'. Since not specified, we use a=1.0 as an example.
a = 1.0

# Compute the result: sinh(a)/a
# Handle a=0 case separately to avoid division by zero
if a == 0:
    result = mp.mpf(1)  # Limit as a->0 is 1
else:
    # sinh(a) is the hyperbolic sine function
    sinh_a = mp.sinh(a)
    result = sinh_a / a

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))