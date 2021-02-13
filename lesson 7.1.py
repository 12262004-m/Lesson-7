class Matrix:
    def __init__(self,list):
        self.list = list
    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        new_list = []
        for i in range(len(self.list)):
            new_list.append([])
            for j in range(len(self.list([0]))):
                sum = self.list[i][j] + other.list[i][j]
                new_list[i].append(sum)
        return '\n'.join(map(str, new_list))

                
first = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
second = [[24, 23, 22, 21], [17, 16, 15, 14], [10, 9, 8, 7]]
m1 = Matrix(first)
m2 = Matrix(second)
print(m1)
print(m2)
print(m1+m2)
