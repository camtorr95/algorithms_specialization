# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def get_test_cases():
    case_1 = [
        Query('add 911 police'.split()),
        Query('add 76213 Mom'.split()),
        Query('add 17239 Bob'.split()),
        Query('find 76213'.split()),
        Query('find 910'.split()),
        Query('find 911'.split()),
        Query('del 910'.split()),
        Query('del 911'.split()),
        Query('find 911'.split()),
        Query('find 76213'.split()),
        Query('add 76213 daddy'.split()),
        Query('find 76213'.split())
    ]
    case_2 = [
        Query('find 3839442'.split()),
        Query('add 123456 me'.split()),
        Query('add 0 granny'.split()),
        Query('find 0'.split()),
        Query('find 123456'.split()),
        Query('del 0'.split()),
        Query('del 0'.split()),
        Query('find 0'.split())
    ]
    return [case_1, case_2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    phonebook = {}

    results = []

    for query in queries:
        if query.type == 'add':
            phonebook[query.number] = query.name
        elif query.type == 'del':
            if query.number in phonebook:
                del phonebook[query.number]
        elif query.type == 'find':
            if query.number in phonebook:
                results.append(phonebook[query.number])
            else:
                results.append('not found')
        else:
            raise Exception('Unknown query type')

    return results


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
