from mathstropy import merge_dictionaries
from mathstropy.image_processing import get_color_count, get_edge_count, resize_max


def data_prep(image):
  return resize_max(image, 180)


def feature_extraction(image):
  color_count = get_color_count(image)

  # TODO: select color features with percentage values (implement function)
  color_pct = get_color_pct(color_count)

  edge_count = get_edge_count(image)

  # TODO: select edge features with percentage values (implement function)
  edge_pct = get_edge_pct(edge_count)

  merged_dict = merge_dictionaries(color_pct, edge_pct)

  return merged_dict


# TODO: implement fuction that calculates the percentage of each color
def get_color_pct(color_cnt):
  """
    This function calculates the percentage of each color

    Parameters:
    - color_cnt(dict): dictionary with the number of pixels for red, green, blue, white, black.
 
    Return:
    - dict: dictionary of percentages for selected color features
    """

  # TODO: calculate total number of pixels
  color_pct = {}
  pixels = 0
  for color in color_cnt:
    if color == "white" or color == "black":
      continue
    pixels += color_cnt[color]

  # TODO: calculate percentages of selected color features
  for color in color_cnt:
    color_pct[color] = color_cnt[color] / pixels

  return color_pct


# TODO: implement fuction that calculates the percentage of each color
def get_edge_pct(edge_cnt):
  """
    This function calculates the percentage of each color based on all edges.

    Parameters:
    - edge_cnt(dict): dictionary with the number of horizontal, fwd-diag, vertical, bkwd-diag edges
      
    Return:
    - dict: dictionary of percentages for selected edge features
    """

  # TODO: calculate total number of edges

  edge_pct = {}
  total_edges = 0
  for edge in edge_cnt:
    if edge == "horizontal" or edge == "vertical":
      continue
    total_edges += edge_cnt[edge]

  # TODO: calculate percentage of edges
  for edge in edge_cnt:
    edge_pct[edge] = edge_cnt[edge] / total_edges

  return edge_pct
