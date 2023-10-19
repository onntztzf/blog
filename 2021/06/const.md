# 修饰符 const

通过使用 `const` 修饰，可以限定一个变量不允许被改变（只读），产生静态作用。

```text
int *ptr; // *ptr is an int value
int const *ptrToConst; // *ptrToConst is a constant (int: integer value)
int * const constPtr; // constPtr is a constant (int *: integer pointer)
int const * const constPtrToConst; // constPtrToConst is a constant (pointer)
                                   // as is *constPtrToConst (value)
void Foo( int * ptr,
          int const * ptrToConst,
          int * const constPtr,
          int const * const constPtrToConst )
{
    *ptr = 0; // OK: modifies the "pointee" data
    ptr  = NULL; // OK: modifies the pointer

    *ptrToConst = 0; // Error! Cannot modify the "pointee" data
    ptrToConst  = NULL; // OK: modifies the pointer

    *constPtr = 0; // OK: modifies the "pointee" data
    constPtr  = NULL; // Error! Cannot modify the pointer

    *constPtrToConst = 0; // Error! Cannot modify the "pointee" data
    constPtrToConst  = NULL; // Error! Cannot modify the pointer
}
```
