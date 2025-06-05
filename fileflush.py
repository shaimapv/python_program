import time

file_1=open('file.txt','w')
for i in range(5):
    print(f"logging event {i+1}",file = file_1,flush=True)
    time.sleep(1)

print("demonstrate working of file and flush",flush=True )

print("hello world",file=file_1)