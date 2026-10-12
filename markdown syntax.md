# Markdown syntax

A practical reference for notes, README files, and Jupyter Markdown cells.
Math examples use LaTeX syntax supported by Jupyter and many Markdown viewers.
Some features, such as math, HTML, and task lists, depend on the viewer.

## 1. Headings

Use `#` followed by a space. More `#` characters mean a smaller heading.

```markdown
# Main heading
## Section
### Subsection
#### Smaller heading
```

## 2. Paragraphs and line breaks

Leave a blank line between paragraphs:

```markdown
This is the first paragraph.

This is the second paragraph.
```

For a line break within the same paragraph, end the line with **two spaces**
before pressing Enter. A normal newline in the source may render as a space.

Alternatively, in viewers that support HTML, use `<br>`:

```markdown
First line.<br>
Second line.
```

For line breaks inside equations, use `\\` within an environment such as
`aligned` (see section 11).

## 3. Bold, italics, and strikethrough

| Formatting | Syntax | Result |
| --- | --- | --- |
| Bold | `**important**` | **important** |
| Italics | `*emphasis*` | *emphasis* |
| Bold and italics | `***both***` | ***both*** |
| Strikethrough | `~~removed~~` | ~~removed~~ |

Strikethrough is a Markdown extension supported by GitHub and many viewers.

For an exercise label, write `**a)**`. Do not add backslashes before the stars
unless you want the stars to appear literally.

## 4. Lists

### Bullet lists

```markdown
- First item
- Second item
  - Nested item
  - Another nested item
```

### Numbered lists

```markdown
1. First step
2. Second step
3. Third step
```

### Task lists

```markdown
- [x] Completed task
- [ ] Remaining task
```

Use blank lines before and after lists. Task lists depend on viewer support.

## 5. Links and images

```markdown
[Link text](https://example.com)
[Another section in this file](#10-inline-and-display-equations)
![Description of the image](figures/example.png)
```

Image paths are relative to the Markdown file. Heading links generally use
lowercase words joined by hyphens, but exact rules depend on the viewer.

For a local filename containing spaces, put the destination inside angle brackets:

```markdown
[My notes](<my notes.md>)
```

## 6. Code

Use single backticks for inline code:

```markdown
Use `W @ x + b` for the layer calculation in NumPy.
```

Use three backticks for a code block. Add a language name for syntax highlighting:

````markdown
```python
import numpy as np

W = np.zeros((10, 4))
x = np.zeros(4)
b = np.zeros(10)
z = W @ x + b
```
````

Code blocks preserve spaces and line breaks. They also display Markdown and
LaTeX literally, which is useful when documenting syntax.

## 7. Quotes

```markdown
> This is a quotation or a note.
>
> This is a second paragraph in the same quote.
```

## 8. Tables

```markdown
| Parameter | Shape | Meaning |
| --- | --- | --- |
| W | (10, 4) | Weights |
| b | (10,) | Bias |
| x | (4,) | One input vector |
```

To align columns, use `:---` for left alignment, `:---:` for centered alignment,
or `---:` for right alignment in the separator row.

Tables are a Markdown extension supported by GitHub and Jupyter.

## 9. Horizontal rules and literal characters

Place `---` on its own line, with blank lines around it, for a horizontal rule:

```markdown
Text above the rule.

---

Text below the rule.
```

Use a backslash to display a Markdown formatting character literally:

```markdown
\*These stars are visible\*
\# This is not a heading
```

Inside equations, use LaTeX commands instead: `\_` for a literal underscore,
`\%` for a percent sign, and `\{` and `\}` for visible braces.

## 10. Inline and display equations

Use single dollar signs for an equation within a sentence:

```markdown
The input is $\mathbf{x} \in \mathbb{R}^{4}$.
```

Use double dollar signs for an equation on its own line:

```markdown
$$
\mathbf{z} = W\mathbf{x} + \mathbf{b}
$$
```

Leave blank lines around display equations for readability and compatibility.

## 11. Multiple equation lines and alignment

Use `aligned` inside `$$ ... $$`. The `\\` command starts a new equation line,
and `&` marks the alignment position.

```markdown
$$
\begin{aligned}
W &\in \mathbb{R}^{10 \times 4} \\
\mathbf{x} &\in \mathbb{R}^{4} \\
\mathbf{b} &\in \mathbb{R}^{10} \\[6pt]
\mathbf{z} &= W\mathbf{x} + \mathbf{b}
\end{aligned}
$$
```

Here, `[6pt]` adds extra vertical space before the last line.

## 12. Spaces in equations

Ordinary spaces inside math are usually ignored. Use explicit commands:

| Command | Effect |
| --- | --- |
| `\,` | Small space |
| `\:` | Medium space |
| `\;` | Larger space |
| `\quad` | Large space |
| `\qquad` | Extra-large space |
| `\!` | Negative space; moves symbols closer together |

```markdown
$$
W \in \mathbb{R}^{10 \times 4}
\qquad
\mathbf{b} \in \mathbb{R}^{10}
$$
```

For words inside an equation, use `\text{...}` so that text and spaces render properly:

```markdown
$$
x > 0 \quad \text{for all positive inputs}
$$
```

## 13. Vectors, matrices, and membership

| Meaning | LaTeX syntax |
| --- | --- |
| Vector with an arrow | `\vec{x}` |
| Bold Latin vector | `\mathbf{x}` |
| Bold Greek symbol | `\boldsymbol{\theta}` |
| Bold matrix | `\mathbf{W}` |
| Transpose | `W^{\mathsf{T}}` |
| Element of | `\in` |
| Not an element of | `\notin` |
| Real numbers | `\mathbb{R}` |
| Four-dimensional real vector space | `\mathbb{R}^{4}` |
| Set braces | `\{0, 1, 2\}` |

```markdown
$$
\mathbf{x} \in \mathbb{R}^{4}
\qquad
W \in \mathbb{R}^{10 \times 4}
$$
```

Use one vector convention consistently: either arrows or bold symbols.

## 14. Subscripts, powers, fractions, and roots

| Meaning | LaTeX syntax |
| --- | --- |
| Subscript | `x_i` |
| Multi-character subscript | `x_{ij}` |
| Power | `x^2` |
| Multi-character exponent | `x^{n+1}` |
| Fraction | `\frac{a}{b}` |
| Square root | `\sqrt{x}` |
| nth root | `\sqrt[n]{x}` |
| Absolute value | `\lvert x \rvert` |
| Euclidean norm | `\lVert \mathbf{x} \rVert_2` |

Braces group characters; they do not appear in the rendered equation.

```markdown
$$
w_{ij}^{(l)} = \frac{x_i}{\sqrt{1 + x_i^2}}
$$
```

## 15. Common mathematical symbols

| Meaning | LaTeX syntax |
| --- | --- |
| Multiplication sign | `\times` |
| Multiplication dot | `\cdot` |
| Less than or equal to | `\leq` |
| Greater than or equal to | `\geq` |
| Not equal to | `\neq` |
| Approximately equal to | `\approx` |
| Right arrow | `\rightarrow` |
| Implies | `\Rightarrow` |
| Infinity | `\infty` |
| For all | `\forall` |
| There exists | `\exists` |
| Alpha, beta, gamma | `\alpha`, `\beta`, `\gamma` |
| Theta, lambda, sigma | `\theta`, `\lambda`, `\sigma` |

For mathematical functions, use commands such as `\log`, `\exp`, and `\sin`
to get upright function names and appropriate spacing.

## 16. Sums, derivatives, and gradients

```markdown
$$
C = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2
$$
```

| Meaning | LaTeX syntax |
| --- | --- |
| Sum | `\sum_{i=1}^{N}` |
| Product | `\prod_{i=1}^{N}` |
| Ordinary derivative | `\frac{dC}{dx}` |
| Partial derivative | `\frac{\partial C}{\partial w_{ij}}` |
| Gradient with respect to W | `\nabla_W C` |
| Predicted value | `\hat{y}` |

Example from a layer with 4 input features and 10 neurons:

```markdown
$$
\begin{aligned}
\frac{\partial C}{\partial W} &\in \mathbb{R}^{10 \times 4} \\
\frac{\partial C}{\partial \mathbf{b}} &\in \mathbb{R}^{10}
\end{aligned}
$$
```

For a scalar cost, each gradient has the same shape as its corresponding parameter.

## 17. Matrices and column vectors

Use `bmatrix` for square brackets. Separate columns with `&` and rows with `\\`.

```markdown
$$
W = \begin{bmatrix}
w_{11} & w_{12} \\
w_{21} & w_{22}
\end{bmatrix}
\qquad
\mathbf{x} = \begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
$$
```

Use `pmatrix` instead for parentheses. For brackets that grow to fit their contents,
use `\left` and `\right`:

```markdown
$$
\left(\frac{a+b}{c}\right)^2
$$
```

## 18. A complete exercise-answer template

```markdown
### Exercise a)

The layer has **10 neurons**, each receiving **4 input features** from one data point.

$$
\begin{aligned}
W &\in \mathbb{R}^{10 \times 4} \\
\mathbf{x} &\in \mathbb{R}^{4} \\
\mathbf{b} &\in \mathbb{R}^{10} \\[6pt]
\mathbf{z} &= W\mathbf{x} + \mathbf{b} \in \mathbb{R}^{10}
\end{aligned}
$$

The gradients have the same shapes as the parameters:

$$
\boxed{\frac{\partial C}{\partial W} \in \mathbb{R}^{10 \times 4}}
\qquad
\boxed{\frac{\partial C}{\partial \mathbf{b}} \in \mathbb{R}^{10}}
$$

In NumPy, the layer calculation is `W @ x + b`.
```

## 19. Common mistakes to avoid

- Use `**bold**`, not `\*\*bold\*\*`, when you want bold formatting.
- Use blank lines between paragraphs; one source newline may not create a visible break.
- Use `\\` inside `aligned` for equation line breaks.
- Use `\quad` or another spacing command when you need extra space in equations.
- Use braces for multi-character subscripts and exponents: `x_{ij}` and `x^{n+1}`.
- Use `\text{...}` for ordinary words inside equations.
- Keep math outside code blocks when you want it rendered.
- In NumPy, `@` means matrix multiplication and `*` means elementwise multiplication.
