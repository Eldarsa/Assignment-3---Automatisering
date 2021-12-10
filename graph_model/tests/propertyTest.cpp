#include "graphtests.h"

#include <stdio.h>
#include <string>

int propertyTest(void) {

	// Create some nodes
	std::shared_ptr<NodeGraphModel::NodeGraph> graph = std::make_shared<NodeGraphModel::NodeGraph>();
	std::shared_ptr<NodeGraphModel::Node> node1 = graph.get()->createNode();
	std::shared_ptr<NodeGraphModel::Node> node2 = graph.get()->createNode();
	std::shared_ptr<NodeGraphModel::Node> node3 = graph.get()->createNode();
	std::shared_ptr<NodeGraphModel::Node> node4 = graph.get()->createNode();
	std::shared_ptr<NodeGraphModel::Node> node5 = graph.get()->createNode();
	std::shared_ptr<NodeGraphModel::Node> node6 = graph.get()->createNode();

	// Set new name
	node1.get()->setName("Node1");
	node2.get()->setName("Node2");
	node3.get()->setName("Node3");
	node4.get()->setName("Node4");
	node5.get()->setName("Node5");
	node6.get()->setName("Node6");


	if (std::shared_ptr<NodeGraphModel::NodeVariableContainer> vars = node1.get()->variables().lock()) {
		for (int i = 0; i < 100; i++) {
			std::string name = "name" + std::to_string(i);
			vars.get()->createVariable(std::string(name), i);
		}
	}
	else {
		std::cout << "Expired NodeVariableContainer\n";
	}

	



	return 0;
};