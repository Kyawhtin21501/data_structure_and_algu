import random 

class sortCL:
    def __init__(self):
        self.data = []

    def input(self, num):
        for i in range(1, num+1):
            x = random.randint(1, 10)
            self.data.append(x)
        return self.data

    def operator(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j] > key:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
        return print(self.data)


sorter = sortCL()
output = sorter.input(10)   
sorted_output = sorter.operator()  
print("Final result:", sorted_output)
