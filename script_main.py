# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:45:02 2019

@author: Chris Crouch - a1015970
"""
import analyze_git_commit
from git import Repo, RemoteProgress
import os

class Progress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(self._cur_line)
#%%

local_link = "../camel"
remote_link = "https://github.com/apache/camel"
fixing_commit = "235036d2396ae45b6809b72a1983dee33b5ba32"

if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())

repo = Repo(local_link)
print("\n\n", repo.git.remote('get-url','origin'))

analyze_git_commit.analyze_git_commit(local_link, fixing_commit)

#%%

local_link = "../junit-plugin"
remote_link = "https://github.com/jenkinsci/junit-plugin"
fixing_commit = "15f39fc49d9f25bca872badb48e708a8bb815ea7"

if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())

repo = Repo(local_link)
print("\n\n", repo.git.remote('get-url','origin'))

analyze_git_commit.analyze_git_commit(local_link, fixing_commit)

#%%
local_link = "../jackson-databind"
remote_link = "https://github.com/FasterXML/jackson-databind"
fixing_commit = "7487cf7eb14be2f65a1eb108e8629c07ef45e0a"

if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())

repo = Repo(local_link)
print("\n\n", repo.git.remote('get-url','origin'))

analyze_git_commit.analyze_git_commit(local_link, fixing_commit)

