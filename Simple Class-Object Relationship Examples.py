
# Example 1: Books and a Library
# =============================
#
# This example shows how a class (Book) serves as a template,
# and objects are individual instances of that template

class Book:
    """A class representing a book in a library"""
    
    def __init__(self, title, author, pages):
        # Each book will have these attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.is_open = False  # All books start closed
    
    def open_book(self):
        """Open the book to read it"""
        self.is_open = True
        return f"{self.title} is now open and ready to read!"
    
    def close_book(self):
        """Close the book when done"""
        self.is_open = False
        return f"{self.title} is now closed."
    
    def describe(self):
        """Get a description of the book"""
        return f"{self.title} by {self.author}, {self.pages} pages."


# EXPLANATION: Creating Objects from a Class
# -----------------------------------------
# Think of the Book class above as a "cookie cutter" or a "blueprint"
# It defines what ALL books have in common:
#   - They all have a title, author, and number of pages (attributes)
#   - They all can be opened and closed (methods)
#   - They all can be described (method)

# Now we create individual "book objects" using that blueprint:
print("=== CREATING BOOK OBJECTS ===")

# Create the first book object
harry_potter = Book("Harry Potter", "J.K. Rowling", 320)
print(f"Object 1: {harry_potter.describe()}")

# Create a second book object
hunger_games = Book("The Hunger Games", "Suzanne Collins", 374)
print(f"Object 2: {hunger_games.describe()}")

# Create a third book object
hobbit = Book("The Hobbit", "J.R.R. Tolkien", 295)
print(f"Object 3: {hobbit.describe()}")

# DEMONSTRATION: Each object is independent
print("\n=== INTERACTING WITH BOOK OBJECTS ===")

# Open the first book
print(harry_potter.open_book())

# Check the status of each book:
print(f"Is Harry Potter open? {harry_potter.is_open}")   # True
print(f"Is Hunger Games open? {hunger_games.is_open}")   # False
print(f"Is The Hobbit open? {hobbit.is_open}")           # False

# Open another book
print(hobbit.open_book())

# Close the first book
print(harry_potter.close_book())

# Final status check:
print(f"Is Harry Potter open? {harry_potter.is_open}")   # False
print(f"Is Hunger Games open? {hunger_games.is_open}")   # False
print(f"Is The Hobbit open? {hobbit.is_open}")           # True


# Example 2: Students in a Classroom
# =================================
#
# This example shows how multiple objects (students)
# can be created from a single class definition

class Student:
    """A class representing a student in a school"""
    
    def __init__(self, name, grade):
        # Each student will have these attributes
        self.name = name
        self.grade = grade
        self.points = 0  # All students start with 0 points
    
    def study(self, hours):
        """Study for some hours to earn points"""
        points_earned = hours * 5  # 5 points per hour
        self.points += points_earned
        return f"{self.name} studied for {hours} hours and earned {points_earned} points!"
    
    def take_test(self):
        """Take a test using accumulated points"""
        if self.points >= 10:
            self.points -= 10  # Use 10 points
            return f"{self.name} took a test and did well!"
        else:
            return f"{self.name} needs more study points before taking a test."
    
    def get_status(self):
        """Get the student's current status"""
        return f"{self.name} is in grade {self.grade} with {self.points} points."


# EXPLANATION: Creating Multiple Objects from the Student Class
# -----------------------------------------------------------
# The Student class defines what ALL students have in common:
#   - They all have a name and grade (attributes)
#   - They all can study to earn points (method)
#   - They all can take tests using points (method)
#   - They all have a status that can be checked (method)

# Now we create individual "student objects" using that blueprint:
print("\n\n=== CREATING STUDENT OBJECTS ===")

# Create three student objects
emma = Student("Emma", 10)
print(f"Student 1: {emma.get_status()}")

jack = Student("Jack", 11)
print(f"Student 2: {jack.get_status()}")

sophia = Student("Sophia", 10)
print(f"Student 3: {sophia.get_status()}")

# DEMONSTRATION: Each student object is independent
print("\n=== STUDENT ACTIVITIES ===")

# Emma studies for 3 hours
print(emma.study(3))

# Jack studies for 1 hour
print(jack.study(1))

# Sophia studies for 5 hours
print(sophia.study(5))

# Let's check the status of each student after studying
print("\n=== STUDENT STATUS AFTER STUDYING ===")
print(emma.get_status())    # Emma has 15 points
print(jack.get_status())    # Jack has 5 points
print(sophia.get_status())  # Sophia has 25 points

# Taking tests
print("\n=== STUDENTS TAKING TESTS ===")
print(emma.take_test())     # Emma can take the test
print(jack.take_test())     # Jack needs more points
print(sophia.take_test())   # Sophia can take the test

# Final status check
print("\n=== FINAL STUDENT STATUS ===")
print(emma.get_status())    # Emma now has 5 points left
print(jack.get_status())    # Jack still has 5 points
print(sophia.get_status())  # Sophia now has 15 points left
