import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Example values for parameters a and b
# Replace these with actual values as needed
a = 1.0
b = 1.0

# Compute the argument for the Bessel function: (a*b)/2
arg = (a * b) / 2

# Calculate the modified Bessel function I_0 at the computed argument
bessel_val = mp.besseli(0, arg)

# Compute the final result: (a * pi / 2) multiplied by the Bessel value
result = (a * mp.pi / 2) * bessel_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))