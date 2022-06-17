import os

def csv_book_details(book_name, book_authors, book_review, publication_date, book_path, image_path, csv_path):
    if not os.path.exists(csv_path):
        with open(csv_path, 'w') as csv_file:
            csv_file.write("BookName|BookAuthor(s)|BookReview|PublicatoinDate|BookPATH|ImagePATH\n")
    else:
        with open(csv_path, 'r') as csv_file:
            header= csv_file.readline()
        if header != "BookName|BookAuthor(s)|BookReview|PublicatoinDate|BookPATH|ImagePATH\n":
            return csv_book_details(book_name, book_authors, book_review, publication_date, book_path, image_path, csv_path)

    with open(csv_path, 'a') as csv_file:
        csv_file.write('|'.join([book_name, book_authors, book_review, publication_date, book_path, image_path]) + "\n")


if __name__ == "__main__":
    pass