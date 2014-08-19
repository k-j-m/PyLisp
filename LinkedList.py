
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
        
