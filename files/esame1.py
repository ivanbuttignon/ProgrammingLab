class ExamException(Exception):
    pass

class MovingAverage():

    def __init__(self, fin):
        self.fin = fin #lunghezza fin.
        if self.fin == None: 
            raise ExamException('error')
        if type(self.fin) != int:
            raise ExamException('error')
        if self.fin <= 0:
            raise ExamException('error')

    def compute(self, mylist):
        if type(mylist) != list:
            raise ExamException('error')
        if mylist == None:
            raise ExamException('error')
        if self.fin > len(mylist):
            raise ExamException('error')
        if mylist == []:
            raise ExamException('error')
        result = []
        for i in range (0, len(mylist) -         self.fin + 1):
            sum = 0
            for j in range (self.fin):
                sum = sum + mylist[i+j]
            avg = sum/self.fin
            result.append(avg)
        return result


moving_average = MovingAverage(2)
res = moving_average.compute([2,4,8,16])
print(res)