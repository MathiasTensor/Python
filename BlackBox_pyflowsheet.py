from pyflowsheet import Flowsheet, BlackBox, Stream, StreamFlag, Port, SvgContext,VerticalLabelAlignment, HorizontalLabelAlignment
from pyflowsheet import HeatExchanger, Distillation, Mixer, Splitter, Vessel
import matplotlib
from pyflowsheet.internals import Tubes, RandomPacking
from IPython.core.display import SVG, HTML
import matplotlib.pyplot as plt

path = "C:/Users/Asus/Desktop/PyGame tutorial/externalized_column_with_preheater.svg"

# Display
pfd = Flowsheet(id="FlowSheet", name="Simple flowSheet diagram", description="BlackBox diagram")
step_x = 200
step_y = 150
size_small = (100, 50)
size_large = (150, 50)
size_flag = (50, 50)

# Elements
BOX1 = BlackBox(id="MULJ", name="box1", position=(150, 150), size=size_small)
BOX2 = BlackBox(id="KOMPOSTIRANJE", name="box2", position=(150 + size_small[0] + step_x, 150), size=size_large)
BOX3 = BlackBox(id="KOMPOST", name="box3", position=(150 + size_small[0] + step_x + size_large[0] + step_x, 150),
                size=size_large)
BOX4 = BlackBox(id="STAR_KOMPOST", name="box4", position=(150 + size_small[0] + step_x, 150 + step_y),
                size=size_large)
BOX5 = BlackBox(id="PRODUKT", name="box5", position=(150 + size_small[0] + step_x + size_large[0] + step_x + step_x +
                                                     size_large[0], 150), size=size_large)
FLAG1 = StreamFlag(id=f"CO\u2082", name="flag1", position=(150 + size_small[0] + step_x + size_large[0] / 2 - 10 -
                                                           size_flag[0] / 2.5, 150 - step_y), size=size_flag)
FLAG1.rotate(-90)
FLAG1.fontSize = 11


# Add all Elements to draw
list_units = [BOX1, BOX2, BOX3, BOX4, BOX5, FLAG1]
pfd.addUnits(list_units)

#Modifications for BlackBox names
for x in list_units:
    x.setTextAnchor(HorizontalLabelAlignment.Center, VerticalLabelAlignment.Center, offset=(0, 3))

# Adding additional ports to BlackBox-es
BOX2.ports["OutBottom"] = Port("OutTop", BOX2, (0.5, 1), (0, 1), "out")
BOX2.ports["OutTop"] = Port("OutTop", BOX2, (0.5, 0), (0, 1), "out")
BOX3.ports["OutBottom"] = Port("OutTop", BOX3, (0.5, 1), (0, 1), "out")
BOX4.ports["OutTop"] = Port("OutTop", BOX4, (0.5, 0), (0, 1), "out")

# All connectors
pfd.connect(name="1_50_odstotkov", fromPort=BOX1["Out"], toPort=BOX2["In"])
pfd.connect(name="/1", fromPort=BOX2["Out"], toPort=BOX3["In"])
pfd.connect(name="2_50_odstotkov", fromPort=BOX3["OutBottom"], toPort=BOX4["Out"])
pfd.connect(name="/2", fromPort=BOX4["OutTop"], toPort=BOX2["OutBottom"])
pfd.connect(name="3_50_odstotkov", fromPort=BOX3["Out"], toPort=BOX5["In"])
pfd.connect(name="10_odstoten_del_ogljika", fromPort=BOX2["OutTop"], toPort=FLAG1["In"])


# Configure connectors
pfd.streams["1_50_odstotkov"].labelOffset = (step_x / 2, -5)
pfd.streams["/1"].labelOffset = (step_x / 2, -5)
pfd.streams["2_50_odstotkov"].labelOffset = (- step_x / 2 - size_small[0], step_y / 1.5)
pfd.streams["/2"].labelOffset = (size_large[0] / 10, - step_y / 3)
pfd.streams["3_50_odstotkov"].labelOffset = (step_x / 2, -5)
pfd.streams["10_odstoten_del_ogljika"].labelOffset = (size_small[0] / 2 + size_flag[0] / 3, - step_y / 3)

# Adding text without BlackBox-es (10 in position x subtracted because text should not start in the middle
#pfd.callout(text=f"CO\u2082", position=(150 + size_small[0] + step_x + size_large[0] / 2 - 10, 150 - step_y / 2))

ctx = SvgContext(path)
img = pfd.draw(ctx)
SVG(img.render(width=1280, height=640))


