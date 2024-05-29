import shutil
import os

src_dir = 'frontend/dist'
dest_dir = 'merchex/blog/static/dist'

if os.path.exists(src_dir):
    shutil.copytree(src_dir, dest_dir)
    print(f'Static files copied from {src_dir} to {dest_dir}')
else:
    print(f'{src_dir} does not exist')
