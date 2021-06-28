import os
import errno

try:
    os.mkdir("upload/Linuz Tri Erianto")
except OSError as exc:
    if exc.errno != errno.EEXIST:
        print("sini23")
        raise
    os.system("cd upload ; rm -rf '{}'".format("Linuz Tri Erianto"))
    os.mkdir("upload/Linuz Tri Erianto 3")
    print("success")
