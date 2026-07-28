# Brute Force String Matching Algorithm

def string_match(text, pattern):
    # Length of text and pattern
    n = len(text)
    m = len(pattern)

    # List to store all matching positions
    matches = []

    # Check every valid starting position
    for i in range(n - m + 1):

        # Compare pattern with text
        for j in range(m):

            # Stop if characters do not match
            if text[i + j] != pattern[j]:
                break

        # If all characters matched
        else:
            matches.append(i)

    return matches


# Sample Input
text = "ABABABCABAB"
pattern = "ABAB"

# Display Output
print("Text :", text)
print("Pattern :", pattern)
print("Pattern Found At Index:", string_match(text, pattern))
