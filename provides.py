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
   status_set,
   flush
)

from charms.reactive import (
   hook,
   RelationBase,
   scopes
)

from charms.reactive.bus import (
   set_state,
   get_state,
   get_states,
   remove_state
)

from charms.layer.jujuenv import JujuEnv

class HPCCPluginsProvides(RelationBase):

    # Plugin interface is container based so it shouldn't
    # matter which conversation scope to choice. GLOBAL
    # probably is easiest to implement
    scope = scopes.GLOBAL

    @hook('{provides:plugin}-relation-joined')
    def joined(self):
        
        conv = self.conversation()
        conv.set_state('{relation_name}.joined')
        status_set('active', 'plugins joined')
        

    @hook('{provides:plugin}-relation-departed')
    def departed(self):
        pass

    @hook('{provides:plugin}-relation-changed')
    def changed(self):
        conv = self.conversation()
       
        if conv.is_state('{relation_name}.joined'):
           conv.remove_state('{relation_name}.joined')
           conv.set_state('{relation_name}.available')
           status_set('active', JujuEnv.STATUS_MSG['PLUGIN_AVAILABLE'])
           return
         
        #conv = self.conversation()
        #msg = conv.get_remote('requires_side_msg')
        #if msg:
        #   set_state('{relation_name}.' + msg)
        #   return
        
