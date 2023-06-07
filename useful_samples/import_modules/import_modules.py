'''
    Shows that Python imports modules from:
    - the same script directory
    - the site_packages directory of the Python distribution used
    - directories added to PYTHONPATH (but not to PATH!!!)
'''
import sys

try:
    import mymodule_same_directory
    print(mymodule_same_directory.__name__, "found")
except ImportError as e:
    print(e.msg)

try:
    import mymodule_in_directory
    print(mymodule_in_directory.__name__, "found")
except ImportError as e:
    print(e.msg)

try:
    import mymodule_in_my_site_packages_directory
    print(mymodule_in_my_site_packages_directory.__name__, "found")
except ImportError as e:
    print(e.msg)

try:
    import mymodule_in_home_directory       # a file name 'mymodule_in_home_directory.py' is added at home
    print(mymodule_in_home_directory.__name__, "found")
except ImportError as e:
    print(e.msg)

try:
    import mymodule_in_root_directory       # a file name 'mymodule_in_root_directory.py' is added at root
    print(mymodule_in_root_directory.__name__, "found")
except ImportError as e:
    print(e.msg)

try:
    import mymodule_in_site_packages_directory
    print(mymodule_in_site_packages_directory.__name__, "found")
except ImportError as e:
    print(e.msg)

try:
    import os
    old_path = os.environ.get('PATH', '')
    new_path = old_path + os.path.join(os.path.dirname(os.path.abspath(__file__)), "added_to_PATH")
    os.environ['PATH'] = new_path           # mac/linux
    os.system(f'setx PATH "{new_path}"')    # windows

    import mymodule_in_PATH_directory
    print(mymodule_in_PATH_directory.__name__, "found")

    # Returns the previous values (please check for windows because it also adds the system's PATH values)
    temp = os.environ.get('PATH', '')
    os.environ['PATH'] = old_path           # mac/linux
    os.system(f'setx PATH "{old_path}"')    # windows
except ImportError as e:
    print(e.msg)

try:
    sys.path.append("./added_to_PYTHONPATH/")
    import mymodule_in_PYTHONPATH_directory
    print(mymodule_in_PYTHONPATH_directory.__name__, "found")
except ImportError as e:
    print(e.msg)
finally:
    sys.path.pop()


####
# mymodule_same_directory found
# No module named 'mymodule_in_directory'
# No module named 'mymodule_in_my_site_packages_directory'
# No module named 'mymodule_in_home_directory'
# No module named 'mymodule_in_root_directory'
# mymodule_in_site_packages_directory found
# SUCCESS: The specified value has been saved.
# No module named 'mymodule_in_PATH_directory'
# mymodule_in_PYTHONPATH_directory found