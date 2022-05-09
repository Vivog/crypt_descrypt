import pathlib

import pyAesCrypt
from pathlib import Path
def decrypt(file, password):
    print(f'---Begin to decrypt file: {Path(file).name}---')

    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(file), str(file).strip('.crp'), password, buffer_size)

    print(f'---File {Path(file).name} is decrypt---')
    pathlib.Path.unlink(file)
def crypt_in_dir(dir, password):
    for file in Path(dir).iterdir():
        path = Path(file)
        if path.is_file():
            try:
                decrypt(path, password)
            except Exception as ex:
                print(ex)
        else:
            crypt_in_dir(path, password)

def main():
    password = input('Enter password for decrypt: ')
    dir = input('Enter path for main dir: ')
    dir = str(dir).strip('\"')
    crypt_in_dir(dir, password)

if __name__ == '__main__':
    main()
