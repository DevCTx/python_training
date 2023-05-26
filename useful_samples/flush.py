'''
    Useful to understand the utility of Flush in print.
    Need to activate the Execution option : Emulate terminal in output console
    or to run it into a terminal
'''
import time

for i in range(5):
    print(i, end=" ", flush=False)  # Print everything together at the end
    time.sleep(0.5)
print("end")

for i in range(5):
    print(i, end=" ", flush=True)  # Print numbers as soon as they are generated
    time.sleep(0.5)
print("end")

for i in range(5):
    print(i, end=" ")  # by default : flush is False
    time.sleep(0.5)
print("end")

# Can be useful to print a progression
for i in range(10):
    print(f'Progression: {i+1}/10', end='\r', flush=True)
    time.sleep(1)