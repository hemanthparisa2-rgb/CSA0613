count = 0

def merge_sort(a):
    global count

    if len(a) > 1:
        mid = len(a)//2
        L = a[:mid]
        R = a[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            count += 1

            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1

a = [12,4,78,23,45,67,89,1]
merge_sort(a)

print("Sorted:", a)
print("Comparisons:", count)