from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# class ProductFilter:
#     def filter_by_color(self, products, color):
#         for p in products:
#             if p.color == color: yield p

#     def filter_by_size(self, products, size):
#         for p in products:
#             if p.size == size: yield p

#     def filter_by_size_and_color(self, products, size, color):
#         for p in products:
#             if p.color == color and p.size == size: yield p

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class ProductFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


if __name__ == '__main__':
    shirt = Product("Heavy Cotton Tee T-Shirt", Color.GREEN, Size.MEDIUM)
    apple = Product("Pink Pearl Apple", Color.RED, Size.SMALL)
    car = Product("Tesla Model 3", Color.RED, Size.LARGE)

    products = [shirt, apple, car]

    product_filter = ProductFilter()
    print('Green items:')

    color_filter = ColorSpecification(Color.GREEN)
    for p in product_filter.filter(products, color_filter):
        print(f' - {p.name} is green')

    size_filter = SizeSpecification(Size.LARGE)

    print('Large red items:')
    # large_red_filter = AndSpecification(large_filter, 
    #     ColorSpecification(Color.RED))

    combinator = size_filter & ColorSpecification(Color.RED)
    for p in product_filter.filter(products, combinator):
        print(f' - {p.name} is large and red')
