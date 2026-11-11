from random import sample
from dadu import Dadu
 
print("=== 9-13 Dadu ===")
for sisi in (6, 10, 20):
    dadu = Dadu(sisi)
    print(f"Dadu {sisi} sisi, dilempar 10 kali:")
    for _ in range(10):
        dadu.lempar_dadu()
    print("\n")