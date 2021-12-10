#pragma once 


#include <stdio.h>
#include <string>
#include <vector>
#include <memory>

#include "nodegraph.h"
#include "nodevariablecontainer.h"

namespace NodeGraphModel {

	class NodeGraph;
	class NodeVariableContainer;

	class Node : public std::enable_shared_from_this<Node> {

	public:

		Node();
		virtual ~Node();

		int id() { return m_id; };

		std::string name() { return m_name; };
		void setName(std::string name) { m_name = name; };


		std::weak_ptr<NodeVariableContainer> variables() { return m_variables; };

	protected:
		void setId(int id) { m_id = id; };
		void setGraph(std::shared_ptr<NodeGraph> graph) { m_graph = graph; };

	private:
		int m_id;
		std::string m_name;
		std::weak_ptr<NodeGraph> m_graph;
		std::shared_ptr<NodeVariableContainer> m_variables;

		friend class NodeGraph; // Makes it possible to access proteccted setID
	};

}