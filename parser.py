
filepath = "C:/Users/bill/Workspace/scheduleInput.txt"

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = line.split('\t')
       print(line)
       line = fp.readline()
       cnt += 1