def sum_digits(num):
    """
    This function takes a two-digit number as input and returns the sum of its digits.
    """
    return num // 10 + num % 10

def check_id_valid(id_number):
    """
    This function checks if a given ID number is valid according to a specific algorithm.
    It takes an ID number as input and returns True if the ID is valid, False otherwise.
    """
    id_lst = list(str(id_number))
    id_lst = [int(id_num) * (2 if (i+1) % 2 == 0 else 1) for i, id_num in enumerate(id_lst)]
    check_sum = sum(sum_digits(num) for num in id_lst)

    return check_sum % 10 == 0

class IDIterator:
    """
    This is an iterator class for generating valid ID numbers.
    """
    def __init__(self, start_id):
        self.current_id = start_id

    def __iter__(self):
        return self

    def __next__(self):
        """
        This method generates the next valid ID number.
        It raises a StopIteration exception if no valid ID number is found before reaching 999999999.
        """
        if self.current_id > 999999999:
            raise StopIteration
        
        while not check_id_valid(self.current_id):
            self.current_id += 1
            if self.current_id > 999999999:
                raise StopIteration
        valid_id = self.current_id
        self.current_id += 1
        return valid_id

def id_generator(start_id):
    """
    This is a generator function for generating valid ID numbers.
    It takes a starting ID number as input and yields valid ID numbers one by one.
    """
    id = start_id
    while id < 999999999:
        while not check_id_valid(id):
            id += 1
            if id > 999999999:
                raise StopIteration
        yield id
        id += 1

def main():
    id = int(input("Enter ID: "))
    iter_or_gen = input("Enter Iterator or Generator (it/gen): ")
    iterator = None
    if iter_or_gen.lower() == "it":
        iterator = IDIterator(id)
    else:
        iterator = id_generator(id)
    for i in range(10):
        print(next(iterator))

if __name__ == '__main__':
    main()