# import os

# def csv_book_details(book_name, book_author, book_path, csv_path):#this is what I mean by argument, and passing stuff through it
#     if not os.path.exists(csv_path):

#         exist_ok=False

csv_path = 'C:\\Users\\LenovoPc\\Desktop\\CSV Book_Details\\t.txt'

#         os.makedirs(csv_path)

#         f = open(csv_path, "a")   

#         f.write('Book name: ' + book_name)
#         f.write('\n')

#         f.write('Author name:', book_author)
#         f.write('\n')

#         f.write('Book path:', book_path)
#         f.write('\n')

#         f.close()


#     if os.path.exists(csv_path):
f = open(csv_path, "r") 
f.readline(1)


whattoReturn = "None"
strToFind = 'w'
if strToFind in f:
    whattoReturn = strToFind
    print(whattoReturn)
    f.close() 
    
        

# if __name__ == "__main__":
#     csv_book_details('BOOK NAME', 'BOOK AUTHOR', 'PATH') # here is a test case, we'll replace these arbitrary values with something useful later on, but the main usage is for anther script, that will pass these details.