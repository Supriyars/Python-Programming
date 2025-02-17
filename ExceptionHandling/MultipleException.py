def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('ZeroDivisionError Occured and Handled')
    except NameError:
        print('Name error occured and Handled')
    except TypeError:
        print('Type Error Occured and Handled')
    except:
        print('Some Error Occured')
disp(10,20)