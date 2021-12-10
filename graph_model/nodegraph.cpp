#include "nodegraph.h"

namespace NodeGraphModel {

	NodeGraph::NodeGraph() :
		m_nodeMap(std::make_unique<nodeMap>()),
		m_nodeList(std::make_shared<nodeList>()),
		m_idmanager(std::make_unique<IdManager>())
	{
	}

	NodeGraph::~NodeGraph()
	{
	}

	std::shared_ptr<Node> NodeGraph::createNode()
	{
		// 1. Get new id from idManager
		int new_id = m_idmanager.get()->allocateId();

		// 2. Create new node
		std::shared_ptr<Node> new_node(new Node);
		new_node.get()->setId(new_id);
		new_node.get()->setGraph(this->shared_from_this());
		new_node.get()->setName("NoNameYet");

		// 3. Add to map and list
		std::pair<int, std::shared_ptr<Node>> new_pair(new_id, new_node);
		m_nodeMap.get()->insert(new_pair);
		m_nodeList.get()->push_back(new_node);

		return new_node;
	}

	std::shared_ptr<Node> NodeGraph::getNode(int id)
	{
		nodeMap::iterator it = m_nodeMap.get()->find(id);
		if (it != m_nodeMap.get()->end()) {
			return it->second;
		}
		else {
			return nullptr;
		}
	}

	std::shared_ptr<Node> NodeGraph::insertNode(Node* node)
	{
		int new_id = m_idmanager.get()->allocateId();
		node->setId(new_id);
		node->setGraph(this->shared_from_this());

		std::shared_ptr<Node> new_node(node);

		std::pair<int, std::shared_ptr<Node>> new_pair(new_id, new_node);
		m_nodeMap.get()->insert(new_pair);
		m_nodeList.get()->push_back(std::weak_ptr<Node>(new_node));

		return new_node;
	}

	void NodeGraph::insertNode(std::shared_ptr<Node> node)
	{
		int new_id = m_idmanager.get()->allocateId();
		node.get()->setId(new_id);
		node.get()->setGraph(this->shared_from_this());

		std::pair<int, std::shared_ptr<Node>> new_pair(new_id, node);
		m_nodeMap.get()->insert(new_pair);
		m_nodeList.get()->push_back(std::weak_ptr<Node>(node));

		return;
	}

	int NodeGraph::deleteNode(int id)
	{

		if (m_nodeMap.get()->erase(id)) {

			// TODO: Remove from vector as well

			m_idmanager.get()->freeId(id);
		};

		return 0;
	}

}