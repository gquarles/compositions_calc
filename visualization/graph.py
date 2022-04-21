import matplotlib.pyplot as plt
import numpy as np
import math

def readnums(file: str):
    f = open(f'data/{file}.txt', 'r')
    lines = f.readlines()
    f.close()

    nums = []
    for line in lines:
        n = line.strip('\n')
        n = n.split(' ')[1]
        nums.append(int(n))
    
    return nums

class SumSet:
    def __init__(self, file):
        self.data = readnums(str(file))

        #Helper array for plotting
        self.x = [i for i in range(0, len(self.data))]
        self.derivative = np.gradient(self.data)
        self.integral = []
        self.integralLog = []
        self.log = []
        self.totalSums = 0
        
        for num in self.data:
            self.totalSums += num
            self.integral.append(self.totalSums)
            
            if num != 0:
                self.log.append(math.log(num))
                self.integralLog.append(math.log(self.totalSums))

#Import all sumsets 1->18
sets = []
for i in range(1, 18):
    sets.append(SumSet(f'{i}'))

plt.xlabel('Summation')
plt.ylabel('Compositions')
#Examples of plotting all imported data
plt.title('Derivatives of lengths 1-17')
for numset in sets:
    plt.plot(numset.derivative)
    #plt.plot(numset.integral)
    #plt.plot(numset.log)
    #plt.plot(numset.integralLog)
    #plt.plot(numset.data)

#Example of plotting only one dataset
#plt.plot(sets[15].integral)
#plt.title('Integral for length = 16')

plt.show()