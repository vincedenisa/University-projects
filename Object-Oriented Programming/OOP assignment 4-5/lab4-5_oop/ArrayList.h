#pragma once
#include <functional>
#include <algorithm>

constexpr auto MINIMUM_ARRAY_CAPACITY = 16;
constexpr auto MIN_INT = -2147483648;
constexpr auto MAX_INT = 2147483647;

template <class E>
class ArrayList
{
private:
	int size;
	int memorySize;
	E* elements;

	void resizeIfNeeded(int newSize);
	bool isIndexValid(int index) const;

public:
	ArrayList();
	~ArrayList();
	ArrayList(const ArrayList<E>& fromArrayList);

	void add(const E& element);
	void addAt(const int& index, const E& element);
	void addAll(const ArrayList<E>& fromArrayList);

	bool any(const std::function<bool(const E&)>& selection) const;

	void clear() const;
	bool isEmpty() const;
	int getSize() const;
	bool hasIndex(int index) const;

	bool contains(const E& element) const;

	bool equals(const ArrayList<E>& toArrayList) const;

	int indexOf(const E& element) const;
	int firstIndexOf(const E& element) const;
	int lastIndexOf(const E& element) const;
	int findIndexOf(const std::function<bool(const E&)>& selection) const;

	void set(int index, const E& element);
	const E& get(int index) const;
	const E& getFirst() const;
	const E& getLast() const;
	const E& find(const std::function<bool(const E&)>& selection) const;

	void forEach(const std::function<void(const E&)>& action) const;
	void forEachIndexed(const std::function<void(const E&, int)>& action) const;

	bool remove(const E& element);
	bool removeAt(int index);
	void removeAll(const std::function<bool(const E&)>& selection);

	int countBy(const std::function<bool(const E&)>& selection) const;
	template <typename T>
	const E& maxBy(const std::function<T(const E&)>& selection) const;
	template <typename T>
	const E& minBy(const std::function<T(const E&)>& selection) const;
	template <typename T>
	int sumBy(const std::function<T(const E&)>& selection) const;

	const ArrayList<E>& reversed();
	template <typename T>
	const ArrayList<E>& sortBy(const std::function<T(const E&)>& selection);
	const ArrayList<E>& filter(const std::function<bool(const E&)>& selection);
};