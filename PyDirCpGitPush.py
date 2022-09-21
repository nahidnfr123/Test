import os
import shutil
import subprocess

baseDir = "/home/nahid/Desktop/Projects/"
source = "NfrExamination"
sourcePath = baseDir + source
projects = ["allexambd", "biddabari-web", "biologykillers", "canvas-ict", "coursecab", "englishmojapb", "marchforwardbd-new", "medilogy", "p2a", "studyplex", "tutoracademia"]
destination = '/src/components/'


def git_push(path, branch):
    if os.path.isdir(path):
        subprocess.Popen(['git', 'add', '.'], stdout=subprocess.PIPE, cwd=path)
        subprocess.Popen(['git', 'commit', '-m', '"Commit Previous!"'], stdout=subprocess.PIPE, cwd=path)
        subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE, cwd=path)
        subprocess.Popen(['git', 'add', '.'], stdout=subprocess.PIPE, cwd=path)
        subprocess.Popen(['git', 'commit', '-m', '"Python Automated Git Commit!"'], stdout=subprocess.PIPE, cwd=path)
        subprocess.Popen(['git', 'push', '-u', 'origin', branch], stdout=subprocess.PIPE, cwd=path)
        # test = pushed.communicate()[0]
        # print(test)


def copy_folders():
    branch = input('Git branch name:')
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
            # push files
            git_push(baseDir + target, branch)
            print(source, 'has been moved to', target, '!')
        else:
            print("Directory does not exist")


copy_folders()

# Fetching the list of all the files
# files = os.listdir(sourcePath)
# Fetching all the files to directory
# for file_name in files:
#     shutil.copy(origin + file_name, baseDir + target + destination + file_name)

# git commit -am "Python Auto Git Commit"
# git push -u origin dev