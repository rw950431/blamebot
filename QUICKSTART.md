used git-gui to clone https://github.com/OpenShiftDemos/os-sample-python.git into Documents/Python/blamebot
create new remote in gitlab web gui 

generate new public/private keypair as per https://blog.openshift.com/deploy-private-git-repositories/

added public key (just the key material) to
https://gitlab.com/rw950431/blamebot/settings/repository

added private key material to openshift console but it doesnt work.

https://blog.openshift.com/deploying-from-private-git-repositories/

Download oc command line client for windows. (33Mb!)

http://blog.lucywyman.me/deploy-private-git-repo-to-openshift.html#add-key-as-a-secret-to-openshift

generated openshift rsa key using git-bash ssh-keygen command line.  Uploaded .pub to gitlab, uploaded private keyfile to blamebot project on openshift.  Still doesnt work.

Eventually gave up and moved to public repo https://github.com/rw950431/blamebot

https://blog.openshift.com/getting-started-python/