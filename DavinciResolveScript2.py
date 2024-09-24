# plugin_for_resolve/
# │
# ├── main.py
# ├── scripts/
# │   └── DaVinciResolveScript.py
# ├── modules/
# │   └── aces_color_module.py
# └── ColorMatchPlugin/
#     └── (plugin files)

import os
import shutil
import sys
import subprocess
from tkinter import filedialog, messagebox

# Function to find DaVinciResolveScript module
def find_davinci_resolve_script():
	common_paths = [
		'C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\Developer\\Scripting\\Modules',
		'/Applications/DaVinci Resolve/Developer/Scripting/Modules'
	]
	for path in common_paths:
		if os.path.exists(path):
			return path
	return None

# Add the directory containing DaVinciResolveScript to the Python path
resolve_script_path = find_davinci_resolve_script()
if resolve_script_path:
	sys.path.append(resolve_script_path)
else:
	messagebox.showerror("Error", "DaVinciResolveScript module not found. Ensure DaVinci Resolve is installed and the path is correct.")
	sys.exit(1)

try:
	import DaVinciResolveScript as dvr  # type: ignore
except ImportError:
	messagebox.showerror("Error", "Failed to import DaVinciResolveScript. Ensure it is installed and the path is correct.")
	sys.exit(1)

# Add the directory containing aces_color_module to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

import aces_color_module

# Function to install the ColorMatchPlugin
def install_plugin():
	"""
	Installs the ColorMatchPlugin to the DaVinci Resolve Fusion Scripts directory.

	Raises:
		Exception: If there is an error during the installation process, an exception
				   will be caught and an error message will be printed.
	"""
	try:
		plugin_dir = "ColorMatchPlugin"
		resolve_plugin_dir = os.path.expanduser("~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp")

		if not os.path.exists(resolve_plugin_dir):
			os.makedirs(resolve_plugin_dir)

		for filename in os.listdir(plugin_dir):
			full_file_name = os.path.join(plugin_dir, filename)
			if os.path.isfile(full_file_name):
				shutil.copy(full_file_name, resolve_plugin_dir)
	except Exception as e:
		print(f"Error during installation: {e}")

# Call the install_plugin function
install_plugin()

# Your script logic goes here
def main():
	# Main logic of the script
	pass

if __name__ == "__main__":
	main()