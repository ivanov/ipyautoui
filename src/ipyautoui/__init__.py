"""
ipyautoui is used to quickly and efficiently create ipywidgets from pydantic schema.

The module has the capability to take a pydantic schema and create a ipywidget from that schema.
The main features being that you can produce a widget from many field types and also save the
data as a JSON easily.

ipyautoui is designed to be extensible. 
all widgets, as a minimum must satisfy the following criteria: 
- be initiated by the following keyword arguments (in addition to others as required):
    - schema
    - value
- the schema must be a valid jsonschema and where possible use the terms defined in jsonschema

Example::

    from ipyautoui.constants import DISPLAY_AUTOUI_SCHEMA_EXAMPLE
    DISPLAY_AUTOUI_SCHEMA_EXAMPLE()
    
"""
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parents[1]))
# #  ^ for dev only. TODO: comment out at build time

from ipyautoui.autoui import AutoUi, AutoVjsf
from ipyautoui.autodisplay import AutoDisplay
