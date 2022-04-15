class Temperature: 
_celsius = None 
_fahrenheit = None 
@property 
def celsius(self): 
return self._celsius 
@celsius.setter 
def celsius(self, value): 
self._celsius = float(value) 
self._fahrenheit = self.to_fahrenheit(self._celsius) 
@property 
def fahrenheit(self): 
return self._fahrenheit 
@fahrenheit.setter 
480 | Python Examples
def fahrenheit(self, value): 
self._fahrenheit = float(value) 
self._celsius = self.to_celsius(self._fahrenheit) 
def __init__(self, celsius=None, fahrenheit=None): 
if celsius != None: 
self._celsius = celsius 
self._fahrenheit = self.to_fahrenheit(celsius) 
if fahrenheit != None: 
self._fahrenheit = fahrenheit 
self._celsius = self.to_celsius(fahrenheit) 
def to_celsius(self, fahrenheit): 
return (fahrenheit - 32) * 5 / 9 
def to_fahrenheit(self, celsius): 
return celsius * 9 / 5 + 32 
# This program creates instances of the Temperature class to convert Cesius 
# and Fahrenheit temperatures. 
def main(): 
temp1 = Temperature(celsius=0) 
print("temp1.celsius =", temp1.celsius) 
print("temp1.fahrenheit =", temp1.fahrenheit) 
print("") 
temp1.celsius = 100 
print("temp1.celsius =", temp1.celsius) 
print("temp1.fahrenheit =", temp1.fahrenheit) 
print("") 
temp2 = Temperature(fahrenheit=0) 
print("temp2.fahrenheit =", temp2.fahrenheit) 
Python Examples | 481
print("temp2.celsius =", temp2.celsius) 
print("") 
temp2.fahrenheit = 100 
print("temp2.fahrenheit =", temp2.fahrenheit) 
print("temp2.celsius =", temp2.celsius) 