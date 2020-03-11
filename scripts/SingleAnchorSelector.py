#MenuTitle: Single Anchor Selector
# -*- coding: utf-8 -*-
__doc__="""
Selects all anchors in current glyph.
"""

from robofab.interface.all.dialogs import AskString, Message

layer = Glyphs.font.selectedLayers[0]

def switch():
	anchor = int(AskString("1:top, 2:bottom, 3:center, 4:topleft, 5:topright, 6:all"))
	
	def top():
		for a in layer.anchors:
			a.selected = False
		layer.anchors["top"].selected = True

	def bottom():
		for a in layer.anchors:
			a.selected = False
		layer.anchors["bottom"].selected = True

	def center():
		for a in layer.anchors:
			a.selected = False
		layer.anchors["center"].selected = True

	def topleft():
		for a in layer.anchors:
			a.selected = False
		layer.anchors["topleft"].selected = True

	def topright():
		for a in layer.anchors:
			a.selected = False
		layer.anchors["topright"].selected = True

	def total():
		for a in layer.anchors:
			a.selected = True

	def default():
		Message("Invalid option")

	dict = {
		1:top,
		2:bottom,
		3:center,
		4:topleft,
		5:topright,
		6:total,
	}

	dict.get(anchor, default)()

switch()