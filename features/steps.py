from lettuce import step
from lettuce import world

from echo_client import main


@step('the message (\S+)')
def the_message(step, msg):
	world.message = [str(msg)]

@step('I call main')
def call_main(step):
	world.main = main(world.message)

@step('I receive the message (\w+)')
def compare(step, expected):
	assert world.main == expected, 'Got %s' % expected