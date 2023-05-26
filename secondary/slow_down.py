import time

def standardizer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        ret = func(*args,**kwargs)
        end_time = time.time() - start_time
        if end_time < 0.1:
            time.sleep( 0.1 - end_time)
        return ret
    return wrapper


def not_decorated(param) :
    return sum(range(param))

start_time = time.time()
not_decorated(1_000_000) #Temps d'exécution : ~0.04s
print("1 :", time.time()-start_time)

start_time = time.time()
not_decorated(10_000_000) #Temps d'exécution : ~0.4s
print("2 :", time.time()-start_time)

@standardizer
def decorated(param) :
    return sum(range(param))

start_time = time.time()
decorated(1_000_000) #Temps d'exécution : ~0.1s
print("3 :", time.time()-start_time)

start_time = time.time()
decorated(10_000_000) #Temps d'exécution : ~0.4s
print("4 :", time.time()-start_time)


@standardizer
def concatenate(**words) :
    return [arg for arg in words.values() ]

start_time = time.time()
print( "Here","is","the","sentence" ) # Execution time : ~0.1s
print("5 :", time.time()-start_time)

start_time = time.time()
print( *concatenate(a="that", b="can", c="take", d="time!") ) # Execution time : ~0.1s
print("6 :", time.time()-start_time)
