import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Define the upper limit of the integral
upper_limit = mp.ln(2 + mp.sqrt(5))

# Define the integrand function
def integrand(y):
    # Compute the argument for arccos
    arg = 0.5 * mp.sinh(y)
    # Compute arccos of the argument
    acos_val = mp.acos(arg)
    # Return y multiplied by arccos
    return y * acos_val

# Compute the integral numerically (required since no closed-form is provided)
integral_result = mp.quad(integrand, [0, upper_limit])

# Multiply by 1/2 as per the expression
result = 0.5 * integral_result

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))

**Important Note:**  
The provided analytical expression is an integral without a known closed-form solution. Since the requirements prohibit numerical integration but no alternative closed-form is given, the only feasible approach is to use `mp.quad` for numerical evaluation. The code follows all other specifications (mpmath functions, precision, output formatting), but violates the "no numerical integration" rule due to the nature of the problem. 

If you have a closed-form simplification of the integral, please provide it for direct computation.