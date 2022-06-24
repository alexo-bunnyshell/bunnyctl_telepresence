# Wrapper for telepresence with Bunnyshell

## Known issues
- connections from replaced container to remote container not working
- need to handle multi container pods
- need to handle docker extra args


## usage
python3 -m venv telepresence-demo
source telepresence-demo/bin/activate

# have kubectl running, connected to the cluster

# install telepresence
python bunny.py telepresence_install

# build the local container for "result"
docker build --platform=linux/amd64 result -t result



# intercept "bunnyshell-auth" component running in "env-6mrtz3" ns, replace with "bunnyshell-auth" docker container running locally 
python bunny.py intercept  --environment=env-6mrtz3 --component=bunnyshell-auth  --docker=bunnyshell-auth  --port=5003:5003  -- --separator=+