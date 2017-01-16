# -*- coding: UTF-8 -*- 

from src import create_agent_app
from src.agentconfig import *

dcos_agent = create_agent_app()

if __name__ == '__main__':
    dcos_agent.debug = DEBUG
    dcos_agent.run(host= HOST,port=PORT)
