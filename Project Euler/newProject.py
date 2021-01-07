import sys
import os

if len(sys.argv) < 2:
    print("Invalid Arguments")
    exit()

os.system(f"mkdir {sys.argv[1]}")

os.system(f"cd {sys.argv[1]}")

os
