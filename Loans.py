class Loans:
    
    def __init__(self, memberId, bookId, loanDate, returnDate):
        self.memberId = memberId
        self.bookId = bookId
        self.loanDate = loanDate
        self.returnDate = returnDate

    # @staticmethod
    # def InitLoans(obj):
    #     lList = []
    #     if isinstance(obj, tuple):
    #         lList.append(Loans(obj[1], obj[2], obj[3], obj[4]))
    #     else:
    #         for i in obj:
    #             lList.append(Loans(i[1], i[2], i[3], i[4]))

    #     return lList
