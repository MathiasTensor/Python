from pyflowsheet import Flowsheet, BlackBox, Stream, StreamFlag, Port, SvgContext,VerticalLabelAlignment, HorizontalLabelAlignment
from pyflowsheet import HeatExchanger, Distillation, Mixer, Splitter, Vessel, Pump
import matplotlib
from pyflowsheet.internals import Tubes, RandomPacking
from IPython.core.display import SVG, HTML
import matplotlib.pyplot as plt

path = "C:/Users/Asus/Desktop/Folders/PyGame tutorial/Scheme3.svg"

# Display
pfd = Flowsheet(id="FlowSheet", name="FlowSheet diagram", description="Multicomponent diagram")
step_x = 200
step_y = 75
size_small = (100, 100)
size_large = (100, 100)
size_flag = (100, 100)

# Elements
Menjalnik = HeatExchanger(id="Toplotni_menjalnik", name="menjalnik1", position=(150 + 2*step_x, 1500 - 2*step_y),
                          size=size_small)
Pumpa = Pump(id="Toplotna_črpalka", name="pumpa", position=(150 + step_x, 1500), size=size_large)
Mulj = BlackBox(id="Mulj", name="box1", position=(150 + step_x,  1500 - 4*step_y),
                size=size_large)
Susenje = BlackBox(id="Sušenje", name="box2", position=(150 + 2*step_x, 1500 - 4*step_y),
                size=size_large)
Kondenzator = Vessel(id="kondenzator", name="kondenzator", position=(150 + 2*step_x, 1500 - 9*step_y), size=(100, 300))

FLAG1 = StreamFlag(id=f"Eletkrika", name="flag1", position=(150, 1500), size=size_flag)
FLAG1.fontSize = 11

FLAG2 = StreamFlag(id=f"Purge", name="flag2", position=(150 + 2*step_x, 1500 - 11*step_y), size=size_flag)
FLAG2.fontSize = 11
FLAG2.rotate(-90)

FLAG3 = StreamFlag(id=f"H\u20820", name="flag3", position=(150 + 3*step_x, 1500 - 7*step_y + size_flag[1] / 3),
                   size=size_flag)
FLAG3.fontSize = 11

# Add all Elements to draw
list_units = [Menjalnik, Pumpa, Mulj, Susenje, Kondenzator, FLAG1, FLAG2, FLAG3]
pfd.addUnits(list_units)

# Modifications for BlackBox names
for x in list_units:
    x.setTextAnchor(HorizontalLabelAlignment.Center, VerticalLabelAlignment.Center, offset=(0, 3))
    x.fontSize = 15

# Adding additional ports to BlackBox-es
Pumpa.ports["OutBottom"] = Port("OutTop", Pumpa, (0.5, 1), (0, 1), intent="out")
Pumpa.ports["OutTop"] = Port("OutTop", Pumpa, (0.5, 0), (0, 1), intent="out")
Menjalnik.ports["In"] = Port("In", Menjalnik, (0, 0.5), (0, 1), intent="in")
Menjalnik.ports["OutBottom"] = Port("OutTop", Menjalnik, (0.5, 1), (0, 1), intent="out")
Menjalnik.ports["OutTop"] = Port("OutTop", Menjalnik, (0.5, 0), (0, 1), intent="out")
Menjalnik.ports["OutLeft"] = Port("OutLeft", Menjalnik, (1, 0.5), (0, 1), intent="out")
# Condensator has 2 "Out" ports
Kondenzator.ports["OutBottom"] = Port("OutBottom", Kondenzator, (0.5, 1), (0, 1), intent="out")
Kondenzator.ports["OutTop"] = Port("OutTop", Kondenzator, (0.5, 0), (0, 1), intent="out")
Kondenzator.ports["Out1"] = Port("OutTop", Kondenzator, (1, 0.25), (0, 1), intent="out")
Kondenzator.ports["Out2"] = Port("OutTop", Kondenzator, (1, 0.75), (0, 1), intent="out")
Kondenzator.ports["InLeft"] = Port("InLeft", Kondenzator, (0, 0.5), (0, 1), intent="in")
Susenje.ports["OutBottom"] = Port("OutTop", Susenje, (0.5, 1), (0, 1), intent="out")
Susenje.ports["OutTop"] = Port("OutTop", Susenje, (0.5, 0), (0, 1), intent="out")
FLAG2.ports["OutLeft"] = Port("OutLeft", FLAG2, (1, 0.5), (0, 1), intent="out")

# All connectors
pfd.connect(name="Elektrika", fromPort=FLAG1["Out"], toPort=Pumpa["In"])
pfd.connect(name="Vroc_plin", fromPort=Pumpa["Out"], toPort=Menjalnik["In"])
pfd.streams["Vroc_plin"].manualRouting = [(step_x / 8, 0), (step_x / 8, -2*step_y)]
pfd.connect(name="Vroc_zrak", fromPort=Menjalnik["OutTop"], toPort=Susenje["OutBottom"])
pfd.connect(name="Dovod_mulja", fromPort=Mulj["Out"], toPort=Susenje["In"])
pfd.connect(name="Nasicen_zrak_85_odstotkov", fromPort=Susenje["OutTop"], toPort=Kondenzator["In"])
pfd.connect(name="/2", fromPort=Kondenzator["Out2"], toPort=FLAG3["In"])
pfd.connect(name="Freon", fromPort=Kondenzator["Out1"], toPort=Pumpa["OutBottom"])
pfd.streams["Freon"].manualRouting = [(step_x / 4, 0), (0, 10*step_y), (-3*size_large[0], 0)]
pfd.connect(name="Zrak_suh", fromPort=Kondenzator["OutTop"], toPort=FLAG2["In"])
pfd.connect(name="40_odstotna_vlaznost_zraka", fromPort=FLAG2["OutLeft"], toPort=Menjalnik["OutBottom"])
pfd.streams["40_odstotna_vlaznost_zraka"].manualRouting = [(2*step_x, 0), (0, 10*step_y), (-4.5*size_large[0], 0)]
pfd.connect(name="/1", fromPort=Menjalnik["OutLeft"], toPort=Kondenzator["InLeft"])
pfd.streams["/1"].manualRouting = [(step_x / 2.5, 0), (0, - 3*step_y), (- 1.25*step_x, 0), (0, - 2*size_large[1])]

# Configure connectors
pfd.streams["Elektrika"].labelOffset = (step_x / 4, -5)
pfd.streams["Vroc_plin"].labelOffset = (step_x / 3.5, -step_y / 2)
pfd.streams["Vroc_zrak"].labelOffset = (step_x / 8, -step_y / 3)
pfd.streams["Dovod_mulja"].labelOffset = (step_x / 5, -5)
pfd.streams["Nasicen_zrak_85_odstotkov"].labelOffset = (5, -step_y / 1.5)
pfd.streams["Freon"].labelOffset = (step_x / 3, 15)
pfd.streams["Zrak_suh"].labelOffset = (step_x / 8, - step_y / 2)
pfd.streams["40_odstotna_vlaznost_zraka"].labelOffset = (step_x, -5)

# Text Configure Elements:
Menjalnik.setTextAnchor(vertical=VerticalLabelAlignment.Center, horizontal=HorizontalLabelAlignment.LeftOuter,
                        offset=(-15, -15))
Pumpa.setTextAnchor(vertical=VerticalLabelAlignment.Top, horizontal=HorizontalLabelAlignment.Center,
                        offset=(-5, - 15))

# Adding text without BlackBox-es (10 in position x subtracted because text should not start in the middle
pfd.callout(text=f"ZRAK Ψ = 40%", position=(150 + 1.5*step_x, 1700))
pfd.callout(text=f"Emisije Elektrike: \n0.49 kg CO\u2082/kWh", position=(150, 1700))

ctx = SvgContext(path)
img = pfd.draw(ctx)
SVG(img.render(width=800, height=2000))


