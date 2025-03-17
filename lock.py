import random
import string
import json
letters = string.ascii_letters+string.digits+string.punctuation

def randomText(len):
  return ''.join(random.choices(letters, k=len))

content = open("./codes/input.txt", encoding="utf-8").read()

arr = {}
for i in range(len(letters)+1):
  arr[str(letters+" ")[i]] = randomText(16)

with open("pass.json", "w", encoding="utf-8") as f:
    json.dump(arr, f, ensure_ascii=False, indent=2)

newContent = list(content)
for i in range(len(newContent)):
  if arr.get(newContent[i]):
    newContent[i] = arr[newContent[i]]

open("./codes/output.txt", "w", encoding="utf-8").write(''.join(newContent))