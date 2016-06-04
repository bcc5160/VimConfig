#############################################################################
#
# This python script will configure vim FOR LINUX so it is easily awesome
#   Includes: 
#       - Vundle
#       - Monokai
#       - youcompleteme
#       - Bookmark
# PREREQ: MUST HAVE VIM, GIT, CMAKE, AND WGET INSTALLED ALREADY
#
#############################################################################

# Import libraries
import os
import subprocess

# PREREQ CHECK: VIM, GIT, CMAKE, PYTHON TOOLS, WGET [LINUX]
# IF NO VIM => cmd: sudo [install cmd] install vim
# IF NO GIT => cmd: sudo [install cmd] install git
# IF NO CMAKE *=> cmd: sudo [install cmd] install build-essential cmake 
# IF NO PY_DEV *=> cmd:sudo [install cmd] install python-dev python3-dev
# IF ERROR == Need Vim 3.4+ and you have that already
#	cmd: "sudo apt-get install vim-gnome-py2"

# Copy a local .vimrc using the template that I made
print("Getting a .vimrc template...")
os.system("wget https://raw.githubusercontent.com/bcc5160/VimConfig/master/.vimrc -O ~/.vimrc")
print("Template copied.")

# Create a .vim folder
print("Creating a .vim directory in the home directory...")
os.system("mkdir ~/.vim")
print(".vim directory made.")

# Within .vim, create the directories: colors and 
print("Creating colors folder...")
os.system("mkdir ~/.vim/colors")
print("Colors directory made.")

# Copy colors directory with current set of color schemes 
# ----- GET: MONOKAI -----
print("Getting monokai colorscheme...")
os.system("wget https://raw.githubusercontent.com/bcc5160/VimConfig/master/colors/monokai.vim -O ~/.vim/colors/monokai.vim")
print("Monokai colorscheme fetched.")

# Install Vundle to .vim
print("Cloning Vundle into ~/.vim/bundle/")
os.system("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim")
print("Vundle cloned.")

# Install the plugins listed in the .vimrc via command line
print("Install plugins in .vimrc...")
os.system("vim +PluginInstall +qall")
print("Plugins installed.")

# Special make/install for youcompleteme
#   cd ~/.vim/bundle/YouCompleteMe
#   ./install.py --clang-completer
print("Installing youcomplete stuff...")
os.system("cd ~/.vim/bundle/YouCompleteMe; python3 install.py --clang-completer")
print("youcompleteme done installing.")

# At this point all the plugins I configured are in the .vimrc, so if you want to add more just follow the trend
# 1. Write the plugin in the .vimrc
# 2. IN VIM, Install the plugins by typing: ":PluginInstall" or run the cmd above.
