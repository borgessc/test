kapacitor
==============

Ansible role to install and configure Kapacitor. You may also be interested in
- [layer2pty.telegraf]
- [layer2pty.influxdb]


## Example

```
- hosts: myhost

  vars:
    kapacitor_version: 0.13.0-1

  roles:
    - layer2pty.kapacitor
```


## Testing

To run this role's integration tests

```
kitchen test
```


## Dependencies

none

*Note:*
An issue encountered while testing alert notification via email has been raised.
(https://github.com/influxdata/kapacitor/issues/602)
