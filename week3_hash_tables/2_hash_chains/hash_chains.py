# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


def get_test_queries():
    case_1 = [
        Query('add world'.split()),
        Query('add HellO'.split()),
        Query('check 4'.split()),
        Query('find World'.split()),
        Query('find world'.split()),
        Query('del world'.split()),
        Query('check 4'.split()),
        Query('del HellO'.split()),
        Query('add luck'.split()),
        Query('add GooD'.split()),
        Query('check 2'.split()),
        Query('del good'.split())
    ]
    case_2 = [
        Query('add test'.split()),
        Query('add test'.split()),
        Query('find test'.split()),
        Query('del test'.split()),
        Query('find test'.split()),
        Query('find Test'.split()),
        Query('add Test'.split()),
        Query('find Test'.split())
    ]
    return [case_1, case_2]


class ChainList:
    def __init__(self):
        self.members = set()
        self.sequence = list()

    def add(self, s: str):
        if s not in self.members:
            self.members.add(s)
            self.sequence.append(s)

    def remove(self, s: str):
        if s in self.members:
            self.members.remove(s)
            self.sequence.remove(s)

    def find(self, s: str):
        return s in self.members


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        for _ in range(bucket_count):
            self.elems.append(ChainList())

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    @staticmethod
    def write_search_result(was_found):
        print('yes' if was_found else 'no')

    @staticmethod
    def write_chain(chain):
        print(' '.join(reversed(chain)))

    @staticmethod
    def read_query():
        return Query(input().split())

    def process_query(self, query):
        if query.type == 'add':
            self.elems[self._hash_func(query.s)].add(query.s)
        elif query.type == 'del':
            self.elems[self._hash_func(query.s)].remove(query.s)
        elif query.type == 'find':
            self.write_search_result(self.elems[self._hash_func(query.s)].find(query.s))
        elif query.type == 'check':
            self.write_chain(self.elems[query.ind].sequence)
        else:
            raise Exception('Unknown query type: {}'.format(query.type))

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
