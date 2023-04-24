# Topology object is imported from the previously created file binding_topology.py
from binding_topology import topology
# Pyang serialiser are imported
from pyangbind.lib.serialise import pybindIETFXMLEncoder
import pyangbind.lib.pybindJSON as pybindJSON

# A topology is created
topo = topology()
# A first node (node1) is added to the topology
node1=topo.topology.node.add("node1")
# A port (node1portA) is added to node1
node1.port.add("node1portA")
# A second node (node2) is added to the topology
node2=topo.topology.node.add("node2")
# A port (node2portA) is added to node2
node2.port.add("node2portA")
# A first link is added to the topology (link1)
link=topo.topology.link.add("link1")
# node1 is selected as the source for link1
link.source_node = "node1"
# node1 is selected as the target for link1
link.target_node = "node2"
# node1portA is selected as the source port for link1
link.source_port = "node1portA"
# node2portA is selected as the source port for link2
link.target_port = "node2portA"
# Topology is printed as an XML
print(pybindIETFXMLEncoder.serialise(topo))
# Topology is printed as a JSON
print(pybindJSON.dumps(topo))