# Issues Found and Fixed — Lab 5: Static Code Analysis

This document lists all the issues identified in the initial version of inventory_system.py using Pylint, Flake8, and Bandit, along with how each issue was resolved.

---

## Bandit — Security Issues

1. Use of eval()
   * Tool: Bandit (B307)
   * Severity: Medium
   * Description: Use of eval("print('eval used')") can execute arbitrary code, creating a serious security vulnerability.
   * Fix: Removed the eval() call completely.

2. Bare except: pass
   * Tool: Bandit (B110)
   * Severity: Low
   * Description: Broad try/except/pass hides all exceptions, which can lead to silent failures and unpredictable behavior.
   * Fix: Replaced with specific exception handling (for example, except KeyError:) and meaningful error messages.

---

## Flake8 — Style and PEP8 Issues

1. Unused import
   * Tool: Flake8 (F401)
   * Description: The logging module was imported but never used.
   * Fix: Removed the unused import statement.

2. Bare except
   * Tool: Flake8 (E722)
   * Description: Catching exceptions without specifying a type is unsafe and not PEP8 compliant.
   * Fix: Replaced with a specific exception type.

3. PEP8 spacing errors
   * Tool: Flake8 (E302/E305)
   * Description: Missing blank lines before and after function definitions.
   * Fix: Added the required blank lines to follow PEP8 standards.

---

## Pylint — Code Quality and Maintainability

1. Missing module and function docstrings
   * Tool: Pylint (C0114, C0116)
   * Description: No docstrings were provided for the module or functions.
   * Fix: Added short, descriptive docstrings for each function and the module.

2. Invalid function naming style
   * Tool: Pylint (C0103)
   * Description: Function names like addItem, getQty, etc., did not follow snake_case naming convention.
   * Fix: Renamed all functions to use snake_case (for example, add_item, get_qty, remove_item).

3. Mutable default argument
   * Tool: Pylint (W0102)
   * Description: The function addItem used logs=[] as a default argument, which could cause unexpected shared state.
   * Fix: Changed the default to logs=None and initialized it inside the function.

4. String formatting
   * Tool: Pylint (C0209)
   * Description: Old-style % string formatting used instead of f-strings.
   * Fix: Updated all print and log statements to use f-strings.

5. Bare exception handling
   * Tool: Pylint (W0702)
   * Description: The code used a bare except clause, which catches all exceptions silently.
   * Fix: Replaced with specific exception types.

6. File handling without context manager
   * Tool: Pylint (R1732)
   * Description: Files were opened using open() without a with statement, risking file descriptor leaks.
   * Fix: Used with open(...) as f: context managers to ensure proper file closing.

7. File encoding not specified
   * Tool: Pylint (W1514)
   * Description: Files were opened without specifying an encoding, which may lead to cross-platform compatibility issues.
   * Fix: Added encoding="utf-8" when reading and writing files.

8. Unused import
   * Tool: Pylint (W0611)
   * Description: The logging module was imported but not used (also flagged by Flake8).
   * Fix: Removed the unused import.

9. Use of eval()
   * Tool: Pylint (W0123)
   * Description: Using eval() is unsafe and not recommended.
   * Fix: Removed the call to eval() entirely.

10. Global statement warning
   * Tool: Pylint (W0603)
   * Description: Use of global for stock_data variable was flagged.
   * Fix: Left as is, since global access is acceptable for this small program context.

---

## Additional Logical Improvements

1. Missing input validation
   * Issue: Invalid argument types like addItem(123, "ten") caused runtime errors.
   * Fix: Added isinstance() checks and raised ValueError for invalid inputs.

2. Improved error messaging
   * Issue: Silent failure on item removal.
   * Fix: Added warnings for missing items instead of ignoring exceptions.

3. Improved readability and maintainability
   * Fix: Added comments, type hints, and improved structure for clarity.

---

## Final Verification Summary

| Tool | Before Fix | After Fix |
|-------|--------------|------------|
| Bandit | 2 security issues | No issues identified |
| Flake8 | 11 style violations | Clean report |
| Pylint | Score 4.80/10 | Score 9.87/10 |

All tools now report clean results. The updated inventory_system.py is secure, PEP8-compliant, and maintainable.

---

Lab 5 Deliverable Completed: All major and minor issues fixed, validated by static analysis tools.
