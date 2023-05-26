"""
    Utility functions for file extensions
"""
import os
from collections import defaultdict


files = ['logo.png', 'script.py', 'data.csv', 'login.py', 'urls.py']
print("Files list :", files)

def file_extension(ext,files):
    """" Retourns the list of files with the ext string extension (should include the point)

    :param ext: extenstion string to find in file names
    :param files: files names list
    :return: list of the files with the ext string extension

    >>> file_extension('.py',files)
    ['script.py', 'login.py', 'urls.py']
    """
    filter_py = lambda fname : True if fname.endswith(ext) else False
    return list(filter(filter_py, files))

print("\nPython files :", file_extension('.py',files))


def files_per_ext(file_list):
    """ Find the lists of files per extension and return them into a dictionary

    :param file_list: file lists to explore
    :return: the dictionary of extension-files pairs found into the file_list

    >>> files_per_ext(files)
    {'png': ['logo.png'], 'py': ['script.py', 'login.py', 'urls.py'], 'csv': ['data.csv']}
    """
    dd = defaultdict(list)
    for i in file_list:
        file, ext = os.path.splitext(i)
        dd[ext[1:]].append(i)
    return dict([(k,v) for (k,v) in dd.items()])

print("\nType files list :")
for (ext, file) in files_per_ext(files).items() :
    print("\t", ext,":", file)