---
type: concept
category: mathematics
defines: ["Partial derivative", "partial derivatives"]
related: ["[[derivative]]", "[[differential-equations]]", "[[optimization-problem]]"]
lists: ["[[calculus-ideas]]"]
read: false
---

# Partial Derivative

## summary

A *partial derivative* of a multivariable function is its derivative with respect to one variable while holding all other variables constant. It measures the rate at which the function changes along the direction of a coordinate axis in multivariable space. Partial derivatives are the fundamental building blocks of multivariable calculus, differential geometry, and mathematical physics.

## you gotta know

- Formally, the partial derivative of f(x, y) with respect to x at (a, b) is defined as the limit of the difference quotient [f(a+h, b) - f(a, b)] / h as h approaches 0.
- It is denoted using the curly-d notation ∂ (e.g., ∂f/∂x) or by subscripts (e.g., f_x); the curly-d symbol was introduced by Adrien-Marie Legendre and later popularized by Carl Gustav Jacob Jacobi.
- *Clairaut's theorem* (also called Schwarz's theorem) states that if the second-order partial derivatives are continuous, the mixed partial derivatives are equal (∂²f/∂x∂y = ∂²f/∂y∂x).
- First-order partial derivatives are collected into the *gradient* vector (∇f), which points in the direction of the greatest rate of increase of the function.
- In vector calculus, the *Jacobian matrix* is the matrix of all first-order partial derivatives of a vector-valued function, representing the best linear approximation to the function at a point.

## connections

- [[derivative]] — partial derivatives extend the single-variable derivative concept to multiple variables.
- [[differential-equations]] — partial differential equations (PDEs) are differential equations that contain partial derivatives.
- [[optimization-problem]] — optimizing multivariable functions requires finding critical points where all partial derivatives vanish.

## see also

- [[derivative]] · [[differential-equations]] · [[optimization-problem]]

<!-- footer -->

---

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
