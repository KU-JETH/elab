def commaCode(ls):
  if not ls:
    return ""
  
  res = ls[0]
  for i in range(1, len(ls)):
    s = ls[i]
    if i != len(ls) - 1:
      res += ', ' + s
    else:
      res += " and " + s
    
  return res