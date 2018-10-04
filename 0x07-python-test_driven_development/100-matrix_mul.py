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
    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_a == [[]]:
        raise ValueError("m_b can't be empty")
    length_a = len(m_a[0])
    out = []
    
