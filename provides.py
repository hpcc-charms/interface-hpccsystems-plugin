#!/usr/bin/env python3

from charmhelpers.core.hookenv import (
   log,
   CRITICAL,
   ERROR,
   WARNING,
   INFO,
   DEBUG,
   remote_unit,
   relation_get,
   related_units,
   status_set
)

from charms.reactive import (
   hook,
   RelationBase,
   scopes
)

from charms.reactive.bus import (
   set_state,
   get_state,
   remove_state
)

from charms.layer.jujuenv import JujuEnv

class HPCCPluginProvides(RelationBase):

    # Plugin interface is container based so it shouldn't
    # matter which conversation scope to choice. GLOBAL
    # probably is easiest to implement
    scope = scopes.GLOBAL

    @hook('{provides:plugin}-relation-joined')
    def joined(self):
        
        set_state('{relation_name}.joined')
        status_set('active', JujuEnv.STATUS_MSG['PLUGIN_JOINED'])

    @hook('{provides:plugin}-relation-departed')
    def departed(self):
        pass

    @hook('{provides:plugin}-relation-changed')
    def changed(self):
        if self.is_state('{relation_name}.joined'):
           set_state('{relation_name}.available')
           return
         
        conv = self.conversation()
        msg = conv.get_remote('requires_side_msg')
        if msg:
           set_state('{relation_name}.' + msg)
           return
        
