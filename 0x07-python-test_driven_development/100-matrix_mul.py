#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if m_a is None:
        raise TypeError("m_a must be a list")
    if m_b is None:
        raise TypeError("m_b must be a list")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    try:
        if not isinstance(m_a[0], list):
            raise TypeError("m_a must be a list of lists")
    except:
        raise TypeError("m_a must be a list of lists")
    try:
        if not isinstance(m_b[0], list):
            raise TypeError("m_b must be a list of lists")
    except:
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    out = []
    crnt = 0
    for i in range(0, len(m_b)):
        for j in range(0, len(m_b[i])):
            if (not isinstance(m_b[i][j], int)
            and not isinstance(m_b[i][j], float)):
                raise TypeError("m_b should contain only integers or floats")
    for i in range(0, len(m_a)):
        for j in range(0, len(m_a[i])):
            if (not isinstance(m_a[i][j], int)
            and not isinstance(m_a[i][j], float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in range(0, len(m_b)):
        if len(m_b[0]) != len(m_b[i]):
            raise TypeError("each row of m_b must should be of the same size")
    for i in range(0, len(m_a)):
        if len(m_a[0]) != len(m_a[i]):
            raise TypeError("each row of m_a must should be of the same size")
    if (len(m_a) > len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(0, len(m_a)):
        out1 = []
        for j in range(0, len(m_b[i])):
            crnt = 0
            for k in range(0, len(m_a[i])):
                crnt += m_a[i][k] * m_b[k][j]
            out1.append(crnt)
        out.append(out1)
    return out
