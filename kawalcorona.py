import json, requests, os, sys
def ask():
	pilih = raw_input("lanjut y/n: ").lower()
	if pilih == "y":
		info()
        elif pilih == "n":
                sys.exit()
        else:
		print "Pilih y/n?"
		ask()
def info():
	os.system("clear")
	print """\033[93m
   ______           _     __
  / ____/___ _   __(_)___/ /
 / /   / __ \ | / / / __  /
/ /___/ /_/ / |/ / / /_/ /
\____/\____/|___/_/\__,_/
----------------------------------\033[97m
Code By	: Wibu Code
source	: https://kawalcorona.com
\n"""
	print "\033[97m[1] \033[91mData Indonesia"
	print "\033[97m[2] \033[92mData Provinsi"
	print "\033[97m[3] \033[96mData Global \n \033[97m"
	select = raw_input("Select Number =>: ")
	api = "https://api.kawalcorona.com"
	if select == "1":
		os.system("clear")
		print """\033[91m
    ____          __                      _
   /  _/___  ____/ /___  ____  ___  _____(_)___ _
   / // __ \/ __  / __ \/ __ \/ _ \/ ___/ / __ `/
 _/ // / / / /_/ / /_/ / / / /  __(__  ) / /_/ /
/___/_/ /_/\__,_/\____/_/ /_/\___/____/_/\__,_/
\033[97m \n"""
		url = api+"/indonesia"
		r = requests.get(url)
		data = json.loads(r.text)
		for info in data:
			print "-"*30
			print "Positif		: "+"\033[92m"+info['positif']+"\033[97m"
			print "Sembuh		: "+"\033[96m"+info['sembuh']+"\033[97m"
			print "Meninggal	: "+"\033[91m"+info['meninggal']+"\033[97m \n"
		pass
		ask()
	elif select == "2":
		os.system("clear")
		print """\033[92m
    ____                  _            _
   / __ \_________ _   __(_)___  _____(_)
  / /_/ / ___/ __ \ | / / / __ \/ ___/ /
 / ____/ /  / /_/ / |/ / / / / (__  ) /
/_/   /_/   \____/|___/_/_/ /_/____/_/
\033[97m \n"""
		url = api+"/indonesia/provinsi"
		r = requests.get(url)
		data = json.loads(r.text)
		for info in data:
			res = info['attributes']
			print "(\033[93m"+res['Provinsi']+"\033[97m)"
			print "-"*30
			print "Positif		: "+"\033[92m"+(str(res['Kasus_Posi']))+"\033[97m"
			print "Sembuh		: "+"\033[96m"+(str(res['Kasus_Semb']))+"\033[97m"
			print "Meninggal	: "+"\033[91m"+(str(res['Kasus_Meni']))+"\n \033[97m"
		pass
		ask()
	elif select == "3":
		os.system("clear")
		print """\033[96m
   ________      __          __
  / ____/ /___  / /_  ____ _/ /
 / / __/ / __ \/ __ \/ __ `/ /
/ /_/ / / /_/ / /_/ / /_/ / /
\____/_/\____/_.___/\__,_/_/
\033[97m \n"""
		r = requests.get(api)
		data = json.loads(r.text)
		for info in data:
			res = info['attributes']
			print "(\033[91m"+res['Country_Region']+"\033[97m)"
			print "-"*30
			print "Konfirmasi	: "+"\033[92m"+(str(res['Confirmed']))+"\033[97m"
			print "Sembuh		: "+"\033[96m"+(str(res['Recovered']))+"\033[97m"
			print "Meninggal	: "+"\033[91m"+(str(res['Deaths']))+"\n \033[97m"
		pass
		ask()
	else:
		print "\033[91mSelect Number!\033[97m"
try:
	info()
except KeyboardInterrupt:
	print "Ctrl + C (exit)"
