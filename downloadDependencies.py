import subprocess

try:
    subprocess.run('pip install -r requirements.txt'.split(' '))
except Exception as error:
    print(error)
else:
    print('Dependencies Installed')