#%%
from logging import Logger
from typing import TypeVar, Generic
from typing import NewType, ClassVar, TypeVar, Generic
from collections.abc import Iterable, Sequence

matrix_item = int | float
matrix_row = Sequence[matrix_item]
matrix = Sequence[matrix_row]


MatrixObj = TypeVar('MatrixObj')
class Matrix():
    def __init__(self, row: int, column: int, values: int | list[int | float] | matrix) -> MatrixObj:
        
        if row <= 0 or column <= 0:
            raise ValueError('row and column must be greater than 0')
        
        if not values:
            raise ValueError(f'values must contain {row * column} matrix_items in it')
        
        self.rows = row
        self.columns = column
        
        match values:
            
            case int(val) | float(val):
                self.values = [[val] * column] * row
                
            case vals if all(isinstance(val, int | float) for val in vals):
                if len(vals) != row * column:
                    raise ValueError(f'values must contain {row * column} matrix_items in it')
                self.values = [[vals[i * column + j] for j in range(column)] for i in range(row)]
                
            case list(vals) if all(isinstance(val, Iterable) for val in vals) and all(isinstance(v, int | float) for val in vals for v in val):
                if any(len(val) != column for val in vals) or len(vals) != row:
                    raise ValueError(f'values must contain {row * column} matrix_items in it')
                self.values = vals
                
            case _:
                raise ValueError('Invalid values')
    
    def flattened(self) -> list[int | float]:
        return [v for row in self.values for v in row]
    
    def __add__(self, other: int | MatrixObj) -> MatrixObj:
        if isinstance(other, int | float):
            return Matrix(self.rows, self.columns, [val + other for val in self.flattened()])
        elif isinstance(other, Matrix):
            if len(self.flattened()) != len(other.flattened()):
                raise ValueError('Matrix dimensions must match')
            return Matrix(self.rows, self.columns, [sum(pair) for pair in zip(self.flattened(), other.flattened())])
        else:
            raise ValueError('Invalid other')
    
    __radd__ = __add__
    
    def transpose(self) -> MatrixObj:
        return Matrix(self.columns, self.rows, [row for row in zip(*self.values)])
    
    def __repr__(self) -> str:
        return str(Matrix(self.rows, self.columns, list(map(lambda x: round(x, 2), self.flattened()))).values)
    
    
