import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute components separately for clarity
sqrt2 = mp.sqrt(2)                     # Calculate √2
catalan_contribution = 2 * mp.catalan  # 2G term
sqrt_contribution = 2 * sqrt2          # 2√2 term

# Logarithmic component calculation
log_argument = 1 + sqrt2               # Compute (1 + √2)
log_term = -2 * mp.log(log_argument)   # -2ln(1+√2)

constant_adjustment = -2               # Final constant term

# Combine all components
result = (catalan_contribution 
          + sqrt_contribution 
          + log_term 
          + constant_adjustment)

print(mp.nstr(result, n=10))