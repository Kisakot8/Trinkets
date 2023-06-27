# Way to run functions in beta-testing where there may be bugs to be caught, but you don't want crashes

def training_wheels(func, *params):
    '''
    Runs a function in a try-except statement to make sure it doesn't crash but can run properly (i.e. without debug print statements) if it's used in beta-testing.
    '''
    try:
        return func(*params)
    
    except Exception as ex:
        print(f'Exception occured in \'{func.__name__}\':', type(ex).__name__, ex)
