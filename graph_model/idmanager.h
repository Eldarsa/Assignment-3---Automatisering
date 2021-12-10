#pragma once

#include <vector>
#include <set>
#include <queue>
#include <memory>

namespace NodeGraphModel {

	class IdManager {

		public:

			IdManager();
			virtual ~IdManager();

			int allocateId();
			void freeId(int id);
			bool checkIfUsed(int id);

			std::set<int> usedIDs();

		private:

			int m_counter;
			std::set<int> m_used_ids;
			std::queue<int> m_recyclable_ids;

		};

}
