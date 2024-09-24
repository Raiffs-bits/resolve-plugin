
# Ensure the required package is installed by running the following command in your terminal:
# pip install python-davinci-resolve

# To run this script, use the following command in your terminal:
# python "C:\Users\Harri\OneDrive\Desktop\plugin for resolve\DavinciResolveScript.py"

# Ensure the required package is installed by running the following command in your terminal:
# pip install python-davinci-resolve

# Add the directory containing DaVinciResolveScript to the Python path
sys.path.append('/path/to/directory/containing/DaVinciResolveScript')

try:
	import DaVinciResolveScript as dvr  # type: ignore
except ImportError:
	try:
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'DaVinciResolveScript'])
		import DaVinciResolveScript as dvr  # type: ignore
	except Exception as e:
		messagebox.showerror("Error", f"Failed to install DaVinciResolveScript: {e}")
		sys.exit(1)
from gettext import install
import os
import shutil
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def install_plugin():
	"""
	Installs the ColorMatchPlugin to the DaVinci Resolve Fusion Scripts directory.

	Raises:
		Exception: If there is an error during the installation process, an exception
				   will be caught and an error message will be printed.
	"""
	try:
		plugin_dir = "ColorMatchPlugin"
		
		if os.name == 'posix':
			# macOS or Linux
			if sys.platform == 'darwin':
				resolve_plugin_dir = os.path.expanduser("~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp")
			else:
				resolve_plugin_dir = os.path.expanduser("~/.local/share/DaVinciResolve/Fusion/Scripts/Comp")
		elif os.name == 'nt':
			# Windows
			resolve_plugin_dir = os.path.expandvars(r"%APPDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp")
		else:
			raise Exception("Unsupported operating system")

		# Ensure the plugin directory exists
		if not os.path.exists(resolve_plugin_dir):
			os.makedirs(resolve_plugin_dir)

		# Copy the plugin to the DaVinci Resolve Fusion Scripts directory
		for filename in os.listdir(plugin_dir):
			full_file_name = os.path.join(plugin_dir, filename)
			if os.path.isfile(full_file_name):
				shutil.copy(full_file_name, resolve_plugin_dir)
		print("ColorMatchPlugin installed successfully.")
	except Exception as e:
		print(f"Error during installation: {e}")

if __name__ == "__main__":
	# Call the install_plugin function
	install_plugin()

	# Change directory to the plugin_for_resolve directory and run the script
	os.chdir('path/to/plugin_for_resolve')

	# Your main script logic goes here
	# For example, you can call other functions or execute additional code
	pass

# Add the directory containing DaVinciResolveScript to the Python path
sys.path.append('/path/to/directory/containing/DaVinciResolveScript')

try:
	import DaVinciResolveScript as dvr  # type: ignore
except ImportError:
	try:
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'DaVinciResolveScript'])
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])
		import DaVinciResolveScript as dvr  # type: ignore
	except Exception as e:
		messagebox.showerror("Error", f"Failed to install DaVinciResolveScript: {e}")
		sys.exit(1)

# Your script logic goes here

import os
import shutil
import sys
import tkinter as tk
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

try:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'aces-color-module'])

	try:
		import aces_color_module
	except ImportError:
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'aces-color-module'])
		import aces_color_module
except ImportError:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'aces_color_module'])
	import aces_color_module
except Exception as e:
	print(f"An error occurred: {e}")

# Your script logic goes here

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

# Change directory to the plugin_for_resolve directory and run the script
os.chdir('path/to/plugin_for_resolve')
subprocess.check_call(['python', 'DavinciResolveScript.py'])

# Your script logic goes here

import os
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
		
		if os.name == 'posix':
			# macOS or Linux
			if sys.platform == 'darwin':
				resolve_plugin_dir = os.path.expanduser("~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp")
			else:
				resolve_plugin_dir = os.path.expanduser("~/.local/share/DaVinciResolve/Fusion/Scripts/Comp")
		elif os.name == 'nt':
			# Windows
			resolve_plugin_dir = os.path.expandvars(r"%APPDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp")
		else:
			raise Exception("Unsupported operating system")

		# Ensure the plugin directory exists
		if not os.path.exists(resolve_plugin_dir):
			os.makedirs(resolve_plugin_dir)

		# Copy the plugin to the DaVinci Resolve Fusion Scripts directory
		shutil.copytree(plugin_dir, os.path.join(resolve_plugin_dir, plugin_dir), dirs_exist_ok=True)
		print("ColorMatchPlugin installed successfully.")
	except Exception as e:
		print(f"Error installing ColorMatchPlugin: {e}")
import os
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
		
		if os.name == 'posix':
			# macOS or Linux
			if sys.platform == 'darwin':
				resolve_plugin_dir = os.path.expanduser("~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp")
			else:
				resolve_plugin_dir = os.path.expanduser("~/.local/share/DaVinciResolve/Fusion/Scripts/Comp")
		elif os.name == 'nt':
			# Windows
			resolve_plugin_dir = os.path.expandvars(r"%APPDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp")
		else:
			raise Exception("Unsupported operating system")

		# Ensure the plugin directory exists
		if not os.path.exists(resolve_plugin_dir):
			os.makedirs(resolve_plugin_dir)

		# Copy the plugin to the DaVinci Resolve Fusion Scripts directory
		shutil.copytree(plugin_dir, os.path.join(resolve_plugin_dir, plugin_dir), dirs_exist_ok=True)
		print("ColorMatchPlugin installed successfully.")
	except Exception as e:
		print(f"Error installing ColorMatchPlugin: {e}")# Change directory to the plugin_for_resolve directory and run the script again
os.chdir('path/to/plugin_for_resolve')
subprocess.check_call(['python', 'DavinciResolveScript.py'])

# Your script logic goes here

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

# Change directory to the plugin_for_resolve directory and run the script
os.chdir('path/to/plugin_for_resolve')
subprocess.check_call(['python', 'DavinciResolveScript.py'])

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

# Change directory to the plugin_for_resolve directory and run the script
os.chdir('path/to/plugin_for_resolve')
subprocess.check_call(['python', 'DavinciResolveScript.py'])

# Your script logic goes here

# Change directory to the plugin_for_resolve directory and run the script again
os.chdir('path/to/plugin_for_resolve')
subprocess.check_call(['python', 'DavinciResolveScript.py'])

{
	"launch": {
		"configurations": [
			{
				"name": "Launch via NPM",
				"request": "launch",
				"runtimeArgs": [
					"run-script",
					"debug"
				],
				"runtimeExecutable": "npm",
				"skipFiles": [
					"<node_internals>/**"
				],
				"type": "node"
			}
		]
	}
}

import os
import shutil
import subprocess
import sys

def install_plugin():
	"""
	Installs the ColorMatchPlugin to the DaVinci Resolve Fusion Scripts directory.

	Raises:
		Exception: If there is an error during the installation process, an exception
				   will be caught and an error message will be printed.
	"""
	try:
		plugin_dir = "ColorMatchPlugin"
		
		if os.name == 'posix':
			# macOS or Linux
			if sys.platform == 'darwin':
				resolve_plugin_dir = os.path.expanduser("~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp")
			else:
				resolve_plugin_dir = os.path.expanduser("~/.local/share/DaVinciResolve/Fusion/Scripts/Comp")
		elif os.name == 'nt':
			# Windows
			resolve_plugin_dir = os.path.expandvars(r"%APPDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp")
		else:
			raise Exception("Unsupported operating system")

		# Ensure the plugin directory exists
		if not os.path.exists(resolve_plugin_dir):
			os.makedirs(resolve_plugin_dir)

		# Copy the plugin to the DaVinci Resolve Fusion Scripts directory
		for item in os.listdir(plugin_dir):
			full_file_name = os.path.join(plugin_dir, item)
			if os.path.isfile(full_file_name):
				shutil.copy(full_file_name, resolve_plugin_dir)
		print("ColorMatchPlugin installed successfully.")
	except Exception as e:
		print(f"Error during installation: {e}")

if __name__ == "__main__":
	# Call the install_plugin function
	install_plugin()

	# Change directory to the plugin_for_resolve directory and run the script
	os.chdir('path/to/plugin_for_resolve')

	# Your main script logic goes here
	# For example, you can call other functions or execute additional code
	pass

try:
	# Your installation logic here
	pass
except Exception as e:
	print(f"Error during installation: {e}")

# Call the install_plugin function
install_plugin()

# Change directory to the plugin_for_resolve directory and run the script
os.chdir('path/to/plugin_for_resolve')

# Ensure the script does not call itself in an infinite loop
if __name__ == "__main__":
	# Your main script logic here
	pass
import os
import subprocess
	
def install_plugin():
		try:
			# Your installation logic here
			pass
		except Exception as e:
			print(f"Error during installation: {e}")
	
	# Call the install_plugin function
	install_plugin()
	
	# Change directory to the plugin_for_resolve directory and run the script
	os.chdir('path/to/plugin_for_resolve')
	
	# Ensure the script does not call itself in an infinite loop
	if __name__ == "__main__":
		# Your script logic goes here
		pass

{
	"launch": {
		"configurations": [
			{
				"name": "Launch via NPM",
				"request": "launch",
				"runtimeArgs": [
					"run-script",
					"debug"
				],
				"runtimeExecutable": "npm",
				"skipFiles": [
					"<node_internals>/**"
				],
				"type": "node"
			}
		]
	}
}
