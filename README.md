# Fast Wordlist Generator 🚀

A high-performance wordlist and password generator that leverages the raw computational speed of **C++** with an easy-to-use **Python** interactive interface. 

Generating millions of string combinations natively in Python can cause high memory usage and slow execution times. This project solves that by offloading the heavy recursive generation and file I/O operations to a compiled C++ shared library, while keeping the user experience simple via Python.

## 🔥 Features

- **Blazing Fast:** C++ core generates and writes millions of combinations in milliseconds.
- **Smart Masking:** Know a part of the password? Use the `?` wildcard (e.g., `admin???24`) to drastically reduce generation time.
- **Flexible Character Sets:** Choose between lowercase, uppercase, digits, special characters, or combine them on the fly.
- **Lightweight:** Zero external dependencies. Uses Python's built-in `ctypes` and standard C++ libraries.

## ⚙️ Prerequisites

- [**Python 3.x**](https://www.python.org/downloads/release/python-3147/)
- [**C++ Compiler** (e.g., `g++` / MinGW for Windows, or Clang/GCC for macOS and Linux)](https://jmeubank.github.io/tdm-gcc/)

## 🛠️ Build & Installation

Before running the Python script, you must compile the C++ core (`generator.cpp`) into a shared library. Open your terminal in the project directory and run the command corresponding to your operating system:

**For Windows:**
```bash
g++ -shared -o libgen.dll generator.cpp
```
**For macOS / Linux:**
```bash
g++ -shared -fPIC -o libgen.so generator.cpp
```

## 🚀 Usage
Once the shared library (.dll or .so) is generated in the same directory, run the Python interface:

```bash
python main.py
```

---
## Example Workflow:

=== Fast Wordlist Generator (C++ Powered) ===
Enter the password pattern (use '?' for unknown, e.g., a??5): P@ss???

Which character sets to test in '?' positions? (e.g., 13)
1. Lowercase (a-z)
2. Uppercase (A-Z)
3. Digits (0-9)
4. Special Characters (!@#$%^&*)

Your choice: 13

Generating wordlist...
Pattern: P@ss???
Testing 36 characters per unknown position...

✅ Done! Words saved in 'passwords.txt'.
⏱️ Processing time: 0.0412 seconds



