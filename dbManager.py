import mysql.connector
from Connection import connection
from Members import Members
from Books import Books
from Loans import Loans
from datetime import date

class DbManager:

    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    
    #Get books
    def Getbooks(self):
        sql = "SELECT * FROM books"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Books.InitBook(obj)
        except mysq.connection.Error() as err:
            print("hata: ", err)

        
    def GetBookById(self, id):
        sql = "SELECT * FROM books WHERE id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Books.InitBook(obj)
        except mysql.connection.Error() as err:
            print("hata: ", err)


    #Add books to database
    def AddBook(self, book: Books):
        sql = "INSERT INTO books (name, author) VALUES (%s,%s)"
        value = (book.name, book.author)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} adet kitap veritabanına eklendi.")
        except mysq.connection.Error() as err:
            print("hata: ", err)


    #Edit book
    def EditBook(self, book: Books):
        sql = "UPDATE books SET name=%s, author=%s where id=%s"
        value = (book.name, book.author, book.id)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} adet kitap güncellendi.")
        except mysql.connection.Error() as err:
            print("hata", err)


    def DeleteBook(self,id):
        sql = "DELETE FROM books where id=%s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} kitap silindi")
        except mysql.connection.Error() as err:
            print("hata: ", err)


    #check is book available
    def CheckBookAvailability(self,id):
        sql = "SELECT isAvailable FROM books WHERE id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try: 
            obj = self.cursor.fetchone()
            return Books.IsBookAvailable(obj)
        except mysql.connection.Error() as err:
            print("hata: ", err)


    #loan
    def LoanBook(self, loan: Loans):
        sql = "INSERT INTO loans (memberId, bookId, loanDate, returnDate) VALUES (%s,%s,%s,%s)"
        value = (loan.memberId, loan.bookId, loan.loanDate, loan.returnDate)
        self.cursor.execute(sql, value)
        try: 
            self.connection.commit()
            print(f"{self.cursor.rowcount} kitap ödünç verildi")
        except mysql.connection.Error() as err:
            print("hata:", err)


    #update is available
    def UpdateBookAvailability(self, bookId, isAvailable):
        sql = "UPDATE books SET isAvailable = %s WHERE id = %s"
        value = (not isAvailable, bookId)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
        except mysql.connection.Error() as err:
            print("hata:", err) 
        


    def CheckAndUpdateAvailability(self):
        updateSql = "UPDATE books SET isAvailable = TRUE WHERE id IN (SELECT bookId FROM loans WHERE returnDate <= %s)"
        value = (date.today(),)
        self.cursor.execute(updateSql, value)

        deleteSql = "DELETE FROM loans WHERE returnDate <= %s"
        self.cursor.execute(deleteSql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} kitabın durumu güncellendi")
        except mysql.connector.Error() as err:
            print("hata", err)


    #Get members
    def GetMembers(self):
        sql = "SELECT * FROM members"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Members.InitMember(obj)
        except mysql.connection.Error() as err:
            print("hata: ", err)


    #Get member by id
    def GetMemberById(self,id):
        sql = "SELECT * FROM members where id=%s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Members.InitMember(obj)
        except mysql.connection.Error() as err:
            print("hata: ", err)


    #Add member to database
    def AddMember(self, member: Members):
        sql = "INSERT INTO members (name, surname, email) VALUES (%s,%s,%s)"
        value = (member.name, member.surname, member.email)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} kişi kaydedildi.")
        except mysql.connection.Error() as err:
            print("hata: ", err)

    
    def EditMember(self, member: Members):
        sql = "UPDATE members SET name=%s, surname=%s, email=%s where id=%s"
        value = (member.name, member.surname, member.email, member.id)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} kişi güncellendi")
        except mysql.connection.Error() as err:
            print("hata: ", err)


    def DeleteMember(self, id):
        sql = "DELETE FROM members WHERE id=%s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} üye silindi")
        except mysql.connector.Error() as err:
            print("hata", err)



   
    



