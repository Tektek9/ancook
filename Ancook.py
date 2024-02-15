import json
import sys
from termcolor import colored as cl

class acukie:
    def __init__(self, yh):
        self.yh = yh

    def logo():
        print(cl("\nAcunetix Cookie\n   by CukiD\n", "magenta"))

    def proses(self):
        with open(str(self.yh[2]), 'r') as file:
            ini = json.load(file)

        gaktau = set()
        for apasih in ini:
            if 'domain' in apasih:
                gaktau.add(apasih['domain'])
            
        for dmn in gaktau:
            print(cl(f"\nCookie URL:","green"))
            print(f"{dmn}\n")
            print(cl("Cookie Value:","green"))
            for apasih in ini:
                if 'domain' in apasih and str(apasih['domain']) == str(dmn):
                    aku = apasih['name']
                    kmu = apasih['value']
                    print(f"{aku}:{kmu};", end='')
            print("\n")

if __name__ == "__main__":
    yuhu = sys.argv 
    if len(yuhu) < 2:
        acukie.logo()
        print("Untuk bantuan:\n  python.exe Ancook.py -h/--help\n")
    elif str(yuhu[1]) == "-h" or str(yuhu[1]) == "--help":
        acukie.logo()
        print("Detail:\n  -c / --convert - Untuk melakukan convert json ke format cookie Acunetix\n\nPenggunaan:\n  python.exe Ancook.py -c [cookie.json]\n")
    elif len(yuhu) < 3:
        acukie.logo()
        print("Silahkan masukan nama file cookie.json\n  Untuk bantuan python.exe Ancook.py -h/--help\n")
    elif len(yuhu) < 4 and (str(yuhu[1]) == "-c" or str(yuhu[1]) == "--convert"):
        lapo = acukie(yuhu)
        lapo.proses()
else:
    acukie.logo()