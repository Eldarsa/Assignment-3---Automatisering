#pragma once

#include "nodegraph.h"

#include <stdio.h>
#include <memory>

namespace Engine {

	class DynamicEngine
	{

		DynamicEngine();
		virtual ~DynamicEngine();

	public:
		int attachNodeGraph(std::shared_ptr<NodeGraphModel::NodeGraph> nodeGraph);
		int detachNodeGraph();

		int setSimulationSpeed(); //STEPS PER SECOND
		int setFlushSpeed(); //FPS

		int startSimulation();

	private:
		std::unique_ptr<NodeGraphModel::NodeGraph> m_nodeGraph;

	};
}

