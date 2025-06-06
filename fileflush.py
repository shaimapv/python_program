import time

file_1=open('file.txt','w')
for i in range(5):
    print(f"logging event {i+1}",file = file_1,flush=True)
    time.sleep(1)

print("demonstrate working of file and flush",flush=True )

print("hello world",file=file_1)



"""  output:
PS C:\training\2nd task> python fileflush.py
demonstrate working of file and flush

file.txt:
logging event 1
logging event 2
logging event 3
logging event 4
logging event 5
hello world

"""
