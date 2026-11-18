# Git and Docker screenshots - capture these on your own computer

The lab asks for screenshots showing *your* workflow. A generated project file
cannot prove that you pushed to your GitHub account or ran Docker on your PC.
Do not use fabricated screenshots as submission evidence.

1. Open VS Code terminal or PowerShell in your Lab 9 folder.
2. Run `git status`, `git add .`, `git commit -m "Complete INF1103 Lab 9"`,
   `git push origin main` (replace branch as needed), and `git log -3 --oneline`.
3. Take a **real screenshot** showing the successful push and recent commit:
   Windows `Win + Shift + S`. Save `evidence/git_workflow.png`.
4. Run `docker build -t inf1103-lab09 .` and `docker run --rm inf1103-lab09`.
5. Run `docker run --rm inf1103-lab09 python -m pytest -q`.
6. Take a **real screenshot** with the run output and passing tests. Save
   `evidence/docker_workflow.png`.
7. Replace or supplement the bundled local Git output image, then ZIP the
   folder again if submitting to LMS.

The bundled `git_local_output.png` is a truthful image of an actual **local**
Git session generated for this example. It is NOT proof of your GitHub push.
Docker was unavailable here, so there is no Docker execution screenshot.
