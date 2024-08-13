import os
import ftplib
import time

host = input("[+] Host: ")
port = int(input("[+] Port: "))

user = "anonymous"
password = "anonymous"

try:
    ftp = ftplib.FTP()
    ftp.connect(host, port)
    ftp.login(user=user, passwd=password)
    print(f"[+] Logged with success!")
    print(f"[!] {ftp.welcome}")
    print("[!] Listing files...")
    time.sleep(2.0)
    files = ftp.nlst()
    for file in files:
        print(f"[!] {file}")
        local = os.path.join(os.getcwd(), file)
        openfile = open(local, "wb")
        def download(dt):
            openfile.write(dt)
        ftp.retrbinary(f"RETR {file}", download)
        print(f"{file} Downloaded!")
except Exception as error:
    print(f"[!] Error: {error}")
