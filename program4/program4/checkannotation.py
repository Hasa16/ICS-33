from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation:
    # We start by binding the class attribute to True meaning checking can occur
    #   (but only when the function's self._checking_on is also bound to True)
    checking_on  = True
  
    # For checking the decorated function, bind its self._checking_on as True
    def __init__(self, f):
        self._f = f
        self._checking_on = True

    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)
        def check_sequence(annot_type, type_str):
            assert isinstance(value, annot_type), 'x failed annotation check(wrong type): value = ' + type_as_str(value) + 'was type ' + str(type(value)) + 'should be type ' + type_str
            if len(annot) == 1:
                iteration = 0
                for v in value:
                    self.check(param, annot[0], v, check_history + type_str + '[' + str(iteration) + '] check: ' + str(annot[0]) + '\n')
                    iteration += 1
            else:
                assert len(annot) == len(value), 'annot and value are different lengths'
                for v,k in zip(value, annot):
                    assert isinstance(v, k), 'x failed annotation check(wrong type): value =' +  type_as_str(v) + '... should be ' + str(k)
                    
        def check_dict():
            assert isinstance(value, dict), repr(param) + ' failed annotation check(wrong type): value = ' + type_as_str(value) + 'was type ' + str(type(value)) + 'should be type dict'
            if len(annot) != 1:
                assert len(annot) == 1, 'length of annotations does not equal 1'
            else:
                for annot_k, annot_v in annot.items():
                    for value_k, value_v in value.items():
                            self.check(param, annot_k, value_k, check_history + 'dict key check: ' + str(annot_k) + '\n')
                            self.check(param, annot_v, value_v, check_history + 'dict value check: ' + str(annot_v) + '\n')

        def check_sets(annot_type, type_str):
            assert isinstance(value, annot_type), repr(param) + ' failed annotation check(wrong type): value = ' + repr(value) + '\n was type ' + type_as_str(value) + ' ...should be type ' + type_str + check_history
            assert len(annot) == 1,  repr(param) + ' annotation inconsistency: set should have 1 item but had ' + str(len(annot)) + '\n annotation = ' + str(annot) + '\n' + check_history   
            for a_v in annot:
                for v in value:
                    self.check(param, a_v, v, check_history + 'set key check: '  + str(a_v)+ '\n')
                    
        def check_lambda():
            assert len(inspect.signature(annot).parameters) == 1, '22222'
            try:
                assert annot(value)
            except Exception as message:
                assert False, repr(param) + ' annotation predicate(' + str(annot) + ') raised exception' + '\n exception = ' + str(message.__class__)[8:-2]+ ': ' + str(message) + '\n' + check_history   
            else:
                assert annot(value), repr(param) + ' failed annotation check: value = ' + repr(value) + '\n predicate = ' + str(annot) + '\n' + check_history
        
        def check_str():
            try:
                worked = eval(annot,self._args)
            except Exception as message:
                assert False, repr(param)+' annotation str('+str(annot)+') raised exception'+\
                '\n exception = '+str(message.__class__)[8:-2]+': '+str(message)+'\n'+check_history   
            else:
                assert worked, repr(param)+' failed annotation check(str predicate: '+repr(annot)+')'\
                '\n args for evaluation: '+', '.join([str(k)+'->'+str(v) for k,v in self._args.items()])+'\n'+check_history
            
        # We start by comparing check's function annotation to its arguments
        if annot == None:
            pass
        elif type(annot) is type:
            assert isinstance(value, annot)
        elif isinstance(annot, list):
            check_sequence(list, 'list')
        elif isinstance(annot, tuple):
            check_sequence(tuple, 'tuple')
        elif isinstance(annot, dict):
            check_dict()
        elif isinstance(annot, set):
            check_sets(set, 'set')
        elif isinstance(annot, frozenset):
            check_sets(frozenset, 'frozenset')
        elif inspect.isfunction(annot):
            check_lambda()
        elif isinstance(annot, str):
            check_str()
        else:
            try:
                annot.__check_annotation__(self.check, param, value, check_history)
            except AttributeError:
                raise AssertionError


            
        
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):

        # Returns the parameter->argument bindings as an OrderedDict, derived
        #   from dict, binding the function header's parameters in order

        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        # On first AssertionError, print the source lines of the function and reraise
        if not (Check_Annotation.checking_on and self.checking_on):
            return self._f(*args,**kargs)
        self._args = param_arg_bindings()
        annot = self._f.__annotations__
        try:
        # Check the annotation for every parameter (if there is one)
            for p in self._args.keys():
                if p in annot:
                    self.check(p,annot[p],self._args[p])
          
        # Compute/remember the value of the decorated function
            answer = self._f(*args,**kargs)
          
        # If the return has an annotation, check it
            if 'return' in annot:
                self._args['_return'] = answer
                self.check('return',annot['return'],answer)

            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            #print(80*'-')
            #for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
            #    print(l.rstrip())
            #print(80*'-')
            raise




  
if __name__ == '__main__':     
    # an example of testing a simple annotation  

           
    #driver tests
    import driver
    driver.default_file_name = 'bscp4S22.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
