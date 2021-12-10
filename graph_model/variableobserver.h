#pragma once

// https://refactoring.guru/design-patterns/observer/cpp/example


template<typename T>
class VariableObserver
{
public:

	virtual ~VariableObserver() {};
	
	virtual void update(const T newValue) = 0;

};


