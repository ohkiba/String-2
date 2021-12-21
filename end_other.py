def end_other(a, b):
    if len(a)>len(b):
        if a[len(a)-len(b):len(a)].lower()==b.lower():
            return True
    elif len(a)<len(b):
        if b[len(b)-len(a):len(b)].lower()==a.lower():
            return True
    elif len(a)==len(b):
        if a.lower()==b.lower():
            return True
    return False

#Alternative Solution
"""
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))
  """