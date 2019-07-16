
def isNumeric(s):
    count_pos = s.count('+')
    count_neg = s.count('-')
    count_dot = s.count('.')
    if 'e' in s or 'E' in s:
        count_E = s.count('e')
        count_e = s.count('E')
        if count_E and count_e:
            return False
        if count_E > 1 or count_e >1:
            return False
        else:
            if 'e' in s:
                index_e = s.index('e')
                if s[index_e+1] == '+':
                    return  False
            elif 'E' in s:
                index_E = s.index('E')
                if s[index_E+1] == '+':
                    return False
            if count_dot:
                if count_dot > 1:
                    return False
                elif s[0] == '.':
                    return False
                else:
                    if count_pos > 0 or count_neg > 0:
                        if count_pos and count_neg:
                            return False
                        if count_pos > 1 or count_neg > 1:
                            return False
                        if s[0] != '+' and s[0] != '-':
                            return False

            else:
                if count_pos > 0 or count_neg > 0:
                    if count_pos > 0 and count_neg > 0:
                        return False
                    if count_pos > 1 or count_neg > 1:
                        return False
                    if s[0] != '+' and s[0] != '-':
                        return False

    else:
        if count_dot:
            if count_dot >1:
                return False
            elif s[0] == '.':
                return False
            else:
                if count_pos > 0 or count_neg >0:
                    if count_pos and count_neg:
                        return False
                    if count_pos> 1 or count_neg > 1:
                        return False
                    if s[0] != '+' and s[0] != '-':
                        return False
        else:
            if count_pos> 0 or count_neg >0:
                if count_pos> 0 and count_neg > 0:
                    return False
                if count_pos> 1 or count_neg > 1:
                    return False
                if s[0] != '+' and  s[0] != '-':
                    return False
            else:#没有E没有.也没有'+'和'-'
                return s.isdigit()
    return True

print(isNumeric('123.45e+6'))
