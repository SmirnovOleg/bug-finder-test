import os
import pickle
import shutil
import sys

'''
This function demonstrates plugin's capabilities of working with OS methods and attributes.
Also it includes distributed semantic pattern with `enumerate()` function call replacement.
'''


def load_change_graphs(argv):
    storage_dir = argv[1]
    file_names = os.listdir(storage_dir)
    print(f'Found {len(file_names)} files in storage directory')
    change_graphs = []
    for file_num in range(len(file_names)):
        print(f'Looking at file with number {file_num}...')
        file_name = file_names[file_num]
        file_path = os.path.join(storage_dir, file_name)
        try:
            with open(file_path, 'rb') as f:
                graphs = pickle.load(f)
            for graph in graphs:
                change_graphs.append(pickle.loads(graph))
        except:
            print(f'Incorrect file {file_path}')
        if file_num % 1000 == 0:
            print(f'Loaded [{1 + file_num}/{len(file_names)}] files')
    print('Pattern mining has started')

    if argv[2]:
        print('Creating directory with info...')
        os.mkdir(os.path.join(argv[3], 'info'))
        print('Directory successfully created.')
    if os.path.exists(argv[4]):
        shutil.rmtree(argv[4])


if __name__ == '__main__':
    load_change_graphs(sys.argv)
