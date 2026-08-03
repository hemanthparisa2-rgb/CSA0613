def string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    for i in range(n - m + 1):
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
            matches.append(i)

    return matches
text = "ABABABCABAB"
pattern = "ABAB"
print("Text :", text)
print("Pattern :", pattern)
print("Pattern Found At Index:", string_match(text, pattern))
