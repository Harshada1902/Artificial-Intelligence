class FuzzySet:
    def __init__(self):
        """
        Initialize an empty fuzzy set.
        """
        self.elements = {}
    
    def add(self, element, membership_degree):
        """
        Add an element to the fuzzy set with a membership degree.
        
        :param element: The element to add
        :param membership_degree: Membership degree (between 0 and 1)
        """
        if 0 <= membership_degree <= 1:
            if membership_degree > 0:
                self.elements[element] = membership_degree
        else:
            raise ValueError("Membership degree must be between 0 and 1")
    
    def remove(self, element):
        """
        Remove an element from the fuzzy set.
        
        :param element: The element to remove
        """
        if element in self.elements:
            del self.elements[element]
    
    def get_membership(self, element):
        """
        Get the membership degree of an element.
        
        :param element: The element to check
        :return: Membership degree (0 if element not in set)
        """
        return self.elements.get(element, 0)
    
    def union(self, other_set):
        """
        Perform union with another fuzzy set.
        
        :param other_set: Another FuzzySet
        :return: A new FuzzySet representing the union
        """
        result = FuzzySet()
        
        # Add elements from first set
        for elem, degree in self.elements.items():
            result.add(elem, degree)
        
        # Add or update elements from second set
        for elem, degree in other_set.elements.items():
            current_degree = result.get_membership(elem)
            result.add(elem, max(current_degree, degree))
        
        return result
    
    def intersection(self, other_set):
        """
        Perform intersection with another fuzzy set.
        
        :param other_set: Another FuzzySet
        :return: A new FuzzySet representing the intersection
        """
        result = FuzzySet()
        
        # Find common elements and take minimum membership
        for elem in set(self.elements) & set(other_set.elements):
            degree = min(
                self.get_membership(elem), 
                other_set.get_membership(elem)
            )
            result.add(elem, degree)
        
        return result
    
    def __str__(self):
        """
        String representation of the fuzzy set.
        
        :return: Formatted string of elements and their degrees
        """
        return "{" + ", ".join(f"{elem}: {degree}" for elem, degree in self.elements.items()) + "}"

# Demonstration of fuzzy set usage
def main():
    # Create fuzzy sets
    fruits1 = FuzzySet()
    fruits1.add("apple", 0.7)
    fruits1.add("banana", 0.3)
    fruits1.add("cherry", 0.9)
    
    fruits2 = FuzzySet()
    fruits2.add("banana", 0.5)
    fruits2.add("cherry", 0.6)
    fruits2.add("date", 0.8)
    
    print("Fruits Set 1:", fruits1)
    print("Fruits Set 2:", fruits2)
    
    # Demonstrate union
    union_set = fruits1.union(fruits2)
    print("\nUnion:", union_set)
    
    # Demonstrate intersection
    intersection_set = fruits1.intersection(fruits2)
    print("Intersection:", intersection_set)
    
    # Check membership
    print("\nMembership of 'apple' in Set 1:", fruits1.get_membership("apple"))
    print("Membership of 'banana' in Set 2:", fruits2.get_membership("banana"))

# Run the demonstration
if __name__ == "__main__":
    main()