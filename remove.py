import os

def remove(path):
    if os.path.exists(path):
        os.remove(path)
        print("удалено")
        return True
    else:
        print("The file does not exist")
        return False
