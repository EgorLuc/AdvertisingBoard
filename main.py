from time import sleep

def upreg(msg):
	res = list(msg)
	while True:
		for i in range(len(res)):
			res[i] = res[i].upper()
			res[i-1] = res[i-1].lower()
			print(''.join(res), end="\r")
			delay = max(0.15, (10 / len(res)))
			sleep(delay)
			
msg = "Забавное приложение написанное на Python, с помощью работы со строками"
print("""
        ▄██▄░░░░░░▄▄
       ▐███▀░░░░░▄███▌
  ▄▀░░▄█▀▀░░░░░░░░▀██
 █░░░██░░░░░░░░░░░░░░░
█▌░░▐██░░▄██▌░░▄▄▄░░░▄
██░░▐██▄░▀█▀░░░▀██░░▐▌
██▄░▐███▄▄░░▄▄▄░▀▀░▄██
▐███▄██████▄░▀░▄█████▌
▐████████████▀▀██████
 ▐████▀██████░░█████
   ▀▀▀ █████▌░████▀
        ▀▀███░▀▀▀
""")

upreg(msg)
