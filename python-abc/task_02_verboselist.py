#!/usr/bin/python3


class VerboseList(list):


    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
         item = self[index]
         print(f"Popped [{item}] from the list.")
         return super().pop(index)
        
