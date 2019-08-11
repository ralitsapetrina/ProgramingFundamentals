class Website:
    def __init__(self, host, domain, queries=None):
        self.host = host
        self.domain = domain
        self.queries = queries

    def format_link(self):
        if self.queries:
            return f"https://www.{self.host}.{self.domain}/query?=[{']&['.join(self.queries)}]"
        else:
            return f"https://www.{self.host}.{self.domain}"


def create_link(data_list):
    if len(data_list) == 3:
        return Website(host=data_list[0], domain=data_list[1], queries=data_list[2].split(','))
    else:
        return Website(host=data_list[0], domain=data_list[1])


websites_list = []

while True:
    data_list = input().split(' | ')
    if data_list[0] == 'end':
        break

    new_website = create_link(data_list)
    websites_list.append(new_website)

for site in websites_list:
    print(site.format_link())