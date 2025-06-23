# Evaluating $\int\limits_0^1x\arcsin x\arccos x\:dx$

I'll compute this definite integral analytically, showing all the necessary steps.

## Step 1: Recall the relationship between arcsin and arccos
First, note that $\arcsin x + \arccos x = \frac{\pi}{2}$ for all $x \in [0,1]$

Therefore:
$\arccos x = \frac{\pi}{2} - \arcsin x$

## Step 2: Substitute this relationship into our integral
\begin{align}
\int\limits_0^1 x\arcsin x\arccos x\:dx &= \int\limits_0^1 x\arcsin x \left(\frac{\pi}{2} - \arcsin x\right) dx\\
&= \int\limits_0^1 x\arcsin x \cdot \frac{\pi}{2} \:dx - \int\limits_0^1 x(\arcsin x)^2 \:dx\\
&= \frac{\pi}{2}\int\limits_0^1 x\arcsin x \:dx - \int\limits_0^1 x(\arcsin x)^2 \:dx
\end{align}

## Step 3: Calculate each integral separately

### For $\frac{\pi}{2}\int\limits_0^1 x\arcsin x \:dx$:
Let's use integration by parts with:
- $u = \arcsin x$
- $dv = x\:dx$
- $du = \frac{1}{\sqrt{1-x^2}}\:dx$
- $v = \frac{x^2}{2}$

\begin{align}
\int x\arcsin x \:dx &= \frac{x^2}{2}\arcsin x - \int \frac{x^2}{2} \cdot \frac{1}{\sqrt{1-x^2}}\:dx\\
&= \frac{x^2}{2}\arcsin x - \frac{1}{2}\int \frac{x^2}{\sqrt{1-x^2}}\:dx
\end{align}

For the remaining integral, I'll use substitution $x = \sin t$, which gives $dx = \cos t\:dt$:
\begin{align}
\int \frac{x^2}{\sqrt{1-x^2}}\:dx &= \int \frac{\sin^2 t}{\sqrt{1-\sin^2 t}} \cos t\:dt\\
&= \int \frac{\sin^2 t}{\cos t} \cos t\:dt\\
&= \int \sin^2 t\:dt\\
&= \int \frac{1-\cos 2t}{2}\:dt\\
&= \frac{t}{2} - \frac{\sin 2t}{4} + C
\end{align}

Substituting back $t = \arcsin x$, so $\sin 2t = 2\sin t\cos t = 2x\sqrt{1-x^2}$:
\begin{align}
\int \frac{x^2}{\sqrt{1-x^2}}\:dx &= \frac{\arcsin x}{2} - \frac{x\sqrt{1-x^2}}{2} + C
\end{align}

Now, returning to our integration by parts:
\begin{align}
\int x\arcsin x \:dx &= \frac{x^2}{2}\arcsin x - \frac{1}{2}\left(\frac{\arcsin x}{2} - \frac{x\sqrt{1-x^2}}{2}\right) + C\\
&= \frac{x^2}{2}\arcsin x - \frac{\arcsin x}{4} + \frac{x\sqrt{1-x^2}}{4} + C\\
\end{align}

Now, evaluating the definite integral:
\begin{align}
\int\limits_0^1 x\arcsin x \:dx &= \left[\frac{x^2}{2}\arcsin x - \frac{\arcsin x}{4} + \frac{x\sqrt{1-x^2}}{4}\right]_0^1\\
&= \left[\frac{1^2}{2}\arcsin 1 - \frac{\arcsin 1}{4} + \frac{1\sqrt{1-1^2}}{4}\right] - \left[\frac{0^2}{2}\arcsin 0 - \frac{\arcsin 0}{4} + \frac{0\sqrt{1-0^2}}{4}\right]\\
&= \left[\frac{\pi}{4} - \frac{\pi}{8} + 0\right] - [0]\\
&= \frac{\pi}{4} - \frac{\pi}{8}\\
&= \frac{\pi}{8}
\end{align}

Therefore, $\frac{\pi}{2}\int\limits_0^1 x\arcsin x \:dx = \frac{\pi}{2} \cdot \frac{\pi}{8} = \frac{\pi^2}{16}$

### For $\int\limits_0^1 x(\arcsin x)^2 \:dx$:
Let's use integration by parts again with:
- $u = (\arcsin x)^2$
- $dv = x\:dx$
- $du = 2\arcsin x \cdot \frac{1}{\sqrt{1-x^2}}\:dx$
- $v = \frac{x^2}{2}$

\begin{align}
\int x(\arcsin x)^2 \:dx &= \frac{x^2}{2}(\arcsin x)^2 - \int \frac{x^2}{2} \cdot 2\arcsin x \cdot \frac{1}{\sqrt{1-x^2}}\:dx\\
&= \frac{x^2}{2}(\arcsin x)^2 - \int \frac{x^2 \arcsin x}{\sqrt{1-x^2}}\:dx
\end{align}

This becomes complex. Let's approach differently.

Let me try substitution $x = \sin t$, which gives $dx = \cos t\:dt$ and $\arcsin x = t$:
\begin{align}
\int x(\arcsin x)^2 \:dx &= \int \sin t \cdot t^2 \cdot \cos t\:dt\\
&= \int t^2 \sin t \cos t\:dt\\
&= \frac{1}{2}\int t^2 \sin 2t\:dt
\end{align}

Using integration by parts with $u = t^2$ and $dv = \sin 2t\:dt$:
\begin{align}
\int t^2 \sin 2t\:dt &= -\frac{t^2 \cos 2t}{2} + \int \frac{2t \cos 2t}{2}\:dt\\
&= -\frac{t^2 \cos 2t}{2} + \int t \cos 2t\:dt
\end{align}

For $\int t \cos 2t\:dt$, let's use integration by parts again with $u = t$ and $dv = \cos 2t\:dt$:
\begin{align}
\int t \cos 2t\:dt &= t \cdot \frac{\sin 2t}{2} - \int \frac{\sin 2t}{2}\:dt\\
&= \frac{t\sin 2t}{2} - \frac{-\cos 2t}{4} + C\\
&= \frac{t\sin 2t}{2} + \frac{\cos 2t}{4} + C
\end{align}

Combining the results:
\begin{align}
\int t^2 \sin 2t\:dt &= -\frac{t^2 \cos 2t}{2} + \frac{t\sin 2t}{2} + \frac{\cos 2t}{4} + C
\end{align}

And our original integral:
\begin{align}
\int x(\arcsin x)^2 \:dx &= \frac{1}{2}\left(-\frac{t^2 \cos 2t}{2} + \frac{t\sin 2t}{2} + \frac{\cos 2t}{4}\right) + C\\
&= -\frac{t^2 \cos 2t}{4} + \frac{t\sin 2t}{4} + \frac{\cos 2t}{8} + C
\end{align}

Substituting back $t = \arcsin x$, $\sin t = x$, $\cos t = \sqrt{1-x^2}$:
\begin{align}
\sin 2t &= 2\sin t \cos t = 2x\sqrt{1-x^2}\\
\cos 2t &= \cos^2 t - \sin^2 t = 1-2\sin^2 t = 1-2x^2
\end{align}

So:
\begin{align}
\int x(\arcsin x)^2 \:dx &= -\frac{(\arcsin x)^2(1-2x^2)}{4} + \frac{\arcsin x \cdot 2x\sqrt{1-x^2}}{4} + \frac{1-2x^2}{8} + C\\
&= -\frac{(\arcsin x)^2}{4} + \frac{x^2(\arcsin x)^2}{2} + \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} + \frac{1}{8} - \frac{x^2}{4} + C
\end{align}

Evaluating the definite integral:
\begin{align}
\int\limits_0^1 x(\arcsin x)^2 \:dx &= \left[-\frac{(\arcsin x)^2}{4} + \frac{x^2(\arcsin x)^2}{2} + \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} + \frac{1}{8} - \frac{x^2}{4}\right]_0^1\\
\end{align}

At $x = 1$: $\arcsin 1 = \frac{\pi}{2}$, $\sqrt{1-1^2} = 0$
At $x = 0$: $\arcsin 0 = 0$, $\sqrt{1-0^2} = 1$

\begin{align}
\int\limits_0^1 x(\arcsin x)^2 \:dx &= \left[-\frac{(\pi/2)^2}{4} + \frac{1^2(\pi/2)^2}{2} + \frac{(\pi/2) \cdot 1 \cdot 0}{2} + \frac{1}{8} - \frac{1^2}{4}\right] - \left[-\frac{0^2}{4} + \frac{0^2 \cdot 0^2}{2} + \frac{0 \cdot 0 \cdot 1}{2} + \frac{1}{8} - \frac{0^2}{4}\right]\\
&= \left[-\frac{\pi^2}{16} + \frac{\pi^2}{8} + 0 + \frac{1}{8} - \frac{1}{4}\right] - \left[0 + 0 + 0 + \frac{1}{8} - 0\right]\\
&= -\frac{\pi^2}{16} + \frac{\pi^2}{8} + \