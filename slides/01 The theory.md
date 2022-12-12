# Projectile Motion

## The question

Considering no air resistance, what is the trajectory followed by a projectile thrown with initial velocity $v_0$ at an angle $\theta$?

<img src="https://github.com/sebastiandres/streamlit_happy_birds/blob/main/images/definition.png?raw=true" alt="Parameter Definition" width="700">


## The short answer

The trajectory followed by a projectile thrown with initial velocity $v_0$ at an angle $\theta$, without air resistance, is:

$$
x(t) = v_0 \cos(\theta)t \\\\
y(t) = v_0 \sin(\theta)t - \frac{1}{2} g t^{2}
$$

where $x$ and $y$ are the horizontal and vertical directions, and $g$ is the acceleration due to gravity.

## The long answer

To obtain the trajectory we start with the equations for the acceleration as given by Newton's Laws:

$$
m \frac{d^{2}}{dt^{2}} x = 0 \\\\
m \frac{d^{2}}{dt^{2}} y = - mg
$$

Initial condition for the position: $x(t=0)=0$ and $y(t=0)=0$.

Initial condition for the velocity: $v_x(t=0) = \cos(\theta)$ and $v_y(t=0) = \sin(\theta)$.

After simplifying for the mass $m$, we can solve by integrating and considering the conditions for velocity: 

$$
\frac{d}{dt}x = v_x(t)= v_0 \cos(\theta) \\\\
\frac{d}{dt}y = v_y(t)= v_0 \sin(\theta) - g t
$$

Integrating again and considering the initial conditions for $x$ and $y$, we obtain:

$$
x(t) = v_0 \cos(\theta)t \\\\
y(t) = v_0 \sin(\theta)t - \frac{1}{2} g t^{2}
$$

## Quiz time

Following the equation above, answer the following question:

stb.single_choice
What is the trajectory of a projectile without considering air resistance?
- A straight line
+ A parabola
- A circle
- A hyperbola

