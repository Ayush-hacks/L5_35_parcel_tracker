\# Lab 5: Static Code Analysis



\## Issue Documentation



| Issue | Type | Description | Fix Applied |

|---|---|---|---|

| Mutable default argument | Bug | The default history list was shared between function calls. | Changed the default argument to `None` and initialized the list inside the function. |

| Broad exception handling | Code quality | Catching all exceptions could hide unexpected programming errors. | Used dictionary lookup and explicitly handled an unknown tracking ID. |

| Unsafe temporary file creation | Security | `tempfile.mktemp()` could create a race condition. | Replaced it with `tempfile.mkstemp()` and closed the file descriptor. |

| Unsafe subprocess helper | Security | The original helper used shell command execution with user-controlled input. | Removed the unused subprocess helper and its import. |

| OTP generation | Security | The `random` module was not suitable for generating security-sensitive tokens. | Replaced it with `secrets.randbelow()`. |

| Missing documentation | Code quality | The module and main function lacked docstrings. | Added descriptive docstrings. |

| Code formatting | Style | Inconsistent spacing and naming reduced readability. | Standardized formatting and used snake\_case names. |



\## Verification



The source code was analyzed using Pylint, Bandit, and Flake8 before and after the changes. The final reports were reviewed to verify the results.



\## Reflection



\### 1. What is static code analysis?



Static code analysis examines source code without executing the program. It helps identify potential bugs, security issues, and style violations.



\### 2. What are the purposes of Pylint, Bandit, and Flake8?



Pylint checks code quality and potential programming mistakes. Bandit identifies potentially insecure coding patterns. Flake8 checks Python style and formatting.



\### 3. What issues were fixed?



The assignment addressed a mutable default argument, broad exception handling, unsafe temporary-file creation, unnecessary subprocess usage, OTP generation, and documentation and formatting issues.



\### 4. What are the benefits of static analysis?



Static analysis helps identify problems early, improves readability and maintainability, and can reduce security risks.



\### 5. What are its limitations?



Static analysis cannot guarantee that a program is completely correct or secure. Runtime testing and code review are also necessary.

