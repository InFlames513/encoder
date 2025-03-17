f = 0
for i in range(50):
  import subprocess
  subprocess.run(["python", "lock.py"])

  txt1 = open("./codes/input.txt", "r", encoding="utf-8").read()
  import subprocess
  subprocess.run(["python", "upgLock.py"])

  txt2 = subprocess.run(["python", "unlock.py"], capture_output=True, text=True).stdout
  if txt1 != txt2: f=f+1
  print(f"{i+1} -> ", txt1 == txt2)

print(f)