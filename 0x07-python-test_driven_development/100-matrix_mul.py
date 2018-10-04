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
    out = []
    crnt = 0
    for i in range(0, len(m_a)):
        out1 = []
        for j in range(0, len(m_b[i])):
            crnt = 0
            for k in range(0, len(m_a[i])):
                crnt += m_a[i][k] * m_b[k][j]
            out1.append(crnt)
        out.append(out1)
    return out







#    for i in range(0, len(m_a)):
 #       out1 = []
  #      if len(m_a[0]) != len(m_a[i]):
   #         raise TypeError("each row of m_a must should be of the same size")
    #    for j in range(0, len(m_a[i])):
     #       if not isinstance(m_a[i][j], int) and
      #      not isinstance(m_a[i][j], float):
       #         raise TypeError("m_a should contain only integers or floats")
        #    for k in range(0, len(m_b)):
         #       if not isinstance(m_b[k][j], int) and
          #      not isinstance(m_b[k][j], float):
           #         raise TypeError("m_b should contain only integers or "
            #                        "floats")
                
