def convert_lambda_to_def(g):
  f = g.split()

  return f"def {f[0]}({f[3][:-1]}):\n    return {g[g.index(':') + 2:]}"
