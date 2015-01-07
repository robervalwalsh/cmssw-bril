## Create a CMSSW project
scram p CMSSW CMSSW_7_Y_X
cd CMSSW_7_Y_X/src
cmsenv
## Initialise cmssw git (this will suppress the checking out of files, need to do explicitly)
git cms-init
## add my standalone remote repository and fetch the branches
git remote add cmssw-bril git@github.com:robervalwalsh/cmssw-bril.git
git fetch cmssw-bril
git checkout cmssw7YX # (or any other branch you want)
## Add packages (use the git cms command)
git cms-addpkg BrilAnalysis/Bcm1f
git cms-addpkg BrilAnalysis/Skimming
## Get any modifications in the remote (= svn update)
git pull cmssw-bril
## Make local modifications and commit/push as usual
git commit -m  comments  < file>
git push
