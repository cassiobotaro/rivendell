# Roman

I am using Python’s module-level __getattr__ to implement a rich DSL for Roman numerals through dynamic attribute resolution. The logic intercepts numeral strings and simplifies them by replacing subtractive pairs—such as IV or CM—with their additive equivalents (e.g., IIII or DCCCC). Once normalized, the code maps the characters to their respective values and sums them up. This allows the module to treat any valid Roman numeral as a dynamic constant, providing a clean and intuitive syntax for numerical operations.

## ⚠️ Disclaimer

This project was created **just for fun** and for educational purposes to explore Python's meta-programming capabilities.

Please be aware that:
* **No Validation:** The code does not perform any validation on the input strings. It assumes the Roman numerals provided are syntactically correct.
* **Experimental Only:** This is a proof-of-concept for a rich DSL using `__getattr__` and should not be used in production environments or for critical applications.

## How to run

```
uv run python -c "import roman; print(roman.XIV)"
```
