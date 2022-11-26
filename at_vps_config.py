import os


print("Welcome to the VPS setup script by Sirj\nThis will implement all the Operating System commands outlined in Perkmeisters VPS setup guide v5.\n\n")
host = input("First, what would you like to call this server? Type in your answer below and hit enter. The guide suggests Alchemy, but it can be whatever you want")
os.system(f'hostnamectl set-hostname {host}')

print("disabling sleep/hibernation")
os.system(f'systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target')

print("Now we need to add your useraccount")
user = input(f"what would you like to name your account?")
os.system(f'adduser {user}')

print("adding correct permissions to useracount")
os.system(f'usermod -aG sudo {user}')

print(f"Now when you ssh to this machine, you should use {user} instead of root, for example: {user}@x.x.x.x")

print(f"We are now updating your server, ensuring it has the latest patches, and replacing the desktop software so it runs optimally with nomachine later.")
os.system(f'apt update && apt autoremove --purge ubuntu-desktop && apt -y install gnome-session gnome-terminal && apt -y install xfe && apt -y install lxterminal && apt -y install htop')

print(f"Installing nomachine")
# os.system(f'apt update && apt -y install wget && wget https://download.nomachine.com/download/7.10/Linux/nomachine_7.10.1_1_amd64.deb && apt install -f  ./nomachine_7.10.1_1_amd64.deb && systemctl start nxserver.service')
os.system(f'wget https://download.nomachine.com/download/7.10/Linux/nomachine_7.10.1_1_amd64.deb && apt install -f  ./nomachine_7.10.1_1_amd64.deb && systemctl start nxserver.service')

print(f"Installing brave browser")
os.system(f'apt -y install apt-transport-https curl && curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg && echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list && apt update && apt -y install brave-browser')

print(f"Configuration complete, rebooting your computer when you hit the enter key, remember, when you log in next, use your new account {user}")
input()