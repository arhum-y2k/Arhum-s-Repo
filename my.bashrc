# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# easier unix commands
alias ll="ls -l"
alias la="ls -a"
alias lla="ls -l -a"

# my directory alias - switch to personal dev directory
alias mydir=""

# remove pychache
alias rm-pycache='find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf'

# git aliases
alias gst="git status"
alias gstu="git status -uno"
alias gdf="git diff"
alias gcm="git commit -m"
alias gsub="git submodule update --init --recursive"
alias grpo="git remote prune origin"
alias gbr="git branch"
alias gsw="git switch"
alias gcl="git clean -fd"
alias gcl_sub="git submodule foreach --recursive git clean -fd"
alias grs="git restore"
alias gmg="git merge"
alias groot="git rev-parse --show-toplevel"
alias groot_sub="git rev-parse --show-superproject-working-tree"
alias gbr_diff="git branch --format=\"%(color:red)%(refname:short) %(color:green)%(upstream)%(color:reset)\""
alias gbr_gone="git branch -v | awk '/gone/ {print}'"

# Bash prompt
# Example:
### [arhum.alam@eng-dev-01] [/scratch/users/arhum/git_repos/Themis] (branch aa-EQ-518-tb-test-config)
### >>>
export PS1="\n[\033[31m\u\033[0m@\033[31m\H\033[0m] [\033[36m\w\033[0m] (\033[32mbranch \033[0m\033[1;32m\$(git branch 2>/dev/null | grep '^*' | colrm 1 2)\033[0m) \n>>> "
export PROMPT_DIRTRIM=6

export LS_OPTIONS='--color=auto'
eval "$(dircolors -b)"
alias ls='ls $LS_OPTIONS'