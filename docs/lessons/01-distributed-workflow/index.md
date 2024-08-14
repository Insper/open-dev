# 01 - Distributed Development Workflow

<ah-external-content src="slides_fb.html" />


In this guide, we will work on the standard workflow for contributing to projects hosted on GitHub (which also applies to Git projects in general). Before starting, each student should locate the corresponding issue on the course's GitHub repository for creating their user.

Our workflow will be based on three main parts. In the first part, we will create a copy of the repository "insper/dev-aberto" where we will make all the necessary changes. In the second part, we will send our modifications to the original repository using a *Pull Request*, which is a request to accept the changes from a forked repository into the original repository. Finally, we will update our fork with modifications sent by colleagues.

Some key points to highlight in the above workflow:

1. Even if a user does not have access to the original repository, they can work on their own copy and only submit their modifications to the original repository when everything is ready.
2. It is necessary for a developer from the original project to "take responsibility" for the accepted external modifications.
3. The *Pull requests* tab allows developers to discuss proposed modifications and improve them. Every commit made after the creation of the PR is included and can be tested by anyone.

## Creating your own copy

We will start our workflow by creating a fork of the repository "insper/dev-aberto". All our modifications will be made in our fork, on a separate branch (it is recommended to use a different branch for each issue). This way, our modifications are completely isolated from the original code, and we can test them alongside the original code.

First, create the fork through the GitHub interface. Then, clone your fork and create a new branch called "issue-X," where "X" is the number of your issue in the original project.

<ah-terminal>
$ git checkout -b issue-X
</ah-terminal>

To ensure that you are in the directory of your fork, execute the following command:

<ah-terminal>
$ git remote -vv
</ah-terminal>

The displayed addresses should be those of your fork, not the original project.

With the fork created and being on the "issue-X" branch (you can check using `git branch` and switch using `git checkout issue-X`), we will begin making modifications.

### Interacting with the course repository

The creation of users and addition of skills is done using the command `dev-aberto.py`.

!!! tip
    To use it, you need to install the packages listed in the requirements.txt file.

Running it in the terminal should list the available commands.

<ah-terminal>
$ python3 dev-aberto.py
</ah-terminal>

To check if everything is working correctly, list all registered users. There should be only one registered user (`igorsm1`).

### Creating a user

User creation is done with the command:

<ah-terminal>
$ python3 dev-aberto.py new-user
</ah-terminal>

This will create three files in the `students` folder:

- `your-login`: basic user information in JSON format.
- `your-login-achievements`: encrypted file containing the deliveries of each student in JSON format.
- `your-login.key`: cryptographic key for the above file.

Verify that your user was created correctly by listing the existing users again. Your user should have an asterisk (*) next to the name, indicating that the login.key file is present in the system.

!!! danger
    Do not include the `*.key` file in your PR. It should be sent by email to the professor. Do this now before you forget!

Also, verify that you can use the command `dev-aberto.py compute-grade your-login`. If everything is okay, proceed to the next item.

### Adding a skill

With the user created, we can add the skill "First Steps." You may have noticed that the professor's key is available (file `students/igorsm1.key`). This was done so that you have at least one example of how each skill should be added. See below for an example of how the skill should be included:

<ah-terminal>
$ python3 dev-aberto.py edit-achievements igorsm1
</ah-terminal>

This will open a file for editing in *Vi*. The format is a list of objects containing two fields: "skill_id" and "metadata". See the example below for the first skill

```
[
{"skill_id": 1, "metadata": {"date": "YYYY-MM-DD"} }
]
```

!!! tip
    If you want to use another text editor, you can set the environment variable `EDITOR` just before calling `dev-aberto.py`.

Now add the skill to your user following the same pattern seen above. Verify that your skill was correctly added using the `compute-grade` command.

!!! tip
    If your repository is *OK*, help your classmates.

## Sending modifications to the original project

Now let's create a commit and send it as a *Pull Request* to the course's repository. Add the created files (excluding the `*.key` file!) and make a commit with the following message (replace the *X* with the number of your issue in the repository):

```
Add user your-login.
```

Execute `git push` and continue.

With your modifications already in your fork, it's time to send them to the original repository. This is done on the GitHub interface. First, access your fork in the browser, locate your *issue-X* branch, and click the "Pull request" button.

![This message appears when your fork has commits that are not present in the original repository.](PR-github.png){width="90%"}

The title of your Pull Request should be *Create user login*. Your PR should contain only one commit and should have the branch `issue-X` created above as the source. In the description of your PR, add the text:

```
Closes #X
```

where `X` is the number of your user's issue. This automatically closes the issue when (and if) this PR is accepted.

!!! warning
    PRs made from `main` or with more than one commit will not be accepted.

Use the checklist below to help verify if your work is correct:

- [ ] Created a new user with `new-user`.
- [ ] Added the "First Steps" skill.
- [ ] Checked that the new user has the new skill using `compute-grade`.
- [ ] Created a PR with only one commit and the correct files.
- [ ] Sent the `.key` file by email to the professor.
- [ ] Did not include the `.key` file in the PR.

Once your PR is accepted, you can remove the issue-X branch.

## Updating your fork

After having your PR accepted, you may have noticed that your commit appears in the original project's `main` branch but does not appear in your fork. This is because a fork is not automatically updated when its corresponding original repository receives new commits.

To make this happen, you need to perform a manual synchronization. For now, we will use the GitHub interface to do this.

Visit your fork again. Now, there should be an option to sync your fork with the original repository. Use it to make your `main` branch receive the new commits.

!!! warning
    Sync your repository whenever you work on a new PR. This will prevent many conflicts when merging your modifications into the original repository.
