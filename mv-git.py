import os
import shutil
import subprocess

baseDir = "/home/nahid/Desktop/Projects/"
source = "NfrExamination"
sourcePath = baseDir + source
# projects = ["allexambd", "biddabari-web", "canvas-ict", "coursecab", "englishmojapb", "marchforwardbd-new", "medilogy", "p2a", "studyplex", "tutoracademia", "mediaim", "shawonsbangla-web", "admission-assistant-web", "ieducation-web", "lingual-academy", 'youthcareer-web']
projects = ["allexambd", "biddabari-web", "canvas-ict", "englishmojapb", "marchforwardbd-new", "medilogy", "p2a", "studyplex", "tutoracademia", "mediaim", "shawonsbangla-web", "admission-assistant-web", "ieducation-web", "lingual-academy", 'youthcareer-web']
destination = '/src/components/'


def cmd(path):
    if os.path.isdir(path):
        subprocess.Popen("git pull", cwd=path)
        subprocess.Popen("git commit -am 'Python Automated Git Commit'", cwd=path)
        subprocess.Popen("git push -u origin dev", cwd=path)


def copy_folders():
    for target in projects:
        destination_path = baseDir + target + destination
        final_destination = destination_path + source
        if os.path.isdir(sourcePath) and os.path.isdir(destination_path):
            if os.path.isdir(final_destination):
                shutil.rmtree(final_destination)
            elif os.path.isfile(final_destination):
                os.remove(final_destination)
            shutil.copytree(sourcePath, final_destination, symlinks=False, ignore=shutil.ignore_patterns('*.idea', '*.git'), dirs_exist_ok=False)
            # cmd(baseDir + target)
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
