class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    mapping = {}
    for i in range(length):
        ticket = tickets[i]
        mapping[ticket.source] = ticket.destination
    
    route = [None] * (length)
    cur = mapping['NONE']
    for i in range(length):
        route[i] = cur
        cur = mapping[cur]

    return route
