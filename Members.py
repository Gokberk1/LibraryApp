class Members:

    def __init__(self, id, name, surname, email):
        
        if id is None:
            self.id = 0
        else:
            self.id = id

        self.name = name
        self.surname = surname
        self.email = email

    @staticmethod
    def InitMember(obj):
        mList = []
        if isinstance(obj, tuple):
            mList.append(Members(obj[0], obj[1], obj[2], obj[3]))
        else:
            for i in obj:
                mList.append(Members(i[0], i[1], i[2], i[3]))
        return mList