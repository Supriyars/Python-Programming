def disp(a,b):
    try:
        print('Task started')
        print(a/b) # Zero Division Error
    except:
        print('Some error handled') 
    else:
        print('Task executed without any exception')
    finally:
        print('Task ended.')

disp(10,0)
disp(10,5) 
disp(20,5)


#try: Used to keep the logic in which we may get some error.

#except: Will be executed when execption occurres in try block logic

#else: will be executed when try block logic executed without any error.

#finally:will always executed irrespective of execption occurred or not.