
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:18:30 2021

@author: map
"""
from config import *

def train_model():
    import glob, re, os

    RANDOM_SEED = 42
    def seed_everything(seed=RANDOM_SEED):
        try:os.environ['PYTHONHASHSEED'] = str(seed)
        except:pass
        try:np.random.seed(seed)
        except:pass
        try:random.seed(seed)
        except:pass
        try:tf.random.set_seed(seed)
        except:pass
        try:torch.manual_seed(seed)
        except:pass
    seed_everything()

    processed_strs = []
    def txt_processing(X):
        nonlocal processed_strs
        l = re.compile("\d+\:\d+").split(X)[1:-1]
        processed_strs.extend(map((lambda X: re.sub(r'\s+', ' ', X).strip()), l))
    def as_txt(data, fname):
        with open(fname, 'w+') as fp:
            fp.write('<|endoftext|>'.join(data))
    for I in glob.glob("input_files/*.txt"):
        with open(I) as f:
            txt_processing(f.read())

    #print(processed_strs[-10:])



    from sklearn.model_selection import train_test_split
    train, test = train_test_split(processed_strs, test_size=0.2)

    as_txt(train, train_file)
    as_txt(test, test_file)

    subprocess.run(f"""
        python3 transformers/examples/pytorch/language-modeling/run_clm.py \
        --model_type {model_type} \
        --model_name_or_path {model_type} \
        --train_file {train_file} \
        --do_train \
        --validation_file {test_file} \
        --do_eval \
        --block_size {max_length} \
        --per_device_train_batch_size 2 \
        --save_steps -1 \
        --num_train_epochs {epochs} \
        --fp16 \
        --output_dir={models_path} \
        --overwrite_output_dir
        """, shell = True)
train_model()