import os

def csv_book_details():

    book_name = 'BOOK NAME' + '.txt'
    book_path = os.path.join('C:\\Users\\LenovoPc\\Desktop\\CSV Book_Details', book_name)



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
