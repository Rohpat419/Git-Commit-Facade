# Git-Commit-Facade

This is my attempt at implementing the original idea from: https://github.com/Shogun89/fancy_job.

This script runs a cron job that will add github commits to your commit history to make you look more "employable". Aimed at fooling companies that blindly check your github commit history when making a hiring decision. 

This project is just for fun, please don't throw my resume into the trash over this. 


## Notes

The github-actions bot needs the correct permissions to make commits to a repo, head over to your github repo: Settings -> Actions -> General, and select "Read and write permissions" under "Workflow Permissions"


## TODOS
Add functionality for user to specify their own cron expression using -c. 

Add functionality for daily randomization of the cron expression to create a random commit history, min of 0 commits and max of 24 commits in a day. Using --mayhem 
