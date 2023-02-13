# new_project



run

```bash
    python build_project.py
```

to changes files with the project name you want

before attempting to start `make install`, please start the git repo inside the project.
The project won't build without a git repo initialized. It is used for auto version name.

At least, use

```bash
    git init
```

## how to...

### apply modifications from main to matplotlib branch

```bash
    git checkout matplotlib; git rebase master matplotlib
```