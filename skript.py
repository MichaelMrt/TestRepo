import os
print("hello world")
script_dir = os.path.dirname(os.path.abspath(__file__))  

with open(os.path.join(script_dir,"test1.txt"), 'w') as file:
    file.write('hi')

with open(os.path.join(script_dir,"test2.txt"), 'w') as file:
    file.write('hi')

with open(os.path.join(script_dir,"test3.txt"), 'w') as file:
    file.write('hi')

