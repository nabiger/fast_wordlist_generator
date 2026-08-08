import ctypes
import os
import sys
import time
import string

def main():
    # 1. Locate the compiled C++ shared library
    # Get the absolute path of the directory containing this Python script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Determine the correct library file extension based on the operating system
    if sys.platform.startswith('win'):
        lib_name = 'libgen.dll'  # Windows
    else:
        lib_name = 'libgen.so'   # macOS and Linux
        
    lib_path = os.path.join(current_dir, lib_name)
    
    # Check if the compiled library exists before proceeding
    if not os.path.exists(lib_path):
        print(f"Error: The file '{lib_name}' was not found!")
        print("Please compile the C++ source code first.")
        return

    # 2. Load the C++ shared library into Python using ctypes
    generator_lib = ctypes.CDLL(lib_path)

    # 3. Define the argument types and return type for the C++ function
    # C++ Function Signature: 
    # void create_wordlist_mask(const char* mask, const char* charset, const char* output_filename)
    generator_lib.create_wordlist_mask.argtypes = [
        ctypes.c_char_p,  # mask (pattern)
        ctypes.c_char_p,  # chars (character set)
        ctypes.c_char_p   # output_filename
    ]
    # Set the return type to None since the C++ function returns void
    generator_lib.create_wordlist_mask.restype = None

    # 4. Interactive User Menu
    print("=== Fast Wordlist Generator (C++ Powered) ===")
    
    # Get the pattern mask from the user
    mask = input("Enter the password pattern (use '?' for unknown, e.g., a??5): ")
    
    # Menu for character set selection
    print("\nWhich character sets should be tested in the '?' positions?")
    print("You can combine multiple choices (e.g., 13)")
    print("1. Lowercase letters (a-z)")
    print("2. Uppercase letters (A-Z)")
    print("3. Digits (0-9)")
    print("4. Special characters (!@#$%^&*)")
    
    choices = input("\nYour choice: ")
    
    # Build the final character set based on user input
    chars = ""
    if "1" in choices:
        chars += string.ascii_lowercase
    if "2" in choices:
        chars += string.ascii_uppercase
    if "3" in choices:
        chars += string.digits
    if "4" in choices:
        chars += string.punctuation

    # Validate that at least one character set was selected
    if not chars:
        print("Error: No character sets were selected. Exiting...")
        return

    output_file = "passwords.txt"

    # Display processing information
    print(f"\nGenerating wordlist...")
    print(f"Pattern: {mask}")
    print(f"Testing {len(chars)} characters per unknown position...")
    
    # Record the start time to calculate total processing time
    start_time = time.time()

    # 5. Execute the heavy lifting in C++
    # Note: Python strings must be encoded to bytes ('utf-8') before passing them to C++ pointers
    generator_lib.create_wordlist_mask(
        mask.encode('utf-8'), 
        chars.encode('utf-8'), 
        output_file.encode('utf-8')
    )

    # Record the end time
    end_time = time.time()
    
    # 6. Display results
    print(f"\n[OK] Done! Generated words are successfully saved in '{output_file}'.")
    print(f"[TIME] Total processing time: {end_time - start_time:.4f} seconds")

# Ensure the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()
