import os
path = 'C:\\Users\\LenovoPc\\Desktop\\CSV Book_Details\\'

join = os.path.join(csv_path, 'books.txt')
make = os.makedirs(join)

def csv_book_details(book_name, book_author, book_path, csv_path):#this is what I mean by argument, and passing stuff through it
    if not os.path.exists(csv_path):

        

        
        f = open(make, "a")   

        f.write('Book name: ' + book_name)
        f.write('\n')

        f.write('Author name:', book_author)
        f.write('\n')

        f.write('Book path:', book_path)
        f.write('\n')

        f.close()


    if os.path.exists(make):
        with open(make) as file:
            contents = file.read()
            search_word = input("enter a word you want to search in file: ")
            if search_word in contents:
                print ('word found')
            else:
                print ('word not found')
        


if __name__ == "__main__":
    csv_book_details('BOOK NAME', 'BOOK AUTHOR', 'PATH', 'CSV_PATH') # here is a test case, we'll replace these arbitrary values with something useful later on, but the main usage is for anther script, that will pass these details.