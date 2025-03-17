import json
content = open("./codes/output.txt", encoding="utf-8").read()
with open("pass.json", "r", encoding="utf-8") as f:
  arr = json.load(f)

block_size = 16
blocks = [content[i:i + block_size] for i in range(0, len(content), block_size)]
# Blokları yazdırmak
for block in blocks:
  for key, value in arr.items():
    if block == value:
      print(key, end="")