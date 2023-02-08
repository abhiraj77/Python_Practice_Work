class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author

class Library:
    def __init__(self,book_list, address):
        self.book_list = book_list
        self.address = address

    def BookCount(self):
        ans = {}
        for i in self.book_list:
            if i.author.upper() in ans.keys():
                ans[i.author.upper()] += 1
            else:
                ans[i.author.upper()] = 1
        return ans

def Test(lib_list, city):
    list = []
    for library in lib_list:
        if library.address["city"].lower() == city.lower():
            books = {}
            for book in library.book_list:
                books[book.id] = book.name
            current_list = sorted(books.values(), key = lambda x: x[0], reverse=True)
        list.extend(current_list)
    return list

library_count = int(input())
library_list = []
for k in range(library_count):
    book_count = int(input())
    book_list = []
    for i in range(book_count):
        id = input()
        name = input()
        author = input()
        book_list.append(Book(id, name, author))
    street = input()
    area = input()
    city = input()
    state = input()
    zip = input()
    address = {}
    address["street"] = street
    address["area"] = area
    address["city"] = city
    address["state"] = state
    address["zip"] = zip
    library_list.append(Library(book_list,address))

author_book_count = []
for library in library_list:
    author_book_count.append(library.BookCount())
    print(author_book_count)
city = input()
print(Test(library_list, city))
'''
3
3
1
Halmet
shakesphere
2
Macbeth
SHAKESPHERE
3
othrllo
Shakesphere
A-10
gomtinagar
lucknow
u.p.
201876
3
1
A Christmas Carol.
Charies Dickens
2
Bleak House
Charies Dickens
3
Oliver Twist
Charies Dickens
A-770
rajamandi
agara
u.p.
2018763
3
1
The adventures of sherlock holmes
sherlock holmes
2
The return of sherlock holmes
sherlock holmes
3
The sign of the four
sherlock holmes
A-660
Khairatabad
lucknow
u.p.
201876
lucknow
'''