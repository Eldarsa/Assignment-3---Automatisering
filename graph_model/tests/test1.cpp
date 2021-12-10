#include "graphtests.h"

void test1(void) {


	// Create graph
	std::shared_ptr<NodeGraphModel::NodeGraph> graph = std::make_shared<NodeGraphModel::NodeGraph>();

	// Create node through graph
	std::shared_ptr<NodeGraphModel::Node> node = graph.get()->createNode();

	// Print ID and name
	std::cout << node.get()->id() << std::endl;
	std::cout << node.get()->name() << std::endl;

	// Set new name
	node.get()->setName("Hello");

	// Does the name change?
	std::cout << node.get()->name() << std::endl;

	// Create a node outside graph without ID and insert it
	std::shared_ptr<NodeGraphModel::Node> node2 = std::make_shared<NodeGraphModel::Node>();
	graph.get()->insertNode(node2);

	// Get the same node using the id from the original
	auto same_node2 = graph.get()->getNode(node2.get()->id());

	//Do the nodes have the same ID?
	std::cout << node2.get()->id() << std::endl;
	std::cout << same_node2.get()->id() << std::endl;

	// Change name and check that the other name is changed as well
	same_node2.get()->setName("It worked?");
	std::cout << node2.get()->name() << std::endl;


	// Every test ran ok!
}