NightmareForge v2.3 – Full Package Description
(Educational Red-Team / Authorized Penetration-Testing Research Framework)When the provided install.sh and nightmareforge.py are used together in an authorized testing environment, they form a complete, self-contained Linux red-team simulation platform with the following capabilities:One-click automated deployment  install.sh updates the system, installs all required dependencies (gcc, OpenSSL, wget, Python3, PyQt6, PyCryptodome, etc.), creates an isolated virtual environment, and marks the main script executable.

Instant launch of a fully functional red-team operator console  Starts nightmareforge.py --gui, opening a compact black/green PyQt6 control panel.

Comprehensive post-exploitation laboratory in a single script
Once running (on authorized target systems or lab VMs), the framework can demonstrate, with one click or one command, the following real-world adversary techniques:  Systemd + cron-based persistence mechanisms  
Decentralized P2P botnet command-and-control (port 6666) with automatic peer discovery and command propagation  
On-the-fly compilation and execution of:
• AES-256-CBC ransomware stub (educational encryption example targeting user documents)
• Silent XMRig Monero cryptominer deployment
• Raw /dev/input/eventX keylogger (low-level keystroke capture)  
Live bot-counter and global command broadcast to the P2P mesh network

Intended Use (strictly educational / authorized only)
The complete install.sh + nightmareforge.py package serves as an all-in-one teaching and red-team research tool to help cybersecurity students, certified penetration testers, and defensive teams study, detect, and mitigate modern Linux-targeted threats (ransomware, cryptojacking, P2P botnets, persistence, etc.) in controlled, fully consented lab environments.Use on any system without explicit written authorization is illegal. This tool exists solely to improve detection and defense capabilities against real criminal actors employing identical techniques in 2025.
NightmareForge v2.3 + install.sh – Complete Package Overview(Educational / Authorized Red Team & Research Use Only)When you run install.sh followed by (or automatically launching) nightmareforge.py --gui, the full package is capable of the following in a controlled, authorized lab environment:What the Combined System Does (Red Team Simulation Capabilities)Fully automates deployment of a self-contained post-exploitation research framework on Debian/Ubuntu-based Linux systems
Sets up a persistent, decentralized P2P botnet node with GUI operator console
Enables one-click simulation of real-world 2025 Linux threat techniques:File encryption (ransomware behavior research)
Cryptocurrency mining resource abuse
Raw input device keylogging
Systemd + cron persistence
Peer-to-peer command propagation (worm-like C2)

Files & Artifacts Generated After ExecutionRunning install.sh + nightmareforge.py will create/modify the following on the target system:File / Directory
Purpose (Research/Educational Context)
nf_env/
Python virtual environment with PyQt6, pycryptodome, etc.
nightmareforge.py
Main framework (made executable)
r.c, ransom
On-the-fly compiled AES-256-CBC encryption binary (ransomware stub)
kl.c, kl
Compiled raw /dev/input/event0 keylogger
x.tgz, xmrig, c.json
Downloaded & extracted XMRig Monero miner + config
/tmp/.k
Keylogger output (raw keycodes)
/etc/systemd/system/nf.service
Systemd persistence service
/etc/crontab
Modified with @reboot
 entry for persistence
nf.log
Local activity log (timestamps + actions)
/home/*/RANSOM.txt
Simulated ransom note (on user desktops)
Multiple *.locked files
Encrypted versions of target documents (research demo)
Open port 6666 (TCP)
P2P C2 listener for botnet research

Summary – Authorized Use OnlyThe full install.sh + nightmareforge.py package is a complete, automated red-team simulation and educational malware research platform that deploys a realistic, multi-technique Linux implant in under 30 seconds.It is designed exclusively for:Cybersecurity training labs
Authorized penetration testing
Defensive research and EDR rule development
Academic study of 2025-era Linux post-exploitation TTPs

Unauthorized deployment constitutes a serious computer crime offense in virtually every country. Use only on systems you own or have explicit written permission to test.
How to launch it 
NightmareForge v2.3 – Educational Execution Demo (LAB ONLY)
===========================================================
1.  git clone https://github.com/APT_BOTNETS_MAASTOOLKIT.git
2.  cd APT_BOTNETS_MAASTOOLKIT
3. chmod +x install.sh nightmareforge.py
4. ./install.sh                     # Auto-installs deps + PyQt6 + launches GUI
5. # OR manual one-liner (after deps already installed):
6. python3 -m venv nf_env && source nf_env/bin/activate && pip install PyQt6 pycryptodome
7. chmod +x nightmareforge.py
8. python nightmareforge.py --gui       # Starts P2P node + red-team GUI console
9. # In GUI: click MINE / KEYLOG / RANSOM / PERSIST to demo techniques
10. # Always run ONLY in isolated VM / authorized pentest lab!

