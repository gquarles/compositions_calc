import matplotlib.pyplot as plt
import numpy as np
import math

def readnums(file):
    f = open(f'data/{file}.txt', 'r')

    lines = f.readlines()
    nums = []
    for line in lines:
        n = line.strip('\n')
        n = n.split(' ')[1]
        nums.append(int(n))
        
    f.close()

    return nums

class SumSet:
    def __init__(self, file):
        self.data = readnums(file)

        integral = []
        integralArea = 0
        log = []
        for num in self.data:
            integralArea += num
            integral.append(integralArea)
            if num != 0:
                log.append(math.log(num))

        integralLog = []
        for num in integral:
            if num != 0:
                integralLog.append(math.log(num))
        
        x = []
        for i in range(0, len(self.data)):
            x.append(i + 1)

        self.log = log
        self.x = x
        self.integralLog = integralLog
        self.integralLogTotal = math.log(integralArea)
        self.integral = integral
        self.integralArea = integralArea
        self.derivative = np.gradient(self.data)
    

sets = []
for i in range(1, 18):
    sets.append(SumSet(f'{i}'))

for i, numset in enumerate(sets):
    i = i + 1
    #plt.plot(numset.integral)

d = []
for i, num in enumerate(sets[13].integral):
    d.append(sets[14].integral[i] + sets[13].integral[i])



#plt.plot(sets[15].integral)
#plt.plot(d)


plt.plot(np.gradient(d))
#plt.plot(sets[16].data)
plt.plot(sets[15].data)
plt.plot(sets[14].data)

#plt.plot(sets[16].derivative)

plt.show()