# Bu kısmın tek farkı lock.json dan çok daha kısa ve daha üst düzey şekilde kodlanmış olmasıdır fakat işlevleri aynıdır.
# This part is only different in that it is much shorter and more high-level than lock.json but its functions are the same.

import random
import string
import json

letters = string.printable

arr = {ch: ''.join(random.choices(letters, k=16)) for ch in letters}

json.dump(arr, open("pass.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

open("./codes/output.txt", "w", encoding="utf-8").write(''.join([arr.get(c, c) for c in open("./codes/input.txt", encoding="utf-8").read()]))
print("Success!")