import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the function to compute the analytical expression
def compute_result(a, b):
    # Compute the argument for Bessel functions: ab/2
    arg = (a * b) / 2
    
    # Compute modified Bessel functions I0 and I2 at the argument
    I0 = mp.besseli(0, arg)
    I2 = mp.besseli(2, arg)
    
    # Compute the difference I0 - I2
    bessel_diff = I0 - I2
    
    # Compute the constant factor: a * π / 2
    factor = (a * mp.pi) / 2
    
    # Multiply factor by the Bessel difference
    result = factor * bessel_diff
    return result

# Example usage (replace with actual a and b values)
a_val = 1.0  # Example value, replace as needed
b_val = 1.0  # Example value, replace as needed

# Compute the result
result = compute_result(a_val, b_val)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))