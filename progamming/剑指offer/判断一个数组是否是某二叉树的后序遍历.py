def VerifySquenceOfBST(sequence):
    # write code here
    if not sequence:
        return False
    root = sequence[-1]
    i = 0
    while i < len(sequence) - 1:
        if sequence[i] > root:
            break
        i += 1
    j = i
    while j < len(sequence) - 1:
        if sequence[j] < root:
            return False
        j += 1
    left = True
    left = VerifySquenceOfBST(sequence[:i])
    right = True
    right = VerifySquenceOfBST(sequence[i:len(sequence) - 1])
    return left and right
