#Encapsulation
#Activity 2: Rectangle using @property

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print("Warning: Width must be greater than zero. Value ignored.")

    @property
    def height(self):
        """Get the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            print("Warning: Height must be greater than zero. Value ignored.")

    @property
    def area(self):
        """Calculate and return the rectangle's area."""
        return self.__width * self.__height


if __name__ == "__main__":
    rectangle = Rectangle(10, 5)

    print("Rectangle width:", rectangle.width)
    print("Rectangle height:", rectangle.height)
    print("Rectangle area:", rectangle.area)

    rectangle.width = 12
    rectangle.height = 6
    print("\nAfter updating dimensions:")
    print("Rectangle width:", rectangle.width)
    print("Rectangle height:", rectangle.height)
    print("Rectangle area:", rectangle.area)

    rectangle.width = -3  
    print("Width after invalid update:", rectangle.width)
