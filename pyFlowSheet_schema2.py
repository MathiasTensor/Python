from pyflowsheet import Flowsheet, BlackBox, Stream, StreamFlag, Port, SvgContext,VerticalLabelAlignment, HorizontalLabelAlignment
from pyflowsheet import HeatExchanger, Distillation, Mixer, Splitter, Vessel, Pump
import matplotlib
from pyflowsheet.internals import Tubes, RandomPacking
from IPython.core.display import SVG, HTML
import matplotlib.pyplot as plt

path = "C:/Users/Asus/Desktop/Folders/PyGame tutorial/Scheme2.svg"

# Display
pfd = Flowsheet(id="FlowSheet", name="FlowSheet diagram", description="Multicomponent diagram")
step_x = 150
step_y = 75
size_small = (100, 100)
size_large = (100, 100)
size_flag = (100, 100)

# Elements
Mulj = BlackBox(id="Mulj", name="box1", position=(150,  1000 - 8*step_y),
                size=size_large)
Susenje = BlackBox(id="Sušenje", name="box2", position=(150 + 2*step_x, 1000 - 8*step_y),
                size=size_large)
Posusen_mulj = BlackBox(id="Posušen_mulj", name="box3", position=(150 + 4*step_x, 1000 - 8*step_y),
                size=size_large)
Pec = BlackBox(id="Peč", name="box4", position=(150 + 2*step_x, 1000 - 5*step_y),
                size=size_large)

FLAG1 = StreamFlag(id=f"Nasičen_zrak", name="flag1", position=(150 + 2*step_x, 1000 - 11*step_y), size=(size_flag[0],
                                                                                                        170))
FLAG1.rotate(-90)

FLAG2 = StreamFlag(id=f"Zrak", name="flag2", position=(150 + 2*step_x, 1000 - 3*step_y), size=size_flag)
FLAG2.rotate(-90)

FLAG3 = StreamFlag(id=f"CH\u2084", name="flag3", position=(150 + step_x, 1000 - 5*step_y),
                   size=size_flag)

FLAG4 = StreamFlag(id=f"Dimni_plini_+_CO\u2082", name="flag4", position=(150 + 3*step_x, 1000 - 5*step_y),
                   size=(175, size_flag[1]))

# Add all Elements to draw
list_all_units = [Susenje, Pec, Mulj, Posusen_mulj, FLAG1, FLAG3, FLAG2, FLAG4]
pfd.addUnits(list_all_units)

# Modifications for BlackBox names
for x in list_all_units:
    x.setTextAnchor(HorizontalLabelAlignment.Center, VerticalLabelAlignment.Center, offset=(0, 3))
    x.fontSize = 15

FLAG1.setTextAnchor(vertical=VerticalLabelAlignment.Top, horizontal=HorizontalLabelAlignment.Center, offset=(0, 75))
FLAG2.setTextAnchor(vertical=VerticalLabelAlignment.Top, horizontal=HorizontalLabelAlignment.Center, offset=(0, 30))

# Adding additional ports to BlackBox-es
Susenje.ports["OutBottom"] = Port("OutTop", Susenje, (0.5, 1), (0, 1), intent="out")
Susenje.ports["OutTop"] = Port("OutTop", Susenje, (0.5, 0), (0, 1), intent="out")
Pec.ports["OutTop"] = Port("In", Pec, (0.5, 0), (0, 1), intent="out")
Pec.ports["InBottom"] = Port("OutTop", Pec, (0.5, 1), (0, 1), intent="in")

# All connectors
pfd.connect(name="/1", fromPort=Mulj["Out"], toPort=Susenje["In"])
pfd.connect(name="Nasicen_zrak", fromPort=Susenje["OutTop"], toPort=FLAG1["In"])
pfd.connect(name="Vroc_suh_zrak", fromPort=Pec["OutTop"], toPort=Susenje["OutBottom"])
pfd.connect(name="/2", fromPort=Susenje["Out"], toPort=Posusen_mulj["In"])
pfd.connect(name=f"/3", fromPort=FLAG3["Out"], toPort=Pec["In"])
pfd.connect(name=f"/5", fromPort=FLAG2["Out"], toPort=Pec["InBottom"])
pfd.connect(name=f"/4", fromPort=Pec["Out"], toPort=FLAG4["In"])

# Configure connectors
pfd.streams["Vroc_suh_zrak"].labelOffset = (step_x / 3.5, -step_y)

# Adding text without BlackBox-es (10 in position x subtracted because text should not start in the middle
pfd.callout(text=f"ZRAK Ψ = 40%", position=(150 + 2*step_x + 9, 1000 - 3*step_y + 47))
pfd.callout(text=f"ZRAK Ψ = 85%", position=(150 + 2*step_x + 9, 1000 - 11*step_y + 90))
pfd.callout(text=f"\u03B2 = 0.85 kWh/kgH\u2082O", position=(150 + 1.15*step_x, 1000 - 7*step_y))
pfd.callout(text=f"\u03BB = 1.1", position=(150 + 2*step_x + 27, 1000 - 3*step_y + 60))
pfd.callout(text=f"25% ss, 75% H\u2082O", position=(150,  1000 - 8*step_y + 70))
pfd.callout(text=f"85% ss, 15% H\u2082O", position=(150 + 4*step_x, 1000 - 8*step_y + 70))

ctx = SvgContext(path)
img = pfd.draw(ctx)
SVG(img.render(width=800, height=2000))


