#!/usr/bin/bash
echo -e "\n"A
git log -1 --pretty=%B
echo -e "\n"B
git diff --name-only HEAD HEAD^ | wc -l
echo -e "\n"C
git diff --dirstat HEAD HEAD^ | wc -l
echo -e "\n"D
git diff HEAD HEAD^ | grep '^-$\|^-[^-]' | wc -l
echo -e "\n"E
git diff HEAD HEAD^ | grep '^+$\|^+[^+]' | wc -l
echo -e "\n"F
git diff HEAD HEAD^ | grep '^-$\|^-[^-]' | grep -v '^-\s*\*\|^-\s*\/\*' | grep -v '^-\s*$' | grep -v '^-\s*\/\/' | wc -l
echo -e "\n"G
git diff HEAD HEAD^ | grep '^+$\|^+[^+]' | grep -v '^+\s*\*\|^+\s*\/\*' | grep -v '^+\s*$' | grep -v '^+\s*\/\/' | wc -l
echo -e "\n"H
for file in `git diff --name-only HEAD HEAD^`; do echo $file; git log -2 --pretty=%cd $file; done
echo -e "\n"I
for file in `git diff --name-only HEAD HEAD^`; do echo $file; git log --pretty=oneline $file | wc -l; done
echo -e "\n"J
for file in `git diff --name-only HEAD HEAD^`; do echo $file; git log --pretty="  %aN" $file |sort -u; done
echo -e "\n"K
for file in $(git diff --name-only HEAD HEAD^); do git log --pretty=%aN $file; done | sort -u | while read auth; do echo -n $auth ": "; git log --pretty=%aN|grep "$auth" | wc -l; done
 