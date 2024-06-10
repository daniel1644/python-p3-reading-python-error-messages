#!/usr/bin/env python3

# Method 1: Using str() for conversion
wrong_type = 'abc' + str(123)
print(wrong_type)  # Output: abc123

# Method 2: Using f-strings for formatting
wrong_type = f'abc{123}'
print(wrong_type)  # Output: abc123

