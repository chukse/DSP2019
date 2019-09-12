## Homework 1



*Problem* 2b <br />
**Command:** <br />
* git checkout test1
* cd homework/VCS/
* touch test.txt

**Output:**
* Switched to branch 'test1'



*Problem* 2c <br />
**Command:** <br />
* echo "This is some example text for branch test1" > test.txt


*Problem* 2d <br />
**Command:** <br />
* git add --all
* git status
* git commit

**Output:**
* On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   readme.md


* $ git commit
[master 09b4dcd] adding readme file for homework
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 homework/VCS/readme.md


*Problem* 2e <br />
**Command:** <br />
* git checkout test2


**Output:**
* ls: cannot open directory '.': Permission denied

**Explanation:** You cannot access because the two branches have not been merged. <br />


*Problem* 2f <br />
**Command:** <br />
* echo "This is some example text for branch test2" > test.txt

*Problem* 2g <br />
**Command:** <br />
* git checkout test1


**Output:**
* error: The following untracked working tree files would be overwritten by checkout:
        homework/VCS/test1.txt
Please move or remove them before you switch branches.
Aborting

**Solution:** $ git add -all and git commit 


*Problem* 2h <br />
**Command:** <br />
* git checkout master
* git merge test1


**Output:**
* $ git merge test1
Updating 09b4dcd..5eed19d
Fast-forward
 homework/VCS/test1.txt | 1 +
 1 file changed, 1 insertion(+)
 
 
 *Problem* 2i <br />
**Command:** <br />
* ls


**Output:**
* test1.txt readme.md

 *Problem* 2j <br />
**Command:** <br />
* git merge test2


**Output:**
* CONFLICT (add/add): Merge conflict in homework/VCS/test1.txt
Auto-merging homework/VCS/test1.txt
Automatic merge failed; fix conflicts and then commit the result.



 *Problem* 2k <br />
**Command:** <br />
* git checkout test2


**Output:**
* error: you need to resolve your current index first
homework/VCS/test1.txt: needs merge


 *Problem* 2l <br />
**Command:** <br />
* git status


**Output:**
* On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both added:      VCS/test1.txt

no changes added to commit (use "git add" and/or "git commit -a")


 *Problem* 2m <br />
**Command:** <br />
* vim test1.txt
* :wq


**Output:**
* 


 *Problem* 2n <br />
**Command:** <br />
* git status
* git add -all
* git commit
* git checkout test2


**Output:**
* [master be90c44] Merge branch 'test2' commit both
* Switched to branch 'test2'




 *Problem* 2o <br />
**Command:** <br />
* git branch -d test1


**Output:**
* error: The branch 'test1' is not fully merged.
If you are sure you want to delete it, run 'git branch -D test1'.


 *Problem* 2p <br />
**Command:** <br />
* git checkout master
* git branch -d test1
* git branch



**Output:**
* Switched to branch 'master'
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)
* Deleted branch test1 (was 5eed19d).
*  development,
"* master",
  test2
  
  
  
*Problem* 2q <br />

**Explanation:** The file test.txt was only merged in the master branch, therefore there is still an error when trying to delete branches from a branch which is not up to date in git status 
 
 
 *Problem* 2r <br />
**Command:** <br />
* git checkout test2
* git branch -d test2




**Output:**
* Switched to branch 'test2'
* error: Cannot delete branch 'test2' checked out at 'C:/Users/HP Owner/Desktop/Git/DSP2019'



   *Problem* 2s <br />
**Command:** <br />
* git checkout master
* git branch -d test2
* git branch




**Output:**
* Switched to branch 'master'
* Deleted branch test2 (was 87df16e)
*   development, "* master"


   *Problem* 2s <br />
**Command:** <br />
* git add --all
* git commit
* git status 
* git push



**Output:**
* Enumerating objects: 19, done.
Counting objects: 100% (19/19), done.
Delta compression using up to 4 threads
Compressing objects: 100% (13/13), done.
Writing objects: 100% (16/16), 1.32 KiB | 168.00 KiB/s, done.
Total 16 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 1 local object.
To https://github.com/chukse/DSP2019.git
   09b4dcd..be90c44  master -> master




  




















