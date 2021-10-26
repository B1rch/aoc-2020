import time, math, operator
from functools import wraps
from collections import defaultdict

def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start_time
        print(f"{func.__name__} took {time_elapsed} seconds")
        return res
    return wrapper

def print_decorator(func):
  @wraps (func)
  def wrapper(*args, **kwargs):
    print(f"=" * 20 + " " + str.capitalize(func.__name__.replace("_", " ")) + " " + "=" * 20)
    res = func(*args, **kwargs)
    return res
  return wrapper

def dijkstra(graph, start, target):
  Q = set(graph.keys())
  D: dict = {k: [math.inf, None] for k in graph.keys()}
  D[start] = [0, None]
  while Q:
    u = min(Q, key=lambda x: D[x][0])
    Q.remove(u)
    if (u == target):
      S, u = [], target
      if D[u][1] or u == start:
        while u:
          S.append(u)
          u = D[u][1]
        return S[::-1]
    for v in graph[u][1]:
      if v in Q:
        alt = D[u][0] + 1
        if alt < D[v][0]:
          D[v] = [alt, u]
  return D

