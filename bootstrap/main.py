import virtualenv


extension = open('venv-extension.py').read()
output = virtualenv.create_bootstrap_script(extension)
f = open('bootstrap.py', 'w').write(output)
