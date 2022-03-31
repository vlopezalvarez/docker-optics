# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class yc_port_topology__topology_node_port(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module topology - based on the path /topology/node/port. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__port_id','__layer_protocol_name',)

  _yang_name = 'port'
  _yang_namespace = 'urn:topology'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__port_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)
    self.__layer_protocol_name = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ETH': {}, 'OPTICAL': {}},), is_leaf=True, yang_name="layer-protocol-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='layer-protocol-name', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['topology', 'node', 'port']

  def _get_port_id(self):
    """
    Getter method for port_id, mapped from YANG variable /topology/node/port/port_id (string)
    """
    return self.__port_id
      
  def _set_port_id(self, v, load=False):
    """
    Setter method for port_id, mapped from YANG variable /topology/node/port/port_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)""",
        })

    self.__port_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_id(self):
    self.__port_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)


  def _get_layer_protocol_name(self):
    """
    Getter method for layer_protocol_name, mapped from YANG variable /topology/node/port/layer_protocol_name (layer-protocol-name)
    """
    return self.__layer_protocol_name
      
  def _set_layer_protocol_name(self, v, load=False):
    """
    Setter method for layer_protocol_name, mapped from YANG variable /topology/node/port/layer_protocol_name (layer-protocol-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_layer_protocol_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_layer_protocol_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ETH': {}, 'OPTICAL': {}},), is_leaf=True, yang_name="layer-protocol-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='layer-protocol-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """layer_protocol_name must be of a type compatible with layer-protocol-name""",
          'defined-type': "topology:layer-protocol-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ETH': {}, 'OPTICAL': {}},), is_leaf=True, yang_name="layer-protocol-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='layer-protocol-name', is_config=True)""",
        })

    self.__layer_protocol_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_layer_protocol_name(self):
    self.__layer_protocol_name = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ETH': {}, 'OPTICAL': {}},), is_leaf=True, yang_name="layer-protocol-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='layer-protocol-name', is_config=True)

  port_id = __builtin__.property(_get_port_id, _set_port_id)
  layer_protocol_name = __builtin__.property(_get_layer_protocol_name, _set_layer_protocol_name)


  _pyangbind_elements = OrderedDict([('port_id', port_id), ('layer_protocol_name', layer_protocol_name), ])


class yc_node_topology__topology_node(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module topology - based on the path /topology/node. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__node_id','__port',)

  _yang_name = 'node'
  _yang_namespace = 'urn:topology'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__node_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="node-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)
    self.__port = YANGDynClass(base=YANGListType("port_id",yc_port_topology__topology_node_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-id', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['topology', 'node']

  def _get_node_id(self):
    """
    Getter method for node_id, mapped from YANG variable /topology/node/node_id (string)
    """
    return self.__node_id
      
  def _set_node_id(self, v, load=False):
    """
    Setter method for node_id, mapped from YANG variable /topology/node/node_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_node_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_node_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="node-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """node_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="node-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)""",
        })

    self.__node_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_node_id(self):
    self.__node_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="node-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /topology/node/port (list)
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /topology/node/port (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("port_id",yc_port_topology__topology_node_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-id', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("port_id",yc_port_topology__topology_node_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-id', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=YANGListType("port_id",yc_port_topology__topology_node_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-id', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)

  node_id = __builtin__.property(_get_node_id, _set_node_id)
  port = __builtin__.property(_get_port, _set_port)


  _pyangbind_elements = OrderedDict([('node_id', node_id), ('port', port), ])


class yc_link_topology__topology_link(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module topology - based on the path /topology/link. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__link_id','__source_node','__target_node','__source_port','__target_port',)

  _yang_name = 'link'
  _yang_namespace = 'urn:topology'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__link_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)
    self.__source_node = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="source-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)
    self.__target_node = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)
    self.__source_port = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="source-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)
    self.__target_port = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['topology', 'link']

  def _get_link_id(self):
    """
    Getter method for link_id, mapped from YANG variable /topology/link/link_id (string)
    """
    return self.__link_id
      
  def _set_link_id(self, v, load=False):
    """
    Setter method for link_id, mapped from YANG variable /topology/link/link_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)""",
        })

    self.__link_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_id(self):
    self.__link_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:topology', defining_module='topology', yang_type='string', is_config=True)


  def _get_source_node(self):
    """
    Getter method for source_node, mapped from YANG variable /topology/link/source_node (leafref)
    """
    return self.__source_node
      
  def _set_source_node(self, v, load=False):
    """
    Setter method for source_node, mapped from YANG variable /topology/link/source_node (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_node is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_node() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="source-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_node must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="source-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)""",
        })

    self.__source_node = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_node(self):
    self.__source_node = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="source-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)


  def _get_target_node(self):
    """
    Getter method for target_node, mapped from YANG variable /topology/link/target_node (leafref)
    """
    return self.__target_node
      
  def _set_target_node(self, v, load=False):
    """
    Setter method for target_node, mapped from YANG variable /topology/link/target_node (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_node is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_node() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="target-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_node must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)""",
        })

    self.__target_node = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_node(self):
    self.__target_node = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)


  def _get_source_port(self):
    """
    Getter method for source_port, mapped from YANG variable /topology/link/source_port (leafref)
    """
    return self.__source_port
      
  def _set_source_port(self, v, load=False):
    """
    Setter method for source_port, mapped from YANG variable /topology/link/source_port (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_port() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="source-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_port must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="source-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)""",
        })

    self.__source_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_port(self):
    self.__source_port = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="source-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)


  def _get_target_port(self):
    """
    Getter method for target_port, mapped from YANG variable /topology/link/target_port (leafref)
    """
    return self.__target_port
      
  def _set_target_port(self, v, load=False):
    """
    Setter method for target_port, mapped from YANG variable /topology/link/target_port (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_port() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="target-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_port must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)""",
        })

    self.__target_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_port(self):
    self.__target_port = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:topology', defining_module='topology', yang_type='leafref', is_config=True)

  link_id = __builtin__.property(_get_link_id, _set_link_id)
  source_node = __builtin__.property(_get_source_node, _set_source_node)
  target_node = __builtin__.property(_get_target_node, _set_target_node)
  source_port = __builtin__.property(_get_source_port, _set_source_port)
  target_port = __builtin__.property(_get_target_port, _set_target_port)


  _pyangbind_elements = OrderedDict([('link_id', link_id), ('source_node', source_node), ('target_node', target_node), ('source_port', source_port), ('target_port', target_port), ])


class yc_topology_topology__topology(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module topology - based on the path /topology. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__node','__link',)

  _yang_name = 'topology'
  _yang_namespace = 'urn:topology'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__node = YANGDynClass(base=YANGListType("node_id",yc_node_topology__topology_node, yang_name="node", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='node-id', extensions=None), is_container='list', yang_name="node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)
    self.__link = YANGDynClass(base=YANGListType("link_id",yc_link_topology__topology_link, yang_name="link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='link-id', extensions=None), is_container='list', yang_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['topology']

  def _get_node(self):
    """
    Getter method for node, mapped from YANG variable /topology/node (list)
    """
    return self.__node
      
  def _set_node(self, v, load=False):
    """
    Setter method for node, mapped from YANG variable /topology/node (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_node is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_node() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("node_id",yc_node_topology__topology_node, yang_name="node", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='node-id', extensions=None), is_container='list', yang_name="node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """node must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("node_id",yc_node_topology__topology_node, yang_name="node", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='node-id', extensions=None), is_container='list', yang_name="node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)""",
        })

    self.__node = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_node(self):
    self.__node = YANGDynClass(base=YANGListType("node_id",yc_node_topology__topology_node, yang_name="node", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='node-id', extensions=None), is_container='list', yang_name="node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)


  def _get_link(self):
    """
    Getter method for link, mapped from YANG variable /topology/link (list)
    """
    return self.__link
      
  def _set_link(self, v, load=False):
    """
    Setter method for link, mapped from YANG variable /topology/link (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("link_id",yc_link_topology__topology_link, yang_name="link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='link-id', extensions=None), is_container='list', yang_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("link_id",yc_link_topology__topology_link, yang_name="link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='link-id', extensions=None), is_container='list', yang_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)""",
        })

    self.__link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link(self):
    self.__link = YANGDynClass(base=YANGListType("link_id",yc_link_topology__topology_link, yang_name="link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='link-id', extensions=None), is_container='list', yang_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='list', is_config=True)

  node = __builtin__.property(_get_node, _set_node)
  link = __builtin__.property(_get_link, _set_link)


  _pyangbind_elements = OrderedDict([('node', node), ('link', link), ])


class topology(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module topology - based on the path /topology. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Basic example of network topology
  """
  __slots__ = ('_path_helper', '_extmethods', '__topology',)

  _yang_name = 'topology'
  _yang_namespace = 'urn:topology'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__topology = YANGDynClass(base=yc_topology_topology__topology, is_container='container', yang_name="topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return []

  def _get_topology(self):
    """
    Getter method for topology, mapped from YANG variable /topology (container)
    """
    return self.__topology
      
  def _set_topology(self, v, load=False):
    """
    Setter method for topology, mapped from YANG variable /topology (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_topology is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_topology() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_topology_topology__topology, is_container='container', yang_name="topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """topology must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_topology_topology__topology, is_container='container', yang_name="topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='container', is_config=True)""",
        })

    self.__topology = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_topology(self):
    self.__topology = YANGDynClass(base=yc_topology_topology__topology, is_container='container', yang_name="topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:topology', defining_module='topology', yang_type='container', is_config=True)

  topology = __builtin__.property(_get_topology, _set_topology)


  _pyangbind_elements = OrderedDict([('topology', topology), ])


