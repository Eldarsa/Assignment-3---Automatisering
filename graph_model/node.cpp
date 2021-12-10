#include "node.h"
#include "nodevariablecontainer.h"

#include <memory>
#include <vector>

namespace NodeGraphModel {

	Node::Node() :
		m_id(),
		m_name(),
		m_variables(std::make_unique<NodeVariableContainer>())
	{

	}

	Node::~Node()
	{
	}

}