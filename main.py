from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("x and y must be either int or float")
    
    return x + y

if __name__ == "__main__":
    print(add(1, 2))
    print(add(1.5, 2.5))
    print(add(1, 2.5))
    print(add(1.5, 2))

    