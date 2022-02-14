import hashlib

f = open("block.txt", "r")
block = f.readline()[:-1]
f.close()

nonce = 0
while(True):
    to_hash = block + str(nonce)
    to_hash_byte = to_hash.encode()
    hash = hashlib.sha256(to_hash_byte).hexdigest()
    if (hash[0:3]=="00"):
        print(to_hash)
        print(hash)
        break
    nonce = nonce + 1

f = open("result.txt", "w")
f.write("string is " + block + "\n")
f.write("nonce is " + str(nonce) + "\n")
f.write("to_hash is " + block + str(nonce) + "\n")
f.write("hash is " + hash)
