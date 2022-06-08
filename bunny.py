import fire
import shutil
import os
import subprocess
import json


import constants

def hello(name):
  print (constants.TELEPRESENCE_BINARY)
  return 'Hello {name}!'.format(name=name)



class Bunnydev(object):

  # def __init__(self, environment, component, docker, container=None,):
  #   self._environment = environment
  #   self._component = component
  #   self._container = container
  #   self._docker = docker

  def hello(name):
    print (constants.TELEPRESENCE_BINARY)
    return 

  # def run(self, environment, component, docker, container=None, *docker_args, **kwargs):
  # def run(self, environment, component, docker, container=None, **kwargs):
  def intercept(self, environment, component, docker, container=None, *docker_args):
    self._environment = environment
    self._component = component
    self._container = container
    self._docker = docker
    self._docker_args = ""
    # self._docker_args = docker_args

    print(f'docker_args: {docker_args}')
    # print(f'kwargs: {kwargs}')

    if not self.telepresence_check_is_installed():
      self.telepresence_install()

    if not self.telepresence_check_is_installed(silent=True):
      return 

    if not self.k8s_check_connection():
      return

    self.telepresence_connect()
    self.telepresence_intercept()

    print("done")

  def telepresence_check_is_installed(self, silent=False):
    return True
    install_path = shutil.which("telepresence")
    if install_path:
      if not silent:
        print(f'telepresence installed at {install_path}')
      return install_path

    if not silent:
      print ('telepresence is not installed')
    return False

  def telepresence_install(self):
    print("install telepresence")
    print("curl -fL https://app.getambassador.io/download/tel2/linux/amd64/latest/telepresence -o telepresence")
    print("chmod a+x telepresence")

  def k8s_check_connection(self):
    kubectl_path = shutil.which("kubectl")
    if kubectl_path:
      print(f'kubectl installed at {kubectl_path}')
      return kubectl_path

    print ('kubectl is not installed')
    return False


    os.system("kubectl cluste_info ")

  def telepresence_connect(self):
    os.system("./telepresence connect")


  def telepresence_intercept(self):

    # build name of env file for this intercept (will be written by telepresence, read by docker)
    env_file_name = f'intercept_{self._environment}_{self._component}.env'
    print(env_file_name)

    kube_service_command=f'kubectl get service {self._component} -n {self._environment} -o yaml | grep \'port:\' | grep -o \'[0-9]*\' | head -1'
    kube_service_command=f'kubectl get service {self._component} -n {self._environment} -o json'
    print(kube_service_command)


    # port=os.popen(kube_service_command).read().strip()
    # output=subprocess.check_output(kube_service_command)
    # print(port)
    # os.system(kube_service_command)

    output=os.popen(kube_service_command).read()
    print (output)
    service_json = json.loads(output)
    
    print(service_json['spec']['ports'][0])

    podPort=service_json['spec']['ports'][0]['targetPort']
    servicePort=service_json['spec']['ports'][0]['port']

    print(f'{constants.TELEPRESENCE_BINARY} intercept {self._component} --port {servicePort}:{servicePort} --namespace  {self._environment} -w {self._component} --env-file {env_file_name}')
    print(f'docker-run --rm  {self._docker_args} -e {env_file_name} -p{servicePort}:{podPort} {self._docker}')



    # k describe service result
    # telepresence intercept result --service result -n env-6mrtz3 --port 5001:5001 -w result --env-file intercept-result.env
    # docker run -p 5001:80 -e intercept-result.env bunnyctl-test-repo_result


if __name__ == '__main__':
  fire.Fire(Bunnydev)