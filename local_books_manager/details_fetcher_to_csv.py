import os

def csv_book_details(book_name, book_author, book_path, book_review, image_path, csv_path):#this is what I mean by argument, and passing stuff through it
    if not os.path.exists(csv_path):
        with open(csv_path, 'w') as csv_file:
            csv_file.write("BookName, BookAuthor(s), BookPATH, BookReview, ImagePATH\n")
    else:
        with open(csv_path, 'r') as csv_file:
            header= csv_file.readline()
        if header != "BookName, BookAuthor(s), BookPATH, BookReview\n":
            return csv_book_details(book_name, book_author, book_path, book_review, image_path, csv_path)

    with open(csv_path, 'a') as csv_file:
        csv_file.write(','.join([book_name, book_author, book_path, book_review, image_path]))


if __name__ == "__main__":
    csv_book_details('BOOK NAME', 'BOOK AUTHOR', 'PATH', 'CSV_PATH') # here is a test case, we'll replace these arbitrary values with something useful later on, but the main usage is for anther script, that will pass these details.