#!/usr/bin/env python3

import os

# 添加tmux配置到zsh环境
os.system('echo "[[ \$TERM != \\"screen\\" ]] && exec tmux" >> ~/.zshrc')
