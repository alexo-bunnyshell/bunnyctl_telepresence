# Wrapper for telepresence with Bunnyshell

## Known issues
- connections from replaced container to remote container not working
- need to handle multi container pods
- need to handle docker extra args


## requirements
- have kubectl intalled and able to connect to the desired cluster
- have telepresence installed (and able to connect to the same cluster as kubectl)


## usage

```bash 
#create and activate a python env
python3 -m venv ./py_env
source ./py_env/bin/activate

# install requirements
pip install -r requirements.txt

# have kubectl running, connected to the cluster
# this is on YOU!!


# install telepresence
# run this command, copy the output and run in bash
python bunny.py telepresence_install




# build the local container for "result"
docker build --platform=linux/amd64 result -t result



# intercept "bunnyshell-auth" component running in "env-6mrtz3" ns, replace with "bunnyshell-auth" docker container running locally 
# OLD python bunny.py intercept  --environment=env-6mrtz3 --component=bunnyshell-auth  --docker=bunnyshell-auth  --port=5003:5003  -- --separator=+


# do a DRY run
python3 bunny.py intercept --environment=env-54pgok --component=express-app --docker=eaas-demonstrator_express-app --dryrun


# do a RUN
python bunny.py intercept --environment=env-54pgok --component=express-app --docker=bunnyshell-auth
```



docker build -t eaas-demonstrator_express-app .



docker run -P -v `pwd`/templates:/usr/src/app/templates --init -p 3000:3000 eaas-demonstrator_express-app



## FOR DEMOS
- 