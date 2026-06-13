---
type: concept
category: mathematics
defines: ["Differential Equations", "differential equation"]
related: ["[[derivative]]", "[[integral]]", "[[separation-of-variables]]"]
lists: ["[[calculus-ideas]]"]
read: false
---

# Differential Equations

## summary

A *differential equation* is an equation involving a function and its derivatives. Solutions to differential equations are functions (not numbers) that satisfy the equation for all x in some domain. Differential equations appear across science and engineering because rates of change (derivatives) govern so much of the natural world: population growth, radioactive decay, heat flow, and planetary motion are all modeled by differential equations. An *ordinary differential equation* (ODE) involves derivatives of a function of one variable; a *partial differential equation* (PDE) involves partial derivatives.

## you gotta know

### Types and Order
- *Ordinary differential equation (ODE)*: involves y'(x), y''(x), etc., where y is a function of x only.
- *Partial differential equation (PDE)*: involves partial derivatives ∂y/∂x, ∂y/∂t, etc.
- The *order* of a differential equation is the highest derivative that appears (e.g., y' + 2y = 0 is order 1; y'' + y = cos(x) is order 2).

### Classic Examples
- Exponential growth/decay: dy/dt = ky, with solution y(t) = Ce^(kt).
- Harmonic oscillator: d²y/dt² + ω²y = 0, solution: y(t) = A·cos(ωt) + B·sin(ωt).
- Newton's second law: F = ma = m(d²x/dt²); relates force to acceleration.

### Solution Techniques
- *Separation of variables*: rearrange dy/dx = f(x,y) to isolate y on one side and x on the other, then integrate both sides.
- *Integrating factor*: for linear first-order ODEs, multiply by an integrating factor to make the left side a derivative.
- *Characteristic equation*: for linear ODEs with constant coefficients, substitute y = e^(rx) to get a polynomial in r.

## context

Differential equations are the language of mathematical modeling. Nearly every quantitative science—physics, chemistry, biology, economics—relies on them. The ability to set up and solve a differential equation is a core skill in applied mathematics. Beginners often tackle first-order separable equations and linear equations with constant coefficients; advanced practitioners work with systems of ODEs, PDEs, and numerical approximations. In quiz bowl, differential equations questions test whether you can recognize a solution form, apply separation of variables, or interpret a differential equation statement (e.g., "what does dy/dt = –ky tell you about y?").

## connections

- [[derivative]] — differential equations are built from derivatives.
- [[integral]] — solving differential equations often requires integration (via separation of variables or integrating factors).
- [[separation-of-variables]] — a key technique for solving first-order separable ODEs.
- [[exponential-function]] — e^x appears in solutions to exponential growth/decay equations.

## see also

- [[derivative]] · [[integral]] · [[separation-of-variables]]

<!-- footer -->

---

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
