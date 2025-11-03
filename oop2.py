class CustomRange:
    def __init__(self,start=0,stop=None,step=1):
        self.start=start
        if stop is None:
            stop = start
            start = 0        
        self.step=step
        self.stop = stop
        self.current=self.start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step>0 and self.current>= self.stop) or (self.step<0 and self.current<=self.stop):
            raise StopIteration

        value =self.current

        self.current+= self.step
        return value

    def reset(self):
        self.current= self.start
    


print("Custom Range 0 to 10:")
for num in CustomRange(10):
    print(num, end=" ")
# Output: 0 1 2 3 4 5 6 7 8 9

print("\n\nCustom Range 5 to 15, step 2:")
for num in CustomRange(5, 15, 2):
    print(num, end=" ")

print("\n\nCustom Range 10 to 0, step -2:")
for num in CustomRange(10, 0, -2):
    print(num, end=" ")

print("\n\nFloat step - 0 to 2, step 0.5:")
for num in CustomRange(0, 2, 0.5):
    print(num, end=" ")
