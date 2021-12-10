#pragma once

#include <stdio.h>
#include <memory>
#include <map>
#include <string>
#include <typeinfo>

#include "boost/any.hpp"
#include "node.h"

/* 
   Q: Is really using boost::any the best option?

   A: Up to debate for sure. It could be beneficial to specify some variants we want
      and only use those. For instance that a variable can only be Int, Float64 and bool.
	  However, from the early stage on I find just having all options open and then making 
	  efforts to limit those for convenience later on a more flexible approach. 
*/

namespace NodeGraphModel {

	template<typename T>
	class VariableValue;

	using boolMap = std::map<std::string, std::shared_ptr<VariableValue<bool>>>;
	using intMap = std::map<std::string, std::shared_ptr<VariableValue<int>>>;
	using doubleMap = std::map<std::string, std::shared_ptr<VariableValue<double>>>;

	enum VarType { UNDEFINED, BOOL, INT, DOUBLE };

	class NodeVariableContainer {

	public:
		NodeVariableContainer();
		virtual ~NodeVariableContainer();

		std::shared_ptr<VariableValue<bool>> createVariable(std::string name, bool value);
		std::shared_ptr<VariableValue<int>> createVariable(std::string name, int value);
		std::shared_ptr<VariableValue<double>> createVariable(std::string name, double value);

		boost::any getVariablePointer(std::string name);
		int changeVariableName(std::string oldName, std::string newName);
		int deleteVariable(std::string name);
		// Function for returning all keys?

	private:
		int checkName(std::string name);

	private:
		std::unique_ptr<std::map<std::string, int>> m_lookupTable;	// We use simple ints to id containers
		std::unique_ptr<boolMap> m_boolContainer;					// ID: 1
		std::unique_ptr<intMap> m_intContainer;						// ID: 2
		std::unique_ptr<doubleMap> m_doubleContainer;				// ID: 3
	};

	template<typename T>
	class VariableValue {
	public:

		VariableValue(T value);
		virtual ~VariableValue();

		inline T value() { return m_value; }
		inline void setValue(T val) { m_value = val; }
		
		int registerObserver();
		int unregisterObserver();
		void notifyObservers();

		// TODO: implement "DESCRIPTION"

	private:
		T m_value;
	};

	template<typename T>
	inline VariableValue<T>::VariableValue(T value) :
		m_value(value)
	{
	};

	template<typename T>
	inline VariableValue<T>::~VariableValue()
	{
	};

}