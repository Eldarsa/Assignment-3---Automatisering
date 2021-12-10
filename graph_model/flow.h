#pragma once

#include <stdio.h>
#include <memory>

namespace NodeGraphModel {

	class Node;


	class Flow
	{

	public:

		Flow(std::shared_ptr<Node> originNode, std::shared_ptr<Node> targetNode);
		virtual ~Flow();

		void executeTransaction(double transfer);


	private:
		std::weak_ptr<Node> m_originNode;
		std::weak_ptr<Node> m_targetNode;



	};


}

