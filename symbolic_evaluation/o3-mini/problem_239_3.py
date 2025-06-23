import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (value not specified in problem, using example value)
a = 1

# Define the function f(nu) = I_nu(a)
def f(nu):
    # Modified Bessel function of the first kind
    return mp.besseli(nu, a)

# Compute the derivative of f at nu=1 using central difference
# Step size for numerical differentiation (adjustable for precision)
h = 1e-7
f_plus = f(1 + h)   # Evaluate at nu = 1 + h
f_minus = f(1 - h)  # Evaluate at nu = 1 - h
derivative = (f_plus - f_minus) / (2 * h)  # Central difference formula

# Apply the negative sign as per the expression
result = -derivative

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))