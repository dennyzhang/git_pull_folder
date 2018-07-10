# git_pull_folder
Use docker to write code in different languages

<a href="https://github.com/DennyZhang?tab=followers"><img align="right" width="200" height="183" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/fork_github.png" /></a>

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[![LinkedIn](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/linkedin_icon.png)](https://www.linkedin.com/in/dennyzhang001) <a href="https://www.dennyzhang.com/slack" target="_blank" rel="nofollow"><img src="http://slack.dennyzhang.com/badge.svg" alt="slack"/></a> [![Github](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/github.png)](https://github.com/DennyZhang)

File me [tickets](https://github.com/DennyZhang/git_pull_folder/issues) or star [the repo](https://github.com/DennyZhang/git_pull_folder).

<a href="https://www.dennyzhang.com"><img align="right" width="185" height="37" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/dns_small.png"></a>

# How To Use
For a given folder, recursive check all sub-folders. If we find one .git folder, run git pull.

Thus we keep all git folder updated.
```
# go to the folder we want to update, run below:
pip install git

curl -L https://raw.githubusercontent.com/dennyzhang/git_pull_folder/master/git_pull_folder.py | python
```

Example:

In below example, we have two folders: cheatsheet and devops_public.

Under cheatsheet, we have cheatsheet-emacs-A4 and cheatsheet-golang-A4.

So run git_pull_folder.py will help to update all git repos.
```
.
├── cheatsheet
│   ├── cheatsheet-emacs-A4
│   │   ├── .git
│   │   ├── README.md
│   │   ├── README.org
...
│   └── cheatsheet-golang-A4
│   │   ├── .git
│       ├── README.md
│       ├── example_file.go
...
│       ├── misc
│       │   └── pages.json
└── devops_public
    ├── LICENSE
    │   ├── .git    
    ├── README.md
    ├── bash
    │   ├── S3Sync
    │   │   ├── README.md
...

2 directories, 196 files
```
# License
- Code is licensed under [MIT License](https://www.dennyzhang.com/wp-content/mit_license.txt).
