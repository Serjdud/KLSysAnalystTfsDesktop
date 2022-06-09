import json


class WiqlQuery:
    def __init__(self, query_name: str, query_dict: dict):
        self.query_name = query_name
        self.query = self.parse_json_query(query_dict)

    def parse_json_query(self, query_dict: dict) -> str:
        query = []
        for keyword, value in query_dict.items():
            if type(value) is list:
                if keyword.upper() in ['SELECT', 'ORDER BY']:
                    delimiter = ', '
                else:
                    delimiter = ' '
                body = delimiter.join(value)
            else:
                body = str(value)
            query.append(f"{keyword} {body}")
        return ' '.join(query)

    def __repr__(self) -> str:
        return self.query_name

    def __str__(self) -> str:
        return self.query_name


class Queries:
    def __init__(self, queries_dict: dict=None, json_filename: str=None):
        if queries_dict and not json_filename:
            pass
        elif json_filename and not queries_dict:
            with open(json_filename) as _queries_file:
                queries_dict = json.load(_queries_file)
        else:
            raise ValueError('One argument must be submitted: query_name or workitems')

        self.queries = {}
        for query_name, query in queries_dict.items():
            self.queries[query_name] = WiqlQuery(query_name, query)

    def __getitem__(self, query_name: str) -> str:
        return self.queries[query_name].query

    def __repr__(self) -> str:
        return ', '.join(self.queries.keys())

    def __str__(self) -> str:
        return ', '.join(self.queries.keys())


QUERIES = Queries(json_filename='configs/queries.json')
