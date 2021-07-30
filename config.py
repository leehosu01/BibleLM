
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:18:30 2021

@author: map
"""

train_file = 'train.txt'
test_file = 'test.txt'
models_path = 'models_ckpts'
max_length = 256

import subprocess
subprocess.run(f"git clone https://github.com/huggingface/transformers", shell = True)
subprocess.run(f"mkdir {models_path}/", shell = True)
subprocess.run(f"cd transformers && git checkout tags/v4.9.1", shell = True)
subprocess.run(f"cd transformers && pip3 install . && python setup.py install", shell = True)
subprocess.run(f"pip3 install -r transformers/examples/pytorch/_tests_requirements.txt", shell = True)