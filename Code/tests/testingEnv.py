import importlib
from importlib import machinery
x  = 'C:\\Projects\\Thesis\\Code\\src\\codeLib.py'
module = importlib.import_module('libP.py'[:-3])
method = getattr(module, "pesel")

loader = machinery.SourceFileLoader('codeLib', x)
print(method)
print(method('95082707756'))


#module2 = importlib.find_loader(None, path=x)
#module2 = importlib.util.find_spec(x)
module2 = loader.load_module()
method2 = getattr(module2, "idnum")
#print(method2('95082707756'))
print(method2('CEM 798370'))