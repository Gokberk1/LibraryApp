from dbManager import DbManager
from Books import Books
from Members import Members
from Loans import Loans
from datetime import date, timedelta

class App:
    def __init__(self):
        self.db = DbManager()
        self.db.CheckAndUpdateAvailability()

    def InitApp(self):
        msg = "****\n1-Kitapları Listele\n2-Kitap Ekle\n3-Kitap Güncelle\n4-Kitap Sil\n5-Üyeleri Listele\n6-Üye Kayıt\n7-Üye Güncelle\n8-Üye Sil\n9-Kitap Ödünç Alma\nE-Çıkış"
        while True:
            print(msg)
            islem = input("Seçim:")
            if islem == "1":
                self.DisplayBooks()
            elif islem == "2":
                self.AddBook()
            elif islem == "3":
                self.EditBook()
            elif islem == "4":
                self.DeleteBook()
            elif islem == "5":
                self.DisplayMembers()
            elif islem == "6":
                self.AddMember()
            elif islem == "7":
                self.EditMember()
            elif islem == "8":
                self.DeleteMember()
            elif islem == "9":
                self.LoanBook()
            elif islem == "E":
                break

    
    def DisplayBooks(self):
        books = self.db.Getbooks()
        for i in books:
            print(f"{i.id} - {i.name}, {i.author}")


    def AddBook(self):
        bookName = input("Kitap Adı: ")
        authorName = input("Yazar İsmi: ")
        book = Books(None, bookName, authorName)
        self.db.AddBook(book)

    
    def EditBook(self):
        self.DisplayBooks()
        bookId = int(input("Hangi kitabı düzenlemek istiyorsunuz? "))
        book = self.db.GetBookById(bookId)
        print(f"Id = {book[0].id} numaralı kitap güncelleniyor: ")
        book[0].name = input("Kitap Adı: ") or book[0].name
        book[0].author = input("Yazar İsmi:") or book[0].author
        self.db.EditBook(book[0])
    
    
    def DeleteBook(self):
        self.DisplayBooks()
        bookId = int(input("Hangi kitabı silmek istiyorsunuz? "))
        self.db.DeleteBook(bookId)


    def DisplayMembers(self):
        members = self.db.GetMembers()
        for i in members:
            print(f"{i.id} - {i.name} {i.surname}")


    def AddMember(self):
        name = input("Üye Adı: ")
        surname = input("Soyadı: ")
        email = input("Eposta Adresi: ")
        member = Members(None, name, surname, email)
        self.db.AddMember(member)


    def EditMember(self):
        self.DisplayMembers()
        memberId = int(input("Hangi üyeyi güncellemek istiyorsunuz? "))
        member = self.db.GetMemberById(memberId)
        print(f"Id = {member[0].id} numaralı üye güncelleniyor: ")
        member[0].name = input("Üye Adı:") or member[0].name 
        member[0].surname = input("Soyadı: ") or member[0].surname
        member[0].email = input("Eposta Adresi: ") or member[0].email
        self.db.EditMember(member[0])

    
    def DeleteMember(self):
        self.DisplayMembers()
        memberId = int(input("Hangi üyeyi silmek istiyorsunuz? "))
        self.db.DeleteMember(memberId)


    def LoanBook(self):
        self.DisplayBooks()
        print("Hangi kitabı ödünç almak istersiniz? ")
        while True:
            bookId = int(input("Kitap Id: "))
            result = self.db.CheckBookAvailability(bookId)
            # print(result)
            if result == True:
                print(f"{bookId} numaralı kitap mevcut, alabilirsiniz.")
                memberId = int(input("Üye Id: "))
                loanDate = date.today()
                returnDate = date.today() + timedelta(days=15)
                loan = Loans(memberId, bookId, loanDate, returnDate)
                print(returnDate)
                self.db.LoanBook(loan)
                self.db.UpdateBookAvailability(bookId, result)
                break
            else:
                print(f"{bookId} numaralı kitap zaten ödünç alınmış. Başka bir kitap seçebilirsiniz.")


        

    


app = App()
app.InitApp()