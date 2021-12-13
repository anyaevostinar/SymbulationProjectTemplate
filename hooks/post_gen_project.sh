#!/bin/bash


# Automate git repository and submodule initialization
# Adopted from https://github.com/devosoft/cookiecutter-empirical-project#quickstart
git init
git add .
git submodule add https://github.com/anyaevostinar/SymbulationEmp.git
git submodule add -b master https://github.com/devosoft/Empirical.git
git submodule init
git submodule update --recursive --init

git commit -m "Initial commit"

# Attempt to push local repo to remote repository on github
git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git
git push origin master || echo 'speculative initial push failed, try setting up repo on github first.'
