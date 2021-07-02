class Tools:
    @staticmethod
    def are_same_type(obj1, obj2):
        return type(obj1) == type(obj2)
    
    @staticmethod
    def are_not_same_type(obj1, obj2):
        return not Tools.are_same_type(obj1, obj2)

    @staticmethod
    def is_numeric_type(obj):
        return type(obj) == int or type(obj) == float

    @staticmethod
    def is_not_numeric_type(obj):
        return not Tools.is_numeric_type(obj)

    @staticmethod
    def are_same_length(list1, list2):
        return len(list1) == len(list2)

    @staticmethod
    def are_not_same_length(list1, list2):
        return not Tools.are_same_length(list1, list2)