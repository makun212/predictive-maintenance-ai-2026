e in what will be committed)
        .gitignore
        README.md
        app/
        data/
        models/
        requirements.txt
        src/
        tests/

nothing added to commit but untracked files present (use "git add" to track)
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (master)
$ git add .
git commit -m "Initial commit: predictive maintenance AI"
git branch -M main
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'app/app.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'data/README.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'requirements.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/features.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/predict.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/train.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tests/test_features.py', LF will be replaced by CRLF the next time Git touches it
[master (root-commit) 4b21541] Initial commit: predictive maintenance AI
 12 files changed, 10432 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 app/app.py
 create mode 100644 data/README.txt
 create mode 100644 data/ai4i2020.csv
 create mode 100644 models/.gitkeep
 create mode 100644 requirements.txt
 create mode 100644 src/__init__.py
 create mode 100644 src/features.py
 create mode 100644 src/predict.py
 create mode 100644 src/train.py
 create mode 100644 tests/test_features.py
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git log --oneline
4b21541 (HEAD -> main, origin/main, origin/HEAD) Initial commit: predictive maintenance AI
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git remote -v
origin  https://github.com/makun212/predictive-maintenance-ai.git (fetch)
origin  https://github.com/makun212/predictive-maintenance-ai.git (push)
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git push -u origin main
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/makun212/predictive-maintenance-ai.git/'
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git remote set-url origin https://github.com/makun212/予測保全AI-2026.git
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git remote set-url origin https://github.com/makun212/Predictive-Maintenance-AI-2026.git
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git push -u origin main
info: please complete authentication in your browser...
Enumerating objects: 18, done.
Counting objects: 100% (18/18), done.
Delta compression using up to 16 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (18/18), 138.97 KiB | 4.34 MiB/s, done.
Total 18 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: This repository moved. Please use the new location:
remote:   https://github.com/makun212/predictive-maintenance-ai-2026.git
To https://github.com/makun212/Predictive-Maintenance-AI-2026.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git push -u origin main
branch 'main' set up to track 'origin/main'.
Everything up-to-date
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git remote set-url origin https://github.com/makun212/predictive-maintenance-ai-2026.git
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git remote -v
origin  https://github.com/makun212/predictive-maintenance-ai-2026.git (fetch)
origin  https://github.com/makun212/predictive-maintenance-ai-2026.git (push)
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git add README.md
git commit -m "Improve README"
git push
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
Everything up-to-date
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   data/README.txt

no changes added to commit (use "git add" and/or "git commit -a")
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ git add README.md
git commit -m "Improve README"
git push
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   data/README.txt

no changes added to commit (use "git add" and/or "git commit -a")
Everything up-to-date
(.venv) 
fight@makun179 MINGW64 ~/OneDrive/Desktop/predictive-maintenance-ai (main)
$ 