import hashlib
username_trial = b"ANDERSON"
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"
order = [4,5,3,6,2,7,1,8]
dynamic = ""
for i in range(8):
	dynamic += hashlib.sha256(username_trial).hexdigest()[order[i]]
flag = key_part_static1_trial + dynamic + key_part_static2_trial
print(flag)