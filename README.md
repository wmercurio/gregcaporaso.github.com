Setting Up Your Environment:
========================

To begin editing the website you first need to install [Git](http://git-scm.com/download) for your operating system.

You will also require a github account. Sign up for github before continuing.

Navigate to https://github.com/ebolyen/ebolyen.github.io and in the top right corner, click "Fork".
What this does is it creates a clone of a repository under your github account. This is a github specific feature that maintains the relation between your copy and the original. This is used to allow "Pull Requests" but more on that later.

You will now be looking at your copy of the repository you have just created. On the right had side there will be a box that contains a URL and is titled "HTTPS clone URL", copy the contents of this box.

Now open a terminal window and navigate to a location where you want to store a local copy of the repository.
Type:
    `git clone <paste the "HTTPS clone URL" here>`
This will create a new directory in your current location, navigate into it.


Making Your Changes:
====================

To add your profile make sure terminal is open and navigate to the `people/` directory. Inside you will see a list of folders in the style of `firstname-lastname` create a folder with your name here. Next, copy the contents of `demo-user` into your new folder. You will use these as a template to get started.

You should now have 2 files, one named `index.md` and one names `profile.png`. Open `index.md` in your favorite editor.

The file should look like this: 

     ---
     layout: bio
     datatype: bio
     
     title: Demo User
     picture: "demo-user/profile.png" 
     abstract: "Hello this is my abstract."
     ---
     
     
     This is my space to put whatever I want.
 
1. Change the `title` from "Demo User" to your full name.
2. Change the `picture` path from "demo-user/profile.png" to "firstname-lastname/profile.png" it should match your folder.
3. Change the `abstract` to a short description of yourself.
4. Any space below the `---` will be rendered as [markdown](http://en.wikipedia.org/wiki/Markdown). 

Save your changes. 

Additionally find a profile picture and place it in your folder. You can rename it to be `profile.png` or you can open `index.md` and change the name of the picture in `picture`.

Using Git and github:
=====================

Navigate to your profile directory in terminal and type `git add *` this will tell Git to track every file and subfolder in the directory. 
Now that Git is tracking your new files we can add them as a commit. A commit acts as a snapshot of the entire project. It's job is to keep track of every change made between itself and the last commit. 
To add a new commit type: `git commit --all -m "<type a brief description of your commit here>"` and press enter.
Your current project state should now be stored as a commit. 

Next you will want to synchronize your local repository (your current location) with your github repository. To do this type: `git push origin master`. This tells Git that you want to upload your current string of commits to a remote location which by default is named `origin` furthermore, you are uploading the `master` branch which is the default branch on which your commits live.
Type in your github username and password.

Now your github repository matches your local repository. You will need to commit and push any additional changes you make in the future.

In github, on the side, select "Pull Requests". Then in the top right corner hit the green button that says "New Pull Request". This will take you to a page which shows an overview of the commits and the branches you are requesting a merge for. You generally don't need to worry about this. Just hit "Click to create a pull request for this comparison".
You are free to give the request a title and description, but for the purposes of this website, it is largely unnecessary, proceed by clicking the green "Send Pull Request" button.

Now it will be my (Evan) job to merge your pull request. Once I have done so you will be able to see your changes at:

http://ebolyen.github.io
