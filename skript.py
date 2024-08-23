import time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))  
print(script_dir)

with open("test.txt", 'w') as file:
    file.write('hi')
    
time.sleep(5)
print(script_dir)
