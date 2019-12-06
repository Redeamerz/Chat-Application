import os

path = 'E:\\reddit_data'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if 'RC_' in file:
            files.append(os.path.join(r, file))

for f in files:
    f.rsplit('\\',1)[1]
    print("starting with: {}".format(f))
    print(f)