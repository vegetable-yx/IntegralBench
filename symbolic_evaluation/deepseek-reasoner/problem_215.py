import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the coefficient term (4π^(3/2))/Γ(1/4)^2
pi_power = mp.pi ** (3/2)          # Compute π^(3/2)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)  # Compute Γ(1/4)
gamma_squared = gamma_1_4 ** 2     # Square the gamma value
coefficient = (4 * pi_power) / gamma_squared  # Combine components

# Calculate the hypergeometric function {}_1F_2(3/4; 1/2, 5/4; -1/16)
a = mp.mpf(3)/4                     # First parameter
b = [mp.mpf(1)/2, mp.mpf(5)/4]      # Second parameters list
z = mp.mpf(-1)/16                   # Function argument
hyper_term = mp.hyper([a], b, z)    # Compute hypergeometric function

# Calculate final result and print with 10 decimal precision
result = coefficient * hyper_term
print(mp.nstr(result, n=10))