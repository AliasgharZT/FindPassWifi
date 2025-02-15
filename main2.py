
import subprocess 

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']
                               ).decode('utf-8', errors="backslashreplace"
                                        ).split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for profile in profiles:
    results = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], 
                             capture_output=True).stdout.decode()
    password = [line.split(":")[1][1:-1] for line in results.split("\n") if "Key Content" in line]
    try:
        print("{:<30}| {:<}".format(profile, password[0]))
    except IndexError:
        print("{:<30}| {:<}".format(profile, "")) 
