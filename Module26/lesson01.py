class MyIter:
    """

    """

    def __init__(self, iterable):
        """

        :param iter_object:
        """
        self.iterable = iterable
        self.end_iter_object = False


    def loop(self, loop_body_func):
        self.iterator = iter(self.iterable)

        while not self.end_iter_object:
            try:
                elem_from_iterator = next(self.iterator)
            except StopIteration:
                self.end_iter_object = False
            else:
                loop_body_func(elem_from_iterator)


my_list = [1, 2, 3, 4, 5]
