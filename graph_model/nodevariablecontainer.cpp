#include "nodevariablecontainer.h"

#include "boost/any.hpp"

#include <map>
#include <memory>

namespace NodeGraphModel {

	NodeVariableContainer::NodeVariableContainer() :
		m_lookupTable(std::make_unique<std::map<std::string, int>>()),
		m_boolContainer(std::make_unique<boolMap>()),
		m_intContainer(std::make_unique<intMap>()),
		m_doubleContainer(std::make_unique<doubleMap>())
	{
	}

	NodeVariableContainer::~NodeVariableContainer()
	{
	}

	std::shared_ptr<VariableValue<bool>> NodeVariableContainer::createVariable(std::string name, bool value)
	{
		std::shared_ptr<VariableValue<bool>> new_var = std::make_shared<VariableValue<bool>>(value);
		std::pair<std::string, std::shared_ptr<VariableValue<bool>>> new_pair(name, new_var);
		m_boolContainer.get()->insert(new_pair);

		std::pair<std::string, int> ref_pair(name, VarType::BOOL);
		m_lookupTable.get()->insert(ref_pair);

		return new_var;
	}

	std::shared_ptr<VariableValue<int>> NodeVariableContainer::createVariable(std::string name, int value)
	{
		std::shared_ptr<VariableValue<int>> new_var = std::make_shared<VariableValue<int>>(value);
		std::pair<std::string, std::shared_ptr<VariableValue<int>>> new_pair(name, new_var);
		m_intContainer.get()->insert(new_pair);

		std::pair<std::string, int> ref_pair(name, VarType::INT);
		m_lookupTable.get()->insert(ref_pair);

		return new_var;
	}

	std::shared_ptr<VariableValue<double>> NodeVariableContainer::createVariable(std::string name, double value)
	{
		std::shared_ptr<VariableValue<double>> new_var = std::make_shared<VariableValue<double>>(value);
		std::pair<std::string, std::shared_ptr<VariableValue<double>>> new_pair(name, new_var);
		m_doubleContainer.get()->insert(new_pair);

		std::pair<std::string, int> ref_pair(name, VarType::DOUBLE);
		m_lookupTable.get()->insert(ref_pair);

		return new_var;
	}

	boost::any NodeVariableContainer::getVariablePointer(std::string name)
	{
		switch (checkName(name)) {
		case 1: { return m_boolContainer.get()->find(name)->second; }
		case 2: { return m_intContainer.get()->find(name)->second; }
		case 3: { return m_doubleContainer.get()->find(name)->second; }
		default: { return nullptr; }
		}

	}

	int NodeVariableContainer::changeVariableName(std::string oldName, std::string newName)
	{

		switch (int map_idx = checkName(oldName)) {
		case 1:
		{
			std::shared_ptr<VariableValue<bool>> tmp(m_boolContainer.get()->find(oldName)->second);
			std::pair<std::string, std::shared_ptr<VariableValue<bool>>> new_pair(newName, std::move(tmp));
			m_boolContainer.get()->erase(oldName);
			m_boolContainer.get()->insert(new_pair);
			return 0;
		}
		case 2:
		{
			std::shared_ptr<VariableValue<int>> tmp(m_intContainer.get()->find(oldName)->second);
			std::pair<std::string, std::shared_ptr<VariableValue<int>>> new_pair(newName, std::move(tmp));
			m_intContainer.get()->erase(oldName);
			m_intContainer.get()->insert(new_pair);
			return 0;
		}
		case 3:
		{
			std::shared_ptr<VariableValue<double>> tmp(m_doubleContainer.get()->find(oldName)->second);
			std::pair<std::string, std::shared_ptr<VariableValue<double>>> new_pair(newName, std::move(tmp));
			m_doubleContainer.get()->erase(oldName);
			m_doubleContainer.get()->insert(new_pair);
			return 0;
		}
		default: { return 1; }
		}

	}

	int NodeVariableContainer::deleteVariable(std::string name)
	{
		switch (checkName(name)) {
		case 1: { m_boolContainer.get()->erase(name); }
		case 2: { m_intContainer.get()->erase(name); }
		case 3: { m_doubleContainer.get()->erase(name); }
		default: { return 1; } // Didn't exist
		}
		return 0;
	}

	int NodeVariableContainer::checkName(std::string name)
	{

		std::map<std::string, int>::iterator it = m_lookupTable.get()->find(name);
		if (it != m_lookupTable.get()->end()) {
			return it->second;
		}
		else {
			return 0; // Indicates non existent! 
		}
	}

}