# -*- coding: utf-8 -*-
import ctypes, sys

def _invoke(_obj , _metodo , _parms):
  try:
    _cobj=ctypes.CDLL(_obj)
    _func=eval('_cobj.%s' % _metodo)
    return _func('%s' % ''.join(str(_k) for _k in _parms))
  except:
    raise

if __name__=='__main__':
  if len(sys.argv) < 3:
    print 'invoke.py - exec a function from a shared object'
    print 'syntax: python invoke.py ./lib.so function [param1, param2, ...]'
    exit(-1)
  else:
    _tmp = _invoke(sys.argv[1], sys.argv[2], sys.argv[3:])
    print '\nfunction "%s" from "%s" returned "%s"' % (sys.argv[2],sys.argv[1],str(_tmp))
    exit(0)
