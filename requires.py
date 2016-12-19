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
    get_state,
    set_state,
    remove_state
)

from charms.layer.jujuenv import JujuEnv


class HPCCPluginRequires(RelationBase):
    scope = scopes.GLOBAL

    @hook('{requires:plugin}-relation-joined')
    def joined(self):
        set_state('{relation_name}.joined')
        status_set('active', JujuEnv.STATUS_MSG['PLUGIN_JOINED'])

    @hook('{requires:hpcc-plugin}-relation-{changed}')
    def changed(self):
        if is_state('{relation_name}.joined'):
           set_state('{relation_name}.available')
           return

        conv = self.conversation()
        msg = conv.get_remote('provides_side_msg')
        if action:
           set_state('{relation_name}.' +msg)
           return

    @hook('{requires:pluin}-relation-departed')
    def departed(self):
        pass
