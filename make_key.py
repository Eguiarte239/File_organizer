import os
import winreg as reg

# Get absolute path of the file organizer executable
relativePath = os.path.join((os.environ['USERPROFILE']), 'Desktop')
absolutePath = os.path.join(relativePath, r'File_organizer\file_organizer.exe')

# Set the path of the context menu (right-click menu)
key_path = r'Directory\\Background\\shell\\File organizer\\'

# Create outer key
key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, 'Organize files from this folder')

# Create inner key
command = reg.CreateKey(key, r"command")
reg.SetValue(command, '', reg.REG_SZ, r''+absolutePath)