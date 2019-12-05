from charmhelpers.core.hookenv import status_set
from charms.reactive import when, when_not, set_state

@when_not('petclinic.installed')
def install_petclinic():
	set_flag('petclinic.installed')
	status_set('stocazzo')
