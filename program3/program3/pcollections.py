import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable = False,  defaults = {}):
    def show_listing(s):
        for line_number, line_text in enumerate(s.split('\n'),1):           
            print(f' {line_number: >3} {line_text.rstrip()}')
    if re.compile(r'[qwertyuiopasdfghjklzxcvbnm]\w').search(type_name) == None or type_name in keyword.kwlist:
        raise SyntaxError #MAKE ERROR
    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    if ' ' in field_names or ',' in field_names:
        field_names = field_names.replace(',',' ')
        field_names = field_names.split(' ')
        print(field_names)
        for x in field_names[:]:
            if x == '':
                field_names.remove(x)
    class_template = '''\
class {class_name}:
    _fields = {fields}
    _mutable = {mut}
    def __init__(self, {args}):
        {attr}
    def __repr__(self):
        return '{type_name}(' + {repr_fmt} + ')';
'''
    repr_template = '{name}'
    class_definition = \
      class_template.format(\
        class_name = type_name, 
        fields = field_names, 
        mut = mutable, 
        args = ','.join(field_names), 
        attr = '\n        '.join(f'self.{x} = {x}' for x in field_names))
        repr_fmt= ','.join(name+'='+'{'+repr_template.format(name=name)+'}' for name in field_names),


    # Debug help: uncomment next line, which prints source code for the class
    # show_listing(class_definition)
    
    # Execute the class_definition's str in name_space; next bind its
    #   source_code attribute to this class_definition; following try+except
    #   return the class object created; if there are any syntax errors, show
    #   the class and also show the error
    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )                    
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):                        
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')

    #driver tests
    import driver  
    driver.default_file_name = 'bscp3S22.txt'
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
