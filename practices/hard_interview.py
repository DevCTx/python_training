class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"

    def get_lst_val(self, lst_val):
        lst_val.append(self.val)
        if self.next is not None:
            self.next.get_lst_val(lst_val)
        return lst_val


def merge_k_linked_lists(linked_lists):
    """
    Merge the given Links recursively incorporated and sorted by value

    :param linked_lists: List of Links with or without next Link
    :return: List of the sorted merged Links.


    >>> print(merge_k_linked_lists([Link(1)]))
    Link(1)

    >>> print(merge_k_linked_lists([Link(2, Link(1))]))
    Link(1, Link(2))

    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2, Link(5))),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4, Link(5)))))

    >>> print(merge_k_linked_lists([
    ...     Link(2, Link(4)),
    ...     Link(2, Link(1)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    """
    values = []  # 0(k*n)

    for link in linked_lists:  # 0(k)
        # lst = []
        # for val in link.get_lst_val(lst):
        #     values.append(val)
        while link:  # 0(n)
            values.append(link.val)
            link = link.next
    values.sort(reverse=True)  # 0(k*n*log(k*n))
    previous_lnk = None
    for val in values:  # 0(k*n)
        lnk = Link(val, previous_lnk)
        previous_lnk = lnk

    return lnk  # 0(k*n*log(k*n))
