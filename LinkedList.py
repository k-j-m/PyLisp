
class cons(object):
    def __init__(self,car,cdr):
        self.car = car
        self.cdr = cdr

    def __str__(self):
        return '(%s)' % self._str_no_parens()
        
    def _str_no_parens(self):
        return str(self.car) + _cdr_to_str(self.cdr)

def car(lst):
    return lst.car

def cdr(lst):
    return lst.cdr

def _cdr_to_str(mycdr):
    if mycdr == None:
        return ''
    elif isinstance(mycdr,cons):
        return ' ' + mycdr._str_no_parens()
    else:
        return ' . ' + str(mycdr)
        
def reverse_recur(lst):
    return reverse_aux(None,lst)

def reverse_aux(preceding,lst):
    if lst is None:
        return preceding
    else:
        return reverse_aux(cons(car(lst),preceding),cdr(lst))

def reverse(lst):
    newlst = None
    while True:
        if lst is None:
            return newlst
        else:
            newlst = cons(car(lst),newlst)
            lst = cdr(lst)

def nreverse(lst):
    newlst = None
    
    while True:
        if lst is None:
            return newlst
        else:
            #newlst = cons(car(lst),newlst)
            tmp = newlst
            newlst = lst
            lst = cdr(lst)
            newlst.cdr = tmp
            
def linkedlist(pylist):
    c = None
    for el in pylist[::-1]:
        c = cons(el,c)
    return c
