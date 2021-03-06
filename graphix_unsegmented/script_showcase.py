from draw import *
from util import *
import sys
import hand_examples
from invert import *
from graphix_lang import *
import time

assert USING_SHOWCASE, "not using showcase params plz set in meta_param.py"
params = hand_examples.ex_grid
squares_orig,lines_orig = mk_scene(params)
rendered = render(squares_orig + lines_orig)
constraints = img_2_constraints(rendered)

draw_orig(rendered, "hand_drawings/target.png")

inverter = Inverter()

def run_comparison():

  stime = time.time()
  inverted_params = inverter.invert_full(constraints, rendered, "nn+cegis", 0.9)
  print inverted_params, 'ours'
  nn_cegis_time = time.time() - stime
  squares,lines = mk_scene(inverted_params)
  draw_orig(render(squares+lines), "hand_drawings/result_nn+cegis.png")

  inverter.clear_solver()

  # stime = time.time()
  # inverted_params = inverter.invert_full(constraints, rendered, "nn", 0.1)
  # nn_time = time.time() - stime
  # squares,lines = mk_scene(inverted_params)
  # draw_orig(render(squares+lines), "hand_drawings/result_full_nn.png")

  # inverter.clear_solver()

  # stime = time.time()
  # inverted_params = inverter.invert_full(constraints, rendered, "rand", 0.1)
  # rand_time = time.time() - stime
  # squares,lines = mk_scene(inverted_params)
  # draw_orig(render(squares+lines), "hand_drawings/result_full_rand.png")

  # inverter.clear_solver()

  # stime = time.time()
  # inverted_params = inverter.invert_cegis(constraints, rendered, "r_cegis")
  # print inverted_params, 'r_cegis'
  # r_cegis_time = time.time() - stime
  # squares,lines = mk_scene(inverted_params)
  # draw_orig(render(squares+lines), "hand_drawings/result_r_cegis.png")

  # inverter.clear_solver()

  # stime = time.time()
  # inverted_params = inverter.invert_cegis(constraints, rendered, "cegis")
  # cegis_time = time.time() - stime
  # squares,lines = mk_scene(inverted_params)
  # draw_orig(render(squares+lines), "hand_drawings/result_cegis.png")

  # inverter.clear_solver()

  # stime = time.time()
  # inverted_params = inverter.invert_full(constraints, rendered, "rand+cegis", 0.1)
  # rand_cegis_time = time.time() - stime
  # squares,lines = mk_scene(inverted_params)
  # draw_orig(render(squares+lines), "hand_drawings/result_rand+cegis.png")

  # inverter.clear_solver()

  print "all done times "
  # print "nn ", nn_time
  # print "rand ", rand_time

  # print "rcegis ", r_cegis_time
  # print "cegis ",  cegis_time
  print "nn then cegis ", nn_cegis_time
  # print "rand then cegis ", rand_cegis_time

run_comparison()
