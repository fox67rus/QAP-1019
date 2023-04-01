import functools

def do_twice(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
      func(*args, **kwargs)
      return func(*args, **kwargs)
  return wrapper




@do_twice
def t_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

print(t_twice.__name__)
print(do_twice.__name__)