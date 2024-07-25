import os

allfiles = os.walk(r"c:\classroom\python\demo")

count = 0
for (dirname, folders, files) in allfiles:
    python_files = []
    for file in files:
        if file.endswith('.py'):
            python_files.append(file)

    if len(python_files) > 0:
        print("Folder : ", dirname)
        print("=" * 60)
        for file in sorted(python_files):
            print(file)

        print("Count = ", len(python_files))
        count += len(python_files)

print("=" * 80)
print("Total Count = ", count)

