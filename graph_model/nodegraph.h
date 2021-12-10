#pragma once 

#include <map>
#include <vector>
#include <memory>

#include "idmanager.h"
#include "node.h"


namespace NodeGraphModel {

    class Node;

    using nodeMap = std::map<int, std::shared_ptr<Node>>;
    using nodeList = std::vector<std::weak_ptr<Node>>;

    class NodeGraph : public std::enable_shared_from_this<NodeGraph> {

    public:

        NodeGraph();
        virtual ~NodeGraph();

        std::shared_ptr<Node> createNode();
        std::shared_ptr<Node> getNode(int id);
        std::shared_ptr<Node> insertNode(Node* node);
        void insertNode(std::shared_ptr<Node> node);
        int deleteNode(int id);

        std::weak_ptr<nodeList> getNodeList() { return m_nodeList; }

    private:
        std::unique_ptr<nodeMap> m_nodeMap;
        std::shared_ptr<nodeList> m_nodeList;
        std::unique_ptr<IdManager> m_idmanager;
    };

}