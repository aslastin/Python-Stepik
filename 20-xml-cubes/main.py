from xml.etree import ElementTree


def cube_dfs(cube, cost, cost_by_color):
    cost_by_color[cube.attrib["color"]] += cost
    for sub_cube in cube:
        cube_dfs(sub_cube, cost + 1, cost_by_color)


xml_cubes = input()
main_cube = ElementTree.fromstring(xml_cubes)
cost_by_color = {"red": 0, "green": 0, "blue": 0}

cube_dfs(main_cube, 1, cost_by_color)

print(cost_by_color["red"], cost_by_color["green"], cost_by_color["blue"])
