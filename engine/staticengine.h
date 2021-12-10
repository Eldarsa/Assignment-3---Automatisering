#pragma once

#include "nodegraph.h"
#include "flow.h"

#include <memory>

namespace Engine {


	class StaticEngine
	{

		StaticEngine();
		virtual ~StaticEngine();

	public:

		int attachNodeGraph(std::shared_ptr<NodeGraphModel::NodeGraph> nodeGraph);
		int detachNodeGraph();

	private:
		std::shared_ptr<NodeGraphModel::NodeGraph> m_originalGraph;
		std::unique_ptr<NodeGraphModel::NodeGraph> m_shadowGraph;
	};

}
