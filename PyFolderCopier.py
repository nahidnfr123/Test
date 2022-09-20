import os
import shutil
import subprocess

baseDir = "C:/Users/NFR/Desktop/Projects/"
source = "NfrExamination"
sourcePath = baseDir + source
projects = ["Project 1", "Project 2"]
destination = '/src/components/'


def cmd(path):
    if os.path.isdir(path):
        # subprocess.Popen("ls", cwd=path)
        subprocess.Popen(['git', 'add', '.'], stdout=subprocess.PIPE, cwd=path)
        subprocess.Popen(['git', 'commit', '-m', '"Python Automated Git Commit"'], stdout=subprocess.PIPE, cwd=path)
        pushed = subprocess.Popen(['git', 'push', '-u', 'origin', 'master'], stdout=subprocess.PIPE, cwd=path)
        test = pushed.communicate()[0]
        print(test)
        # subprocess.Popen("git pull", cwd=path)
        # subprocess.Popen("git commit -am 'Python Automated Git Commit'", cwd=path)
        # subprocess.Popen("git push -u origin master", cwd=path)


cmd('C:/Users/NFR/Desktop/GitAutomation/test')


def copy_folders():
    for target in projects:
        destination_path = baseDir + target + destination
        final_destination = destination_path + source
        if os.path.isdir(sourcePath) and os.path.isdir(destination_path):
            # Remove existing directory
            if os.path.isdir(final_destination):
                shutil.rmtree(final_destination)
            # Remove existing file
            elif os.path.isfile(final_destination):
                os.remove(final_destination)
            # Paste directory
            shutil.copytree(sourcePath, final_destination, symlinks=False, ignore=shutil.ignore_patterns('*.idea', '*.git'), dirs_exist_ok=False)
            # cmd(baseDir + target)
            print(source, 'has been moved to', target, '!')
        else:
            print("Directory does not exist")

# copy_folders()

# Fetching the list of all the files
# files = os.listdir(sourcePath)
# Fetching all the files to directory
# for file_name in files:
#     shutil.copy(origin + file_name, baseDir + target + destination + file_name)

# git commit -am "Python Auto Git Commit"
# git push -u origin dev
