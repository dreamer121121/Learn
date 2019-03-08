def insert_sort(elements, flags=True):
    if flags:
        for j in range(1, len(elements)):
            key = elements[j]
            i = j - 1
            while i >= 0 and elements[i] > key:  # 倒序还是正序排列的主要取决于这一条件
                elements[i + 1] = elements[i]
                i -= 1
            elements[i+1] = key
    else:
        for j in range(1, len(elements)):
            key = elements[j]
            i = j - 1
            while i >= 0 and elements[i] < key:  # 倒序还是正序排列的主要取决于这一条件
                elements[i + 1] = elements[i]
                i -= 1
            elements[i+1] = key

    return elements


if __name__ == '__main__':
    unsort_list = [31, 41, 59, 26, 41, 58]
    print(insert_sort(unsort_list, flags=False))
