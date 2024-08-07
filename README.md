# 100-days-of-python-code-replit

Here's how to document your progress from repl.it to GitHub:

1. Open the [100 Days of Python Code](https://replit.com/learn/100-days-of-python/hub) repl.it.
2. Click the day number you want to work on.
3. Find the **Tools** section on the sidebar, then click **Git**.
4. It will open a panel of Git, then click **Initialize Git Repository**.
5. Go to the **Settings** gear icon on the panel, then under the **Remote** section, enter the URL of your GitHub repository. In my case, it's `https://github.com/PaullyMac/100-days-of-python-code-replit`.
6. Click **Save**. (In some cases, you may need to click **Save** again.)
7. Go back to the **Git** panel, and go to the **Pane Actions** icon. It will drop down a list of actions. Then type in the *Search* bar: **Shell**.
8. Click the **Shell** icon. It will open a terminal.
9. Then type in the terminal the following:

```bash
git branch --set-upstream-to=origin/main main
git pull origin main --allow-unrelated-histories --no-rebase
```
 so that it will set the upstream branch to the main branch of the GitHub repository and pull the changes from the GitHub repository. It will ask you to *Pass Github Credentials* (i.e., your GitHub username and password ) and click **Confirm for this session** to proceed.

10. Now, under the **Files** section, you can see the files that you have pulled from the GitHub repository together with the files from the repl.it repository.
11. Proceed with your coding.
12. After you have done your coding, go back to the **Git** panel, and add a summary of your commit in the **Commit** message box.
13. Go back to the **Shell** icon, then type in the terminal 
```bash
git add .
git commit -m "Your commit message here"
git push origin main
```
 so that it will add all the changes you have made, commit the changes with your commit message, and push the changes to the GitHub repository. It will ask you to *Pass Github Credentials* (i.e., your GitHub username and password) and click **Confirm for this session** to proceed.

14. Go to your GitHub repository, and you will see the changes you have made.
