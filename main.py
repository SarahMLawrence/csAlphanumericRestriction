def csAlphanumericRestriction(input_str):
  if input_str.isalpha() or input_str.isnumeric():
    return True
  else:
    return False