# Overview

This interface layer implements the basic form of the HPCCSystems platform  `hpcc-plugin`
interface protocol, which is used for things like additional programming language
support, such as Java embeded, MySQL embeded, and some services like memcached, kafak,
et cetera.

# Usage

## Provides

By providing the 'hpcc-plugin' interface, your charm install the plugin and 
perform any configuration if needed

metadata.yaml:
provides
  hpcc-plugin:
     interface: plugin

```python
@when('hpcc-plugin.available')
def configure_plugins(hpcc-plugin):
    pass
```


## Requires
By requiring the `hpcc-plugin` interface, your charm  should respond to the
`{relation_name}.available` state, to restart HPCC platform
@when('hpcc-plugin.available')
def restart_hpcc(hpcc-plugin):



