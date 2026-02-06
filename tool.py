import subprocess
import pyfiglet

text = pyfiglet.figlet_format("Web Pinner")
print(text)

print("Enter An IP or Website name: ")
i = input()
subprocess.call("ping "+ i ,shell=True)
