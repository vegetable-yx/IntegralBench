import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate key constants
sqrt2 = mp.sqrt(2)  # Square root of 2
log_val = mp.log(1 + sqrt2)  # Natural logarithm of (1 + sqrt(2))
arg_val = 0.5 - 0.5 / sqrt2  # Argument for polylog functions: 1/2 - 1/(2*sqrt(2))

# Compute polylogarithm functions
Li2_val = mp.polylog(2, arg_val)  # Dilogarithm Li₂ at computed argument
Li3_val = mp.polylog(3, arg_val)  # Trilogarithm Li₃ at computed argument

# Compute each term of the expression
term1 = mp.pi**3  # π³ term
term2 = 12 * mp.pi * log_val**2  # 12π[ln(1+√2)]² term
term3 = -24 * log_val * Li2_val  # -24ln(1+√2) Li₂(...) term
term4 = 24 * Li3_val  # 24 Li₃(...) term

# Combine all terms and divide by 48
result = (term1 + term2 + term3 + term4) / 48

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))