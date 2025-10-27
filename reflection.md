# Reflection - Lab 5: Static Code Analysis

1. Which issues were the easiest to fix, and which were the hardest? Why?

* The easiest issues to fix were the style and formatting problems reported by Flake8, such as missing blank lines and unused imports. These required only minor edits to improve readability and PEP 8 compliance.  
   The hardest issues to fix were the ones related to security and logic, particularly the use of eval() and the mutable default argument. Removing eval() required restructuring the main block to preserve functionality safely, while the mutable default argument issue needed an understanding of how Python handles function defaults. Both required deeper reasoning beyond simple syntax correction.

2. Did the static analysis tools report any false positives? If so, describe one example.
*  One possible false positive came from Pylint’s warning about using the global statement for the variable stock_data. In this case, the global variable was intentional and necessary to maintain shared program state within a simple script, so the warning was not a real design flaw for this scale of application.

3. How would you integrate static analysis tools into your actual software development workflow?
*  Static analysis tools can be integrated into the development process through continuous integration pipelines. Tools like Pylint, Bandit, and Flake8 can be configured to run automatically on every commit or pull request using GitHub Actions or other CI services. This ensures that code quality, security, and style standards are enforced before merging changes into the main branch. Additionally, developers can run these tools locally before committing to detect and fix issues early.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

*  After applying all fixes, the code became significantly more structured, readable, and maintainable. The removal of unsafe functions like eval() improved security, while the addition of type checks and context managers increased robustness. The adherence to PEP 8 standards and the use of f-strings improved consistency and readability. The Pylint score increased from 4.80 to 9.87, and both Bandit and Flake8 reports became clean, confirming measurable improvement in quality and security.
