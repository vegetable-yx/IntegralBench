

To solve the definite integral \( \int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx \), we use a substitution technique to exploit symmetry in the integrand.

### Step 1: Define the integral and substitute \( u = 2012 - x \)
Let \( I = \int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx \).  
Consider the substitution \( u = 2012 - x \), which implies \( du = -dx \). When \( x = 1 \), \( u = 2011 \), and when \( x = 2011 \), \( u = 1 \). Rewriting the integral in terms of \( u \):  
\[
I = \int_{2011}^1 \frac{\sqrt{2012 - u}}{\sqrt{u} + \sqrt{2012 - u}} (-du) = \int_1^{2011} \frac{\sqrt{2012 - u}}{\sqrt{u} + \sqrt{2012 - u}} \, du.
\]  
Since \( u \) is a dummy variable, we replace \( u \) with \( x \):  
\[
I = \int_1^{2011} \frac{\sqrt{2012 - x}}{\sqrt{x} + \sqrt{2012 - x}} \, dx.
\]

### Step 2: Add the original integral and the substituted integral
Let \( J = \int_1^{2011} \frac{\sqrt{2012 - x}}{\sqrt{x} + \sqrt{2012 - x}} \, dx \). From the substitution, we see \( J = I \).  
Adding \( I \) and \( J \):  
\[
I + J = \int_1^{2011} \frac{\sqrt{x} + \sqrt{2012 - x}}{\sqrt{x} + \sqrt{2012 - x}} \, dx = \int_1^{2011} 1 \, dx.
\]  
The integrand simplifies to 1, so:  
\[
I + J = 2011 - 1 = 2010.
\]  

### Step 3: Solve for \( I \)
Since \( I = J \), we have \( I + I = 2010 \), so \( 2I = 2010 \). Thus, \( I = 1005 \).

### Numerical Approximation
The exact value is an integer, so the numerical approximation is \( 1005.0 \).

{"answer": "1005", "numerical_answer": "1005.0000000000"}