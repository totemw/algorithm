"""
Design a list with the follwoing methods:

class CustomList {

	/**
	* Constructs a list with the specified length. All elements are initially 0s.
	*/
	public CustomList(int n) {
	}

	/**
	* Replaces the element at the specified position in this list with the specified value.
	*/
	public void set(int index, int value) {
	}

	/**
	* Returns the element at the specified position in this list.
	*/
	public int get(int index) {
	}

	/**
	* Replaces all elements in this list with the specified value.
	*/
	public void setAll(int value) {
	}
}
All methods should work in O(1) time.


class CustomList {

	private int length;
	private Map<Integer, Integer> map;
	private int allValue;

	/**
	* Constructs a list with the specified length. All elements are initially 0s.
	*/
	public CustomList(int n) {
		length = n;
		map = new HashMap<Integer, Integer>;
		allValue = 0;
	}

	/**
	* Replaces the element at the specified position in this list with the specified value.
	*/
	public void set(int index, int value) {
		if (index < 0 || index >= length) {
			throw new RuntimeException("Out of bounds");
		}
		map.put(index, value);
	}

	/**
	* Returns the element at the specified position in this list.
	*/
	public int get(int index) {
		if (index < 0 || index >= length) {
			throw new RuntimeException("Out of bounds");
		}
		Integer check = map.get(index);
		if (check != null) {
			return check;
		} else {
			return allValue;
		}
	}

	/**
	* Replaces all elements in this list with the specified value.
	*/
	public void setAll(int value) {
		map = new HashMap<Integer, Integer>;
		allValue = value;
	}
}
"""