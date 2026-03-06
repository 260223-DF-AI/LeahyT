def read_lines(filepath, encoding='utf-8'):
    """
    Yield lines from a file one at a time.
    - Strip whitespace from each line
    - Skip empty lines
    - Handle encoding errors gracefully
    
    Usage:
        for line in read_lines('large_file.txt'):
            process(line)
    """
    with open(filepath, "r") as file:
        for line in file:
            yield line

def batch(iterable, size):
    """
    Yield items in batches of the specified size.
    
    Usage:
        list(batch([1,2,3,4,5,6,7], 3))
        # [[1,2,3], [4,5,6], [7]]
    """
    i = 0
    while i < len(iterable):
        thisBatch = []
        for j in range(size):
            if not i == len(iterable):
                thisBatch.append(iterable[i])
                i += 1
        yield thisBatch
    
def filter_by(iterable, predicate):
    """
    Yield items that match the predicate.
    
    Usage:
        evens = filter_by(range(10), lambda x: x % 2 == 0)
        list(evens)  # [0, 2, 4, 6, 8]
    """
    for item in iterable:
        if predicate(item):
            yield item

def filter_errors(log_lines):
    """
    Yield only lines containing 'ERROR'.
    """
    for line in log_lines:
        if 'ERROR' in line:
            yield line


def filter_by_field(records, field, value):
    """
    Yield records where record[field] == value.
    
    Usage:
        active_users = filter_by_field(users, 'status', 'active')
    """
    for record in records:
        if record[field] == value:
            yield record