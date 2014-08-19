import sys
sys.path.insert(0, 'C:/CCMSuite/CCMSuite/')
import ccm
log=ccm.log()
from ccm.lib.actr import *

## The Environment
class MyEnvironment(ccm.Model):
   pass    ## Environment is empty

class MyAgent(ACTR):
    buffer_context=Buffer()
    buffer_DM=Buffer()
    buffer_planning_unit=Buffer()
    buffer_unit_task=Buffer()
    buffer_method=Buffer()
    buffer_operator=Buffer()
    DM=Memory(buffer_DM)

    def init():
        DM.add('planning_unit:New Planning Unit cuelag:none cue:start unit_task:New Unit Task')


##Initial Model Behaviours
        pass    ## No initial model behaviours
    
## Planning Units

    def New Planning Unit(Firing Condition,
):
        Behaviour
    
## Unit Tasks

    def New Unit Task(Firing Condition,
):
        Behaviour
    
## Methods

    def New Method(Firing Condition,
):
        Behaviour
    
## Operators 

    def New Operator(Firing Condition,
):
        Behaviour

## Global productions for retrieving Unit Tasks from DM

    def request_next_unit_task(b_plan_unit='planning_unit:?planning_unit cuelag:?cuelag cue:?cue unit_task:?unit_task state:running', b_unit_task='unit_task:?unit_task state:finished'):
        DM.request('planning_unit:?planning_unit cue:?unit_task unit_task:? cuelag:?cue')
        b_plan_unit.set('planning_unit:?planning_unit cuelag:?cuelag cue:?cue unit_task:?unit_task state:retrieve')

    def retrieve_next_unit_task(b_plan_unit='state:retrieve', b_DM='planning_unit:?planning_unit cuelag:?cuelag cue:?cue!finished unit_task:?unit_task'):
        b_plan_unit.set('planning_unit:?planning_unit cuelag:?cuelag cue:?cue unit_task:?unit_task state:running')
        b_unit_task.set('unit_task:?unit_task state:start')

    def last_unit_task(b_unit_task='unit_task:finished state:start', b_plan_unit='planning_unit:?planning_unit'):
        b_unit_task.set('stop')

## Code to run the model
tim = MyAgent()
env = MyEnvironment()
env.agent = tim
ccm.log_everything(env)

env.run()
ccm.finished()
