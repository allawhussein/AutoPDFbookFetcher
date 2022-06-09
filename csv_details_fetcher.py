import os

def csv_book_details(book_name, book_author, book_path):#this is what I mean by argument, and passing stuff through it
    if os.path.exists(book_path):
        print('Loading')
        f = open(book_path, "a")  
        f.write('Test1 pass')
        f.close()

    if not os.path.exists(book_path):
        
        # print('pass')             
        os.makedirs(book_path)
        
        print('pass')
        # f = open(book_path, "w") 
        # f.write('Test3 pass')
        # f.close() 

if __name__ == "__main__":
    csv_book_details('BOOK NAME', 'BOOK AUTHOR', 'PATH')#here is a test case, we'll replace these arbitrary values with something useful later on, but the main usage is for anther script, that will pass these details.