from subprocess import call
from hurry.filesize import size
import zipfile
import os

def show_jar_classes(jar_file):

    deleted_files = 0
    total_size_before_script = os.stat(jar_file).st_size

    zf = zipfile.ZipFile(jar_file, 'r')
    try:
        lst = zf.infolist()
        for zi in lst:
            fn = zi.filename
            if fn.endswith('.txt'):
                delete_file(jar_file_name, fn)
                deleted_files = deleted_files + 1
            elif fn.endswith('pom.xml'):
                delete_file(jar_file_name, fn)
                deleted_files = deleted_files + 1
            elif fn.endswith('pom.properties'):
                delete_file(jar_file_name, fn)
                deleted_files = deleted_files + 1
    finally:
        zf.close()

    total_size_after_scrpit = os.stat(jar_file).st_size
    print('Resume of script:\nTotal of files deleted: {0}'.format(deleted_files))
    print('Total size of {0} before script is {1}'.format(jar_file, size(total_size_before_script)))
    print('Total size of {0} now is {1}'.format(jar_file, size(total_size_after_scrpit)))

def delete_file(jar, file_to_delete):
    call(["zip", "-d", jar, file_to_delete])


jar_file_name = input("Jar name: ")

show_jar_classes(jar_file_name)
