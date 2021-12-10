#include "idmanager.h"

namespace NodeGraphModel {

	IdManager::IdManager()
	{
		m_counter = 1;
	}

	IdManager::~IdManager()
	{
	}

	int IdManager::allocateId()
	{
		int new_id;
		if (m_recyclable_ids.empty()) {
			new_id = m_counter;
			m_counter++;
		}
		else {
			new_id = m_recyclable_ids.front();
			m_recyclable_ids.pop();
		}

		return new_id;
	}

	void IdManager::freeId(int id)
	{
		if (m_used_ids.erase(id)) {
			m_recyclable_ids.push(id);
		}
	}

	bool IdManager::checkIfUsed(int id)
	{
		return(m_used_ids.find(id) != m_used_ids.end());
	}

	std::set<int> IdManager::usedIDs()
	{
		return m_used_ids;
	}

}