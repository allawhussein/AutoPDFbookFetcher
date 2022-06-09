import os


book_name = 'BOOK NAME' + '.txt'
book_path = os.path.join('C:\\Users\\LenovoPc\\Desktop\\CSV Book_Details', book_name)


if os.path.exists(book_path):
    print('The book', book_name, 'is founded already')


elif not os.path.exists('C:\\Users\\LenovoPc\\Desktop\\CSV Book_Details'):
    
    # print('pass')

    os.makedirs('C:\\Users\\LenovoPc\\Desktop\\CSV Book_Details')
     
f = open(book_path, "a")  
