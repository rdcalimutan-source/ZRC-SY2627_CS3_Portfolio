def check_positive_whole_number(value, label):
    if isinstance(value, bool) or not isinstance(value, int):
        return f"{label} must be a whole number."
    if value <= 0:
        return f"{label} must be positive."
    return None


class Publication:
    def __init__(self, title, author):
        self.__title = None
        self.__author = None
        self.set_title(title)
        self.set_author(author)

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")


class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = None
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages):
        error = check_positive_whole_number(number_pages, "Number of pages")
        if error is None:
            self.__number_of_pages = number_pages
        else:
            print(error)

    def display_info(self):
        super().display_info()
        pages = self.get_number_of_pages()
        print(f"Number of pages: {pages if pages is not None else 'Not set'}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        error = check_positive_whole_number(issue_number, "Issue number")
        if error is None:
            self.__issue_number = issue_number
        else:
            print(error)

    def display_info(self):
        super().display_info()
        issue = self.get_issue_number()
        print(f"Issue number: {issue if issue is not None else 'Not set'}")


def main():
    pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
    pub2 = Publication("Philippine Journal of Science", "Various Authors")
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    book2 = Book("Noli Me Tangere", "Jose Rizal", 400)
    mag1 = Magazine("National Geographic", "Various Authors", 202)
    mag2 = Magazine("Time", "Various Authors", 45)

    print("Publication Information:")
    pub1.display_info()
    print()
    pub2.display_info()

    print("\nBook Information:")
    book1.set_number_of_pages(-310)
    book1.display_info()
    print("get_number_of_pages() returns:", book1.get_number_of_pages())
    print()
    book2.display_info()

    print("\nMagazine Information:")
    mag1.display_info()
    print("get_issue_number() returns:", mag1.get_issue_number())
    print()
    mag2.display_info()

    print("\nExtra validation tests:")
    bad_book = Book("Untitled Draft", "Unknown Author", 0)
    bad_book.display_info()
    print()
    book2.set_number_of_pages(412)
    print("Pages after a valid change:", book2.get_number_of_pages())
    mag2.set_issue_number(-5)
    mag2.set_issue_number("seven")
    print("Issue number after bad input:", mag2.get_issue_number())


if __name__ == "__main__":
    main()