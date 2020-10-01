def divide(a,b):

    try:
        c = a/b 
    except ZeroDivisionError:
        print('enter a positive integer')
    except TypeError:
        print('enter valid type')
    else:
        print(f"division value is --> {c}")
    finally:
        print('done one more attempt??')

divide(1,"m")