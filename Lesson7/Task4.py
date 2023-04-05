class Matrix:
    def __init__(self, table):
        self.table = table

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.table)

    def __add__(self, other):
        for i in range(len(self.table)):
            for j in range(len(other.table[i])):
                self.table[i][j] = self.table[i][j] + other.table[i][j]
        return Matrix.__str__(self)


if __name__ == '__main__':
    m = Matrix([[31, 32], [37, 43], [51, 58]])
    m_2 = Matrix([[30, 52], [41, 28], [11, 32]])
    print(m.__add__(m_2))
