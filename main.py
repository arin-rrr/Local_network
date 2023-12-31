class Server:
    servers = []  # список всех серверов

    def __new__(cls, *args, **kwargs):
        a = super().__new__(cls)
        cls.servers.append(a)
        return a

    def __init__(self):
        self.ip = len(self.servers)
        self.buffer = []

    def send_data(self, data):
        for i in Router.rout:
            if self in i.linked:
                i.buffer.append(data)

    def get_data(self):
        a = self.buffer.copy()
        self.buffer.clear()
        return a

    def get_ip(self):
        return self.ip


class Router:
    rout = []  # список всех роутеров

    def __new__(cls, *args, **kwargs):
        a = super().__new__(cls)
        cls.rout.append(a)
        return a

    def __init__(self):
        self.buffer = []  # буфер
        self.linked = []  # список присоединённых серверов

    def link(self, server):
        self.linked.append(server)

    def unlink(self, server):
        self.linked.remove(server)

    def send_data(self):
        for i in self.buffer:
            ip = i.ip
            for j in self.linked:
                if j.ip == ip:
                    j.buffer.append(i)
        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

# пример использования
# router = Router()
# sv_from = Server()
# sv_from2 = Server()
# router.link(sv_from)
# router.link(sv_from2)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data() 
