class Books:

    def __init__(self, id, name, author):
        if id is None:
            self.id = 0
        else:
            self.id = id

        self.name = name
        self.author = author

    @staticmethod
    def InitBook(obj):
        bList = []
        if isinstance(obj, tuple):
            bList.append(Books(obj[0], obj[1], obj[2]))
        else:
            for i in obj:
                bList.append(Books(i[0], i[1], i[2]))
        return bList

    @staticmethod
    def IsBookAvailable(obj):
        info  = True
        if isinstance(obj, tuple):
            if obj[0] == True:
                info = True
            else:
                info = False
        return info
