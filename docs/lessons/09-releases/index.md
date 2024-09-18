# 09 - Releases

Creating a release is the final step to distribute software to users. It involves "freezing" the repository in a specific commit and attaching binaries and other ready to use assets. Users should be able to grab one of the releases and use it direclty without having to setup a dev environment. 

The skill *New Release* involves the creation of a release for your own project used in the last lessons. 


:material-package-up:{ .achicon }

> "skill_id": 12, "metadata": {"url": "release url", "group": ["student2"]}



## Instructions

The following guids might be useful.

- [Creating releases in Github](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [PyInstaller](https://pyinstaller.org/en/stable/) for creating installers/binaries using Python

The following checks will be used to verify if this skill is completed:

- [ ] there is a release in the repo's *Releases* tab containing the description of the release and the source code
- [ ] the release includes either an installer or a direccly executable file in one of the following formats:
    - **Linux**: *.deb, .rpm* for installers, **AppImage** for executables
    - **Windows**: *.msi* installer or single *.exe* (plus asses, if necessary)
    - **Other**: if the project is an extension, plugin or any other type of stoftware, the release must include a redistributable package in the official format


