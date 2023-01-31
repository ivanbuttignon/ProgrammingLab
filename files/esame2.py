class ExamException(Exception):
    pass

class Diff():
    def __init__(self, ratio=1):
        self.ratio = ratio
        if self.ratio == None: 
            raise ExamException('error')
        if self.ratio <= 0:
            raise ExamException('error')
    def compute(self, mylist):
        if mylist == None:
            raise ExamException('error')
        if type(mylist) != list:
            raise ExamException('error')
        if mylist == []:
            raise ExamException('error')
        if len(mylist) == 1:
            raise ExamException('error')
        result = []
        for i in range (len(mylist)-1):
            try:
                dif = mylist[i+1] -    mylist[i]
            except:
                raise ExamException('error')
            result.append(dif)
        for j in range(len(result)):
            try:
                result[j] =    result[j]/self.ratio
            except:
                raise ExamException('error')
        return result

diff = Diff(2)
res = diff.compute([2,4,8,16])
print(res)