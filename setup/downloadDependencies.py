import subprocess

try:
    subprocess.run('pip install -r ./setup/requirements.txt'.split(' '))
except Exception as error:
    print(error)
else:
    print('Dependencies Installed')