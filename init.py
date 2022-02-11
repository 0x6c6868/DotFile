#!/usr/bin/env python3

import os

# 添加tmux配置到zsh环境
os.system('echo "[[ \$TERM != \\"screen\\" ]] && exec tmux" >> ~/.zshrc')

# 安装vim vundle
os.system('git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim')

# TODO 移动相关 vimrc 配置

# 安装vim vundle插件
os.system('vim +PluginInstall +qall')
